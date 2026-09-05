"""Password-based AES-GCM encryption for experiment payloads.

This module deliberately uses the well-reviewed ``cryptography`` package rather
than implementing cryptography ourselves.  The returned encrypted payload
contains the salt and nonce needed for decryption, but never the passphrase.
"""

from __future__ import annotations

import os
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

MAGIC = b"SGSB"  # Identifies a payload made by this project.
VERSION = b"\x01"
SALT_BYTES = 16
NONCE_BYTES = 12
KEY_BYTES = 32


def _derive_key(passphrase: str, salt: bytes) -> bytes:
    """Turn a user passphrase into a 256-bit AES key."""
    if not isinstance(passphrase, str) or not passphrase:
        raise ValueError("A non-empty passphrase is required.")
    return Scrypt(salt=salt, length=KEY_BYTES, n=2**14, r=8, p=1).derive(
        passphrase.encode("utf-8")
    )


def encrypt(plaintext: bytes, passphrase: str) -> bytes:
    """Encrypt bytes and return a self-contained payload safe to embed."""
    if not isinstance(plaintext, bytes):
        raise TypeError("Plaintext must be bytes.")

    salt = os.urandom(SALT_BYTES)
    nonce = os.urandom(NONCE_BYTES)
    key = _derive_key(passphrase, salt)
    ciphertext = AESGCM(key).encrypt(nonce, plaintext, None)
    return MAGIC + VERSION + salt + nonce + ciphertext


def decrypt(payload: bytes, passphrase: str) -> bytes:
    """Decrypt a project payload or raise ValueError on any safe failure."""
    minimum_size = len(MAGIC) + len(VERSION) + SALT_BYTES + NONCE_BYTES + 16
    if not isinstance(payload, bytes) or len(payload) < minimum_size:
        raise ValueError("The hidden payload is incomplete or invalid.")
    if payload[: len(MAGIC)] != MAGIC or payload[len(MAGIC) : len(MAGIC) + 1] != VERSION:
        raise ValueError("This file does not contain a supported project payload.")

    salt_start = len(MAGIC) + len(VERSION)
    salt = payload[salt_start : salt_start + SALT_BYTES]
    nonce_start = salt_start + SALT_BYTES
    nonce = payload[nonce_start : nonce_start + NONCE_BYTES]
    ciphertext = payload[nonce_start + NONCE_BYTES :]

    try:
        return AESGCM(_derive_key(passphrase, salt)).decrypt(nonce, ciphertext, None)
    except InvalidTag as error:
        raise ValueError("Incorrect passphrase or altered hidden data.") from error

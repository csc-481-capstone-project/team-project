import pytest

from app.crypto import decrypt, encrypt


def test_encrypt_then_decrypt_returns_original_message():
    secret = encrypt(b"Hello, team!", "correct horse battery staple")
    assert decrypt(secret, "correct horse battery staple") == b"Hello, team!"


def test_wrong_passphrase_fails_safely():
    secret = encrypt(b"Hello", "right-password")
    with pytest.raises(ValueError, match="Incorrect passphrase"):
        decrypt(secret, "wrong-password")

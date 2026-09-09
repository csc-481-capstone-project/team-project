"""Educational zero-width-character text carrier.

This carrier is intentionally limited: some programs strip these characters.
It should be used only for the documented educational experiment workflow.
"""

from __future__ import annotations

from pathlib import Path

ZERO = "\u200b"  # zero-width space
ONE = "\u200c"   # zero-width non-joiner
LENGTH_BYTES = 4


def capacity(cover_text: str) -> int:
    """Return bytes that fit by placing one hidden bit after each visible character."""
    return max(0, len(cover_text) // 8 - LENGTH_BYTES)


def _bits(data: bytes):
    for byte in data:
        for shift in range(7, -1, -1):
            yield (byte >> shift) & 1


def embed(cover_text: str, payload: bytes, output_path: str | Path) -> None:
    """Write visibly unchanged cover text containing the hidden payload."""
    if ZERO in cover_text or ONE in cover_text:
        raise ValueError("Cover text already contains this carrier's marker characters.")
    if len(payload) > capacity(cover_text):
        raise ValueError("Payload is too large for this cover text.")

    stream = iter(_bits(len(payload).to_bytes(LENGTH_BYTES, "big") + payload))
    parts = []
    for character in cover_text:
        parts.append(character)
        try:
            parts.append(ONE if next(stream) else ZERO)
        except StopIteration:
            parts.append("")
    Path(output_path).write_text("".join(parts), encoding="utf-8")


def extract(stego_text: str) -> bytes:
    """Recover payload bytes from text created by embed."""
    bits = [0 if character == ZERO else 1 for character in stego_text if character in (ZERO, ONE)]

    def read_bytes(start_bit: int, count: int) -> bytes:
        required = start_bit + count * 8
        if required > len(bits):
            raise ValueError("Hidden payload is incomplete or invalid.")
        return bytes(
            sum(bits[start_bit + byte * 8 + shift] << (7 - shift) for shift in range(8))
            for byte in range(count)
        )

    payload_length = int.from_bytes(read_bytes(0, LENGTH_BYTES), "big")
    if payload_length > max(0, len(bits) // 8 - LENGTH_BYTES):
        raise ValueError("Embedded payload length is invalid.")
    return read_bytes(LENGTH_BYTES * 8, payload_length)

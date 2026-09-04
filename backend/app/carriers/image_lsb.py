"""PNG RGB/RGBA least-significant-bit carrier.

The first 32 embedded bits store the encrypted payload length.  The remaining
bits store the encrypted payload itself.  Only lossless PNG output is supported.
"""

from __future__ import annotations

from pathlib import Path
from PIL import Image

LENGTH_BYTES = 4


def capacity(image_path: str | Path) -> int:
    """Return the number of payload bytes that fit in an RGB/RGBA PNG."""
    with Image.open(image_path) as image:
        if image.mode not in ("RGB", "RGBA"):
            raise ValueError("Only RGB or RGBA PNG images are supported.")
        channels_used = 3  # Do not alter transparency values.
        return max(0, (image.width * image.height * channels_used) // 8 - LENGTH_BYTES)


def _bits(data: bytes):
    for byte in data:
        for shift in range(7, -1, -1):
            yield (byte >> shift) & 1


def embed(image_path: str | Path, payload: bytes, output_path: str | Path) -> None:
    """Embed payload bytes in a PNG and save the result to output_path."""
    if len(payload) > capacity(image_path):
        raise ValueError("Payload is too large for this image.")

    with Image.open(image_path) as source:
        if source.mode not in ("RGB", "RGBA"):
            raise ValueError("Only RGB or RGBA PNG images are supported.")
        image = source.copy()

    stream = _bits(len(payload).to_bytes(LENGTH_BYTES, "big") + payload)
    pixels = []
    finished = False
    for pixel in image.getdata():
        values = list(pixel)
        for index in range(3):
            try:
                values[index] = (values[index] & 0b11111110) | next(stream)
            except StopIteration:
                finished = True
                break
        pixels.append(tuple(values))
        if finished:
            pixels.extend(list(image.getdata())[len(pixels) :])
            break

    image.putdata(pixels)
    image.save(output_path, format="PNG")


def extract(image_path: str | Path) -> bytes:
    """Recover the embedded payload bytes from a PNG."""
    with Image.open(image_path) as image:
        if image.mode not in ("RGB", "RGBA"):
            raise ValueError("Only RGB or RGBA PNG images are supported.")
        bits = [channel & 1 for pixel in image.getdata() for channel in pixel[:3]]

    def read_bytes(start_bit: int, count: int) -> bytes:
        return bytes(
            sum(bits[start_bit + byte * 8 + shift] << (7 - shift) for shift in range(8))
            for byte in range(count)
        )

    payload_length = int.from_bytes(read_bytes(0, LENGTH_BYTES), "big")
    if payload_length > capacity(image_path):
        raise ValueError("Embedded payload length is invalid.")
    return read_bytes(LENGTH_BYTES * 8, payload_length)

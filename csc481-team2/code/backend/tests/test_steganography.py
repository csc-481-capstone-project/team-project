from pathlib import Path

from PIL import Image

from app.services.steganography import encode_payload


def read_hidden_payload(image_path: Path) -> bytes:
    """Read the STEG header and payload directly from RGB LSBs for this test."""
    with Image.open(image_path) as image:
        pixel_bytes = image.convert("RGBA").tobytes()

    bits = []
    for byte_index in range(0, len(pixel_bytes), 4):
        bits.append(pixel_bytes[byte_index] & 1)
        bits.append(pixel_bytes[byte_index + 1] & 1)
        bits.append(pixel_bytes[byte_index + 2] & 1)

    def read_bytes(start_bit: int, byte_count: int) -> bytes:
        return bytes(
            sum(
                bits[start_bit + byte_number * 8 + bit_number]
                << (7 - bit_number)
                for bit_number in range(8)
            )
            for byte_number in range(byte_count)
        )

    header = read_bytes(0, 8)

    assert header[:4] == b"STEG"

    payload_length = int.from_bytes(header[4:8], "big")

    return read_bytes(64, payload_length)


def test_encode_payload_hides_message_in_png(tmp_path):
    cover_image = tmp_path / "cover.png"
    encoded_image = tmp_path / "encoded.png"
    payload = b"Hello from Team 2!"

    Image.new("RGB", (100, 100), color=(100, 150, 200)).save(cover_image)

    encode_payload(cover_image, encoded_image, payload)

    assert read_hidden_payload(encoded_image) == payload
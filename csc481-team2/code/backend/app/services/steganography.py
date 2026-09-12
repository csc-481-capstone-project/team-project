from pathlib import Path

from PIL import Image


def encode_payload(input_path: Path, output_path: Path, payload: bytes) -> None:
    """Hide binary payload bytes inside a PNG using RGB least-significant bits."""

    if not isinstance(payload, bytes):
        raise TypeError("Payload must be bytes.")

    # This header lets the future decoder find the payload length.
    payload = b"STEG" + len(payload).to_bytes(4, "big") + payload

    # Convert every payload byte into eight 0/1 bits.
    payload_bits = []
    for byte in payload:
        for bit_position in range(7, -1, -1):
            payload_bits.append((byte >> bit_position) & 1)

    with Image.open(input_path) as original_image:
        image = original_image.convert("RGBA")

    pixel_bytes = bytearray(image.tobytes())

    # Only use red, green, and blue channels; preserve alpha transparency.
    available_bits = (len(pixel_bytes) // 4) * 3

    if len(payload_bits) > available_bits:
        raise ValueError("The message is too large for this image.")

    bit_index = 0

    for byte_index in range(0, len(pixel_bytes), 4):
        for color_channel in range(3):
            if bit_index >= len(payload_bits):
                break

            current_value = pixel_bytes[byte_index + color_channel]
            next_bit = payload_bits[bit_index]

            # Replace only the final binary digit of the color value.
            pixel_bytes[byte_index + color_channel] = (
                current_value & 0b11111110
            ) | next_bit

            bit_index += 1

        if bit_index >= len(payload_bits):
            break

    encoded_image = Image.frombytes("RGBA", image.size, bytes(pixel_bytes))
    encoded_image.save(output_path, "PNG")
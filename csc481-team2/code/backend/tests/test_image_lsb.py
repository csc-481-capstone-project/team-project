import pytest
from PIL import Image

from app.services import crypto, image_lsb


def test_png_round_trip(tmp_path):
    cover = tmp_path / "cover.png"
    output = tmp_path / "stego.png"
    Image.new("RGB", (40, 40), color=(100, 150, 200)).save(cover)

    image_lsb.embed(cover, b"secret", output)

    assert image_lsb.extract(output) == b"secret"

def test_image_decrypts_original_message(tmp_path):
    input_image = tmp_path / "cover.png"
    output_image = tmp_path / "stego.png"

    Image.new("RGB", (100, 100), color=(255, 255, 255)).save(input_image)

    message = "Hello from Team 2!"
    passphrase = "test-password"

    encrypted_payload = crypto.encrypt(message.encode("utf-8"), passphrase)

    image_lsb.embed(input_image, encrypted_payload, output_image)

    assert image_lsb.decrypt_message(output_image, passphrase) == message


def test_image_rejects_wrong_passphrase(tmp_path):
    input_image = tmp_path / "cover.png"
    output_image = tmp_path / "stego.png"

    Image.new("RGB", (100, 100), color=(255, 255, 255)).save(input_image)

    encrypted_payload = crypto.encrypt(b"Secret message", "correct-password")

    image_lsb.embed(input_image, encrypted_payload, output_image)

    with pytest.raises(ValueError):
        image_lsb.decrypt_message(output_image, "wrong-password")
import pytest

from app.services import crypto, zero_width_text

def test_text_round_trip(tmp_path):
    output = tmp_path / "stego.txt"
    cover = "This is ordinary cover text. " * 20

    zero_width_text.embed(cover, b"secret", output)

    assert zero_width_text.extract(output.read_text(encoding="utf-8")) == b"secret"
def test_zero_width_text_decrypts_original_message(tmp_path):
    output_file = tmp_path / "hidden.txt"
    cover_text = "This is normal cover text. " * 40
    message = "Hello from Team 2!"
    passphrase = "test-password"
    encrypted_payload = crypto.encrypt(message.encode("utf-8"), passphrase)

    zero_width_text.embed(cover_text, encrypted_payload, output_file)

    stego_text = output_file.read_text(encoding="utf-8")

    assert zero_width_text.decrypt_message(stego_text, passphrase) == message

def test_zero_width_text_rejects_wrong_passphrase(tmp_path):
    output_file = tmp_path / "hidden.txt"
    cover_text = "This is normal cover text. " * 40
    passphrase = "correct-password"
    encrypted_payload = crypto.encrypt(b"Secret message", passphrase)
    zero_width_text.embed(cover_text, encrypted_payload, output_file)

    stego_text = output_file.read_text(encoding="utf-8")
    
    with pytest.raises(ValueError):
        zero_width_text.decrypt_message(stego_text, "wrong-password")
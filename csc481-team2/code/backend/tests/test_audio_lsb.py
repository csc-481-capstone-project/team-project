import wave
import pytest

from app.services import audio_lsb, crypto


def test_wav_round_trip(tmp_path):
    cover = tmp_path / "cover.wav"
    output = tmp_path / "stego.wav"
    with wave.open(str(cover), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(8_000)
        wav.writeframes(b"\x00\x00" * 1_000)

    audio_lsb.embed(cover, b"secret", output)

    assert audio_lsb.extract(output) == b"secret"

def test_audio_decrypts_original_message(tmp_path):
    cover_audio = tmp_path / "cover.wav"
    stego_audio = tmp_path / "stego.wav"
    message = "Hello from Team 2!"
    passphrase = "test-password"

    with wave.open(str(cover_audio), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(8_000)
        wav.writeframes(b"\x00\x00" * 5_000)

    encrypted_payload = crypto.encrypt(message.encode("utf-8"), passphrase)

    audio_lsb.embed(cover_audio, encrypted_payload, stego_audio)

    assert audio_lsb.decrypt_message(stego_audio, passphrase) == message


def test_audio_rejects_wrong_passphrase(tmp_path):
    cover_audio = tmp_path / "cover.wav"
    stego_audio = tmp_path / "stego.wav"
    passphrase = "correct-password"

    with wave.open(str(cover_audio), "wb") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(8_000)
        wav.writeframes(b"\x00\x00" * 5_000)

    encrypted_payload = crypto.encrypt(b"Secret message", passphrase)

    audio_lsb.embed(cover_audio, encrypted_payload, stego_audio)

    with pytest.raises(ValueError):
        audio_lsb.decrypt_message(stego_audio, "wrong-password")
import wave

from app.carriers import audio_lsb


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

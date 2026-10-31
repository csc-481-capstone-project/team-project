import wave

from PIL import Image

from app.services import detection


def test_image_detector_returns_low_suspicion_for_unbalanced_lsb_values(tmp_path):
    image_path = tmp_path / "unbalanced.png"

    Image.new("RGB", (10, 10), color=(255, 255, 255)).save(image_path)

    result = detection.analyze_image_lsb(image_path)

    assert result["total_bits_analyzed"] == 300
    assert result["suspicion"] == "low"
    assert result["balance_score"] == 0.0


def test_image_detector_returns_high_suspicion_for_balanced_lsb_values(tmp_path):
    image_path = tmp_path / "balanced.png"

    image = Image.new("RGB", (10, 10))
    image.putdata([(index % 2, index % 2, index % 2) for index in range(100)])
    image.save(image_path)

    result = detection.analyze_image_lsb(image_path)

    assert result["suspicion"] == "high"
    assert result["balance_score"] == 1.0


def test_audio_detector_returns_low_suspicion_for_unbalanced_lsb_values(tmp_path):
    audio_path = tmp_path / "unbalanced.wav"

    with wave.open(str(audio_path), "wb") as audio:
        audio.setnchannels(1)
        audio.setsampwidth(2)
        audio.setframerate(44100)
        audio.writeframes(bytes([0, 0] * 100))

    result = detection.analyze_audio_lsb(audio_path)

    assert result["total_bits_analyzed"] == 100
    assert result["suspicion"] == "low"


def test_audio_detector_returns_high_suspicion_for_balanced_lsb_values(tmp_path):
    audio_path = tmp_path / "balanced.wav"
    frames = bytearray()

    for index in range(100):
        frames.extend((index % 2, 0))

    with wave.open(str(audio_path), "wb") as audio:
        audio.setnchannels(1)
        audio.setsampwidth(2)
        audio.setframerate(44100)
        audio.writeframes(bytes(frames))

    result = detection.analyze_audio_lsb(audio_path)

    assert result["total_bits_analyzed"] == 100
    assert result["suspicion"] == "high"
    assert result["balance_score"] == 1.0


def test_zero_width_detector_returns_low_suspicion_when_no_hidden_text_exists():
    result = detection.analyze_zero_width_text("This is normal visible text.")

    assert result["total_bits_analyzed"] == 0
    assert result["suspicion"] == "low"


def test_zero_width_detector_returns_high_suspicion_for_balanced_hidden_bits():
    stego_text = "\u200b\u200c" * 50

    result = detection.analyze_zero_width_text(stego_text)

    assert result["total_bits_analyzed"] == 100
    assert result["suspicion"] == "high"
    assert result["balance_score"] == 1.0
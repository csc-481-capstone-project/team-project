from PIL import Image

from app.services import detection


def test_detector_returns_low_suspicion_for_unbalanced_lsb_values(tmp_path):
    image_path = tmp_path / "unbalanced.png"

    Image.new("RGB", (10, 10), color=(255, 255, 255)).save(image_path)

    result = detection.analyze_image_lsb(image_path)

    assert result["total_bits_analyzed"] == 300
    assert result["suspicion"] == "low"
    assert result["balance_score"] == 0.0


def test_detector_returns_high_suspicion_for_balanced_lsb_values(tmp_path):
    image_path = tmp_path / "balanced.png"

    image = Image.new("RGB", (10, 10))
    pixels = []

    for index in range(100):
        value = index % 2
        pixels.append((value, value, value))

    image.putdata(pixels)
    image.save(image_path)

    result = detection.analyze_image_lsb(image_path)

    assert result["suspicion"] == "high"
    assert result["balance_score"] == 1.0
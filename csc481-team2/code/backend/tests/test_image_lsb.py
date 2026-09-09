from PIL import Image

from app.carriers import image_lsb


def test_png_round_trip(tmp_path):
    cover = tmp_path / "cover.png"
    output = tmp_path / "stego.png"
    Image.new("RGB", (40, 40), color=(100, 150, 200)).save(cover)

    image_lsb.embed(cover, b"secret", output)

    assert image_lsb.extract(output) == b"secret"

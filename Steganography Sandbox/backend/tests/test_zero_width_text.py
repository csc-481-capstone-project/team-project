from app.carriers import zero_width_text


def test_text_round_trip(tmp_path):
    output = tmp_path / "stego.txt"
    cover = "This is ordinary cover text. " * 20

    zero_width_text.embed(cover, b"secret", output)

    assert zero_width_text.extract(output.read_text(encoding="utf-8")) == b"secret"

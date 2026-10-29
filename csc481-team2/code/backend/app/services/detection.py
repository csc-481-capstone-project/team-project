from __future__ import annotations

from pathlib import Path

from PIL import Image


def analyze_image_lsb(image_path: str | Path) -> dict[str, float | int | str]:
    """Return an LSB-balance score for an RGB or RGBA PNG image."""
    with Image.open(image_path) as image:
        if image.mode not in {"RGB", "RGBA"}:
            raise ValueError("Only RGB or RGBA PNG images are supported.")

        ones = 0
        total_bits = 0

        for pixel in image.get_flattened_data():
            for channel in pixel[:3]:
                ones += channel & 1
                total_bits += 1

    one_ratio = ones / total_bits
    balance_score = 1.0 - abs(one_ratio - 0.5) * 2

    if balance_score >= 0.98:
        suspicion = "high"
    elif balance_score >= 0.90:
        suspicion = "medium"
    else:
        suspicion = "low"

    return {
        "total_bits_analyzed": total_bits,
        "lsb_ones": ones,
        "one_ratio": round(one_ratio, 4),
        "balance_score": round(balance_score, 4),
        "suspicion": suspicion,
    }
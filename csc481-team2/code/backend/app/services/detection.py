from __future__ import annotations

from pathlib import Path

from PIL import Image

def analyze_image_lsb(image_path: str | Path) -> dict[str, float | int | str]:
    """Return an LSB-balance score for an RGB or RGBA PNG image."""
    with Image.open(image_path) as source:
        if source.format != "PNG":
            raise ValueError("Only PNG images are supported.")
        image = source.convert("RGB")

        ones = 0
        total_bits = 0

        for pixel in image.getdata():
            for channel in pixel:
                ones += channel & 1
                total_bits += 1
        
        if total_bits == 0:
            raise ValueError("The image contains no analyzable color data.")

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
        "notice": (
            "This is an educational statistical indicator only. "
            "It cannot prove that hidden data exists in the image."
        ),
    }
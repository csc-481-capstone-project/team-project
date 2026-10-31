from __future__ import annotations

from pathlib import Path
import wave

from PIL import Image

ZERO = "\u200b"
ONE = "\u200c"


def _build_result(ones: int, total_bits: int) -> dict[str, float | int | str]:
    """Build a consistent LSB-balance detection result."""
    if total_bits == 0:
        return {
            "total_bits_analyzed": 0,
            "lsb_ones": 0,
            "one_ratio": 0.0,
            "balance_score": 0.0,
            "suspicion": "low",
        }

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


def analyze_image_lsb(image_path: str | Path) -> dict[str, float | int | str]:
    """Analyze RGB or RGBA PNG least-significant-bit balance."""
    with Image.open(image_path) as image:
        if image.mode not in {"RGB", "RGBA"}:
            raise ValueError("Only RGB or RGBA PNG images are supported.")

        ones = 0
        total_bits = 0

        for pixel in image.get_flattened_data():
            for channel in pixel[:3]:
                ones += channel & 1
                total_bits += 1

    return _build_result(ones, total_bits)


def analyze_audio_lsb(audio_path: str | Path) -> dict[str, float | int | str]:
    """Analyze the least-significant bits used by 16-bit PCM WAV samples."""
    with wave.open(str(audio_path), "rb") as audio:
        if audio.getsampwidth() != 2 or audio.getcomptype() != "NONE":
            raise ValueError("Only uncompressed 16-bit PCM WAV files are supported.")

        frames = audio.readframes(audio.getnframes())

    lsb_bytes = frames[::2]
    ones = sum(byte & 1 for byte in lsb_bytes)

    return _build_result(ones, len(lsb_bytes))


def analyze_zero_width_text(stego_text: str) -> dict[str, float | int | str]:
    """Analyze zero-width characters used to hide binary text data."""
    zero_count = stego_text.count(ZERO)
    one_count = stego_text.count(ONE)
    total_bits = zero_count + one_count

    return _build_result(one_count, total_bits)
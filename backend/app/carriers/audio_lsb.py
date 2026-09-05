"""16-bit PCM WAV least-significant-bit carrier."""

from __future__ import annotations

from pathlib import Path
import wave

LENGTH_BYTES = 4


def _read_wav(path: str | Path):
    with wave.open(str(path), "rb") as source:
        if source.getsampwidth() != 2 or source.getcomptype() != "NONE":
            raise ValueError("Only uncompressed 16-bit PCM WAV files are supported.")
        return source.getparams(), bytearray(source.readframes(source.getnframes()))


def capacity(audio_path: str | Path) -> int:
    """Return the number of payload bytes that fit in a supported WAV file."""
    params, _ = _read_wav(audio_path)
    sample_count = params.nframes * params.nchannels
    return max(0, sample_count // 8 - LENGTH_BYTES)


def _bits(data: bytes):
    for byte in data:
        for shift in range(7, -1, -1):
            yield (byte >> shift) & 1


def embed(audio_path: str | Path, payload: bytes, output_path: str | Path) -> None:
    """Embed payload bytes in a supported WAV and save it."""
    if len(payload) > capacity(audio_path):
        raise ValueError("Payload is too large for this audio file.")
    params, frames = _read_wav(audio_path)
    for sample_offset, bit in zip(range(0, len(frames), 2), _bits(len(payload).to_bytes(4, "big") + payload)):
        frames[sample_offset] = (frames[sample_offset] & 0b11111110) | bit
    with wave.open(str(output_path), "wb") as output:
        output.setparams(params)
        output.writeframes(frames)


def extract(audio_path: str | Path) -> bytes:
    """Recover the embedded payload bytes from a supported WAV file."""
    _, frames = _read_wav(audio_path)
    bits = [frames[offset] & 1 for offset in range(0, len(frames), 2)]

    def read_bytes(start_bit: int, count: int) -> bytes:
        return bytes(
            sum(bits[start_bit + byte * 8 + shift] << (7 - shift) for shift in range(8))
            for byte in range(count)
        )

    payload_length = int.from_bytes(read_bytes(0, LENGTH_BYTES), "big")
    if payload_length > capacity(audio_path):
        raise ValueError("Embedded payload length is invalid.")
    return read_bytes(LENGTH_BYTES * 8, payload_length)

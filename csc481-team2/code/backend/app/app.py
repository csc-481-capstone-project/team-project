from io import BytesIO
from pathlib import Path
from uuid import uuid4
import re
import wave

from flask import Flask, jsonify, render_template, request, send_file
from PIL import Image, UnidentifiedImageError

from services.crypto import encrypt
from services.image_lsb import embed as embed_image
from services.audio_lsb import embed as embed_audio

app = Flask(__name__, template_folder="templates")
# Reject files larger than 500 MB.
app.config["MAX_CONTENT_LENGTH"] = 500 * 1024 * 1024

# Create a private folder beside app.py for uploaded images.
IMAGE_UPLOAD_FOLDER = Path(app.root_path) / "private_uploads"
IMAGE_UPLOAD_FOLDER.mkdir(exist_ok=True)
AUDIO_UPLOAD_FOLDER = Path(app.root_path) / "private_audio_uploads"
AUDIO_UPLOAD_FOLDER.mkdir(exist_ok=True)

IMAGE_OUTPUT_FOLDER = Path(app.root_path) / "private_outputs"
IMAGE_OUTPUT_FOLDER.mkdir(exist_ok=True)
AUDIO_OUTPUT_FOLDER = Path(app.root_path) / "private_audio_outputs"
AUDIO_OUTPUT_FOLDER.mkdir(exist_ok=True)    

MAX_DIMENSION = 4000


@app.route("/")
def home():
    return render_template("image_stego.html")
@app.get("/audio")
def audio_stego():
    return render_template("audio_stego.html")


@app.post("/api/v1/uploads")
def upload_png():
    uploaded_file = request.files.get("image")

    if not uploaded_file or uploaded_file.filename == "":
        return jsonify({"error": "Please select a PNG image."}), 400

    image_data = uploaded_file.read()

    try:
        # Verify that the file contents are a real image.
        with Image.open(BytesIO(image_data)) as image:
            image.verify()

        # Reopen the image and confirm it is PNG and not too large.
        with Image.open(BytesIO(image_data)) as image:
            if image.format != "PNG":
                return jsonify({"error": "Only genuine PNG images are allowed."}), 415

            if image.width > MAX_DIMENSION or image.height > MAX_DIMENSION:
                return jsonify({"error": "Image dimensions are too large."}), 413

    except (UnidentifiedImageError, OSError):
        return jsonify({"error": "The file is not a valid PNG image."}), 415

    # Create a safe server-side filename.
    upload_id = uuid4().hex
    saved_path = IMAGE_UPLOAD_FOLDER / f"{upload_id}.png"
    saved_path.write_bytes(image_data)

    return jsonify({
        "message": "Image uploaded successfully.",
        "upload_id": upload_id
    }), 201

@app.post("/api/v1/encode")
def encode_png():
    data = request.get_json(silent=True) or {}

    upload_id = data.get("upload_id", "")
    secret_message = data.get("message", "")

    # A valid upload ID is the 32-character hexadecimal value created by uuid4().
    if not re.fullmatch(r"[a-f0-9]{32}", upload_id):
        return jsonify({"error": "Invalid upload ID."}), 400

    if not isinstance(secret_message, str) or len(secret_message) < 1:
        return jsonify({"error": "secret_message must be at least 1 character."}), 400

    if len(secret_message) > 100:
        return jsonify({"error": "secret_message must be 100 characters or fewer."}), 400

    input_path = IMAGE_UPLOAD_FOLDER / f"{upload_id}.png"

    if not input_path.exists():
        return jsonify({"error": "Uploaded image was not found."}), 404

    output_id = uuid4().hex
    output_path = IMAGE_OUTPUT_FOLDER / f"{output_id}.png"

    try:
        encrypted_payload = encrypt(secret_message.encode("utf-8"), secret_message)
        embed_image(input_path, encrypted_payload, output_path)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    return jsonify({
        "message": "Message encoded successfully.",
        "output_id": output_id,
        "download_url": f"/api/v1/downloads/{output_id}"
    }), 201
@app.get("/api/v1/downloads/<output_id>")
def download_encoded_image(output_id):
    # Only allow the random 32-character output IDs created by uuid4().
    if not re.fullmatch(r"[a-f0-9]{32}", output_id):
        return jsonify({"error": "Invalid output ID."}), 400

    output_path = IMAGE_OUTPUT_FOLDER / f"{output_id}.png"

    if not output_path.exists():
        return jsonify({"error": "Encoded image was not found."}), 404

    return send_file(
        output_path,
        mimetype="image/png",
        as_attachment=True,
        download_name="encoded_image.png"
    )
@app.post("/api/v1/audio/uploads")
def upload_audio():
    audio_file = request.files.get("audio")

    if not audio_file or audio_file.filename == "":
        return jsonify({"error": "Please select a WAV file."}), 400

    audio_data = audio_file.read()

    try:
        with wave.open(BytesIO(audio_data), "rb") as wav_file:
            if wav_file.getsampwidth() != 2:
                return jsonify({
                    "error": "Only 16-bit WAV files are supported."
                }), 415

            if wav_file.getcomptype() != "NONE":
                return jsonify({
                    "error": "Only uncompressed WAV files are supported."
                }), 415

    except (wave.Error, EOFError):
        return jsonify({"error": "The file is not a valid WAV file."}), 415

    audio_id = uuid4().hex
    saved_path = AUDIO_UPLOAD_FOLDER / f"{audio_id}.wav"
    saved_path.write_bytes(audio_data)

    return jsonify({
        "message": "Audio uploaded successfully.",
        "audio_id": audio_id
    }), 201


@app.post("/api/v1/audio/encode")
def encode_audio():
    data = request.get_json(silent=True) or {}

    audio_id = data.get("audio_id", "")
    secret_message = data.get("message", "")
    passphrase = data.get("passphrase", "")

    if not re.fullmatch(r"[a-f0-9]{32}", audio_id):
        return jsonify({"error": "Invalid audio ID."}), 400

    if not isinstance(secret_message, str) or not secret_message.strip():
        return jsonify({"error": "Enter a message to embed."}), 400

    if not isinstance(passphrase, str) or len(passphrase) < 1:
        return jsonify({
            "error": "Use a passphrase with at least 1 characters."
        }), 400

    input_path = AUDIO_UPLOAD_FOLDER / f"{audio_id}.wav"

    if not input_path.exists():
        return jsonify({"error": "Uploaded audio was not found."}), 404

    output_id = uuid4().hex
    output_path = AUDIO_OUTPUT_FOLDER / f"{output_id}.wav"

    try:
        encrypted_payload = encrypt(
            secret_message.encode("utf-8"),
            passphrase
        )

        embed_audio(input_path, encrypted_payload, output_path)

    except ValueError as error:
        return jsonify({"error": str(error)}), 400

    return jsonify({
        "message": "Message embedded successfully in audio.",
        "output_id": output_id,
        "download_url": f"/api/v1/audio/downloads/{output_id}"
    }), 201


@app.get("/api/v1/audio/downloads/<output_id>")
def download_encoded_audio(output_id):
    if not re.fullmatch(r"[a-f0-9]{32}", output_id):
        return jsonify({"error": "Invalid audio output ID."}), 400

    output_path = AUDIO_OUTPUT_FOLDER / f"{output_id}.wav"

    if not output_path.exists():
        return jsonify({"error": "Encoded audio was not found."}), 404

    return send_file(
        output_path,
        mimetype="audio/wav",
        as_attachment=True,
        download_name="encoded_audio.wav"
    )


@app.errorhandler(413)
def file_too_large(error):
    return jsonify({"error": "files must be 500 MB or smaller."}), 413


if __name__ == "__main__":
    app.run(debug=True)
from io import BytesIO
from pathlib import Path
from uuid import uuid4
import re

from flask import Flask, jsonify, render_template, request, send_file
from PIL import Image, UnidentifiedImageError

from services.steganography import encode_message

app = Flask(__name__, template_folder="templates")
# Reject files larger than 5 MB.
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

# Create a private folder beside app.py for uploaded images.
UPLOAD_FOLDER = Path(app.root_path) / "private_uploads"
UPLOAD_FOLDER.mkdir(exist_ok=True)

OUTPUT_FOLDER = Path(app.root_path) / "private_outputs"
OUTPUT_FOLDER.mkdir(exist_ok=True)

MAX_DIMENSION = 4000


@app.route("/")
def home():
    return render_template("upload.html")


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
    saved_path = UPLOAD_FOLDER / f"{upload_id}.png"
    saved_path.write_bytes(image_data)

    return jsonify({
        "message": "Image uploaded successfully.",
        "upload_id": upload_id
    }), 201

@app.post("/api/v1/encode")
def encode_png():
    data = request.get_json(silent=True) or {}

    upload_id = data.get("upload_id", "")
    message = data.get("message", "")

    # A valid upload ID is the 32-character hexadecimal value created by uuid4().
    if not re.fullmatch(r"[a-f0-9]{32}", upload_id):
        return jsonify({"error": "Invalid upload ID."}), 400

    if not isinstance(message, str) or not message.strip():
        return jsonify({"error": "Please enter a message to encode."}), 400

    if len(message) > 500:
        return jsonify({"error": "Message must be 500 characters or fewer."}), 400

    input_path = UPLOAD_FOLDER / f"{upload_id}.png"

    if not input_path.exists():
        return jsonify({"error": "Uploaded image was not found."}), 404

    output_id = uuid4().hex
    output_path = OUTPUT_FOLDER / f"{output_id}.png"

    try:
        encode_message(input_path, output_path, message)
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

    output_path = OUTPUT_FOLDER / f"{output_id}.png"

    if not output_path.exists():
        return jsonify({"error": "Encoded image was not found."}), 404

    return send_file(
        output_path,
        mimetype="image/png",
        as_attachment=True,
        download_name="encoded_image.png"
    )


@app.errorhandler(413)
def file_too_large(error):
    return jsonify({"error": "Image must be 5 MB or smaller."}), 413


if __name__ == "__main__":
    app.run(debug=True)
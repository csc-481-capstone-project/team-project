from pathlib import Path
from playwright.sync_api import Page

# Test files
TEST_DIR = Path(__file__).parent
SAMPLE_PNG = TEST_DIR / "sample.png"
SAMPLE_WAV = TEST_DIR / "sample.wav"

# Frontend pages
BASE_URL = (
    "http://127.0.0.1:3000/"
    "csc481-team2/code/backend/app/templates/"
)

IMAGE_URL = BASE_URL + "image_stego.html"
AUDIO_URL = BASE_URL + "audio_stego.html"
ZERO_WIDTH_URL = BASE_URL + "zero_width_stego.html"



# ==================================================
#       IMAGE STEGANOGRAPHY - EMBEDDING TESTS
# ==================================================

def test_image_missing_upload(page: Page):
    page.goto(IMAGE_URL)

    page.locator("#secretMessage").fill("Hello world")
    page.locator("#passphrase").fill("test123")
    page.locator("#imageStegoForm button[type='submit']").click()

    assert not page.locator("#imageUpload").evaluate(
        "element => element.validity.valid"
    )


def test_image_missing_message(page: Page):
    page.goto(IMAGE_URL)

    page.set_input_files("#imageUpload", str(SAMPLE_PNG))
    page.locator("#passphrase").fill("test123")
    page.locator("#imageStegoForm button[type='submit']").click()

    assert not page.locator("#secretMessage").evaluate(
        "element => element.validity.valid"
    )


def test_image_missing_passphrase(page: Page):
    page.goto(IMAGE_URL)

    page.set_input_files("#imageUpload", str(SAMPLE_PNG))
    page.locator("#secretMessage").fill("Hello world")
    page.locator("#imageStegoForm button[type='submit']").click()

    assert not page.locator("#passphrase").evaluate(
        "element => element.validity.valid"
    )


def test_image_valid_submission(page: Page):
    page.goto(IMAGE_URL)

    page.route(
        "**/api/v1/uploads",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body='{"upload_id": "test-image-123"}'
        )
    )

    page.route(
        "**/api/v1/encode",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body='{"download_url": "/downloads/test-encoded.png"}'
        )
    )

    page.set_input_files("#imageUpload", str(SAMPLE_PNG))
    page.locator("#secretMessage").fill("Hello world")
    page.locator("#passphrase").fill("test123")
    page.locator("#imageStegoForm button[type='submit']").click()

    page.locator("#statusMessage").get_by_text(
        "Message embedded successfully."
    ).wait_for()

    assert "Message embedded successfully." in (
        page.locator("#statusMessage").inner_text()
    )



# ==================================================
#       IMAGE STEGANOGRAPHY - DECRYPTION TESTS
# ==================================================

def test_image_missing_extraction_upload(page: Page):
    page.goto(IMAGE_URL)

    page.locator("#extractPassphrase").fill("test123")
    page.locator("#imageExtractForm button[type='submit']").click()

    assert not page.locator("#encodedImageUpload").evaluate(
        "element => element.validity.valid"
    )


def test_image_missing_extraction_passphrase(page: Page):
    page.goto(IMAGE_URL)

    page.set_input_files("#encodedImageUpload", str(SAMPLE_PNG))
    page.locator("#imageExtractForm button[type='submit']").click()

    assert not page.locator("#extractPassphrase").evaluate(
        "element => element.validity.valid"
    )


def test_image_extracted_message_readonly(page: Page):
    page.goto(IMAGE_URL)

    extracted_message = page.locator("#extractedMessage")

    assert extracted_message.count() == 1
    assert extracted_message.get_attribute("readonly") is not None



# ==================================================
#       AUDIO STEGANOGRAPHY - EMBEDDING TESTS
# ==================================================

def test_audio_missing_upload(page: Page):
    page.goto(AUDIO_URL)

    page.locator("#secretMessage").fill("Hello world")
    page.locator("#passphrase").fill("test123")
    page.locator("#audioStegoForm button[type='submit']").click()

    assert not page.locator("#audioUpload").evaluate(
        "element => element.validity.valid"
    )


def test_audio_missing_message(page: Page):
    page.goto(AUDIO_URL)

    page.set_input_files("#audioUpload", str(SAMPLE_WAV))
    page.locator("#passphrase").fill("test123")
    page.locator("#audioStegoForm button[type='submit']").click()

    assert not page.locator("#secretMessage").evaluate(
        "element => element.validity.valid"
    )


def test_audio_missing_passphrase(page: Page):
    page.goto(AUDIO_URL)

    page.set_input_files("#audioUpload", str(SAMPLE_WAV))
    page.locator("#secretMessage").fill("Hello world")
    page.locator("#audioStegoForm button[type='submit']").click()

    assert not page.locator("#passphrase").evaluate(
        "element => element.validity.valid"
    )


def test_audio_valid_submission(page: Page):
    page.goto(AUDIO_URL)

    page.route(
        "**/api/v1/audio/uploads",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body='{"audio_id": "test-audio-123"}'
        )
    )

    page.route(
        "**/api/v1/audio/encode",
        lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body='{"download_url": "downloads/test-encoded.wav"}'
        )
    )

    page.set_input_files("#audioUpload", str(SAMPLE_WAV))
    page.locator("#secretMessage").fill("Hello world")
    page.locator("#passphrase").fill("test123")
    page.locator("#audioStegoForm button[type='submit']").click()

    page.locator("#statusMessage").get_by_text(
        "Message embedded successfully in audio."
    ).wait_for()

    assert "Message embedded successfully in audio." in (
        page.locator("#statusMessage").inner_text()
    )



# ==================================================
#       AUDIO STEGANOGRAPHY - DECRYPTION TESTS
# ==================================================

def test_audio_missing_extraction_upload(page: Page):
    page.goto(AUDIO_URL)

    page.locator("#extractPassphrase").fill("test123")
    page.locator("#audioExtractForm button[type='submit']").click()

    assert not page.locator("#extractAudioUpload").evaluate(
        "element => element.validity.valid"
    )


def test_audio_missing_extraction_passphrase(page: Page):
    page.goto(AUDIO_URL)

    page.set_input_files("#extractAudioUpload", str(SAMPLE_WAV))
    page.locator("#audioExtractForm button[type='submit']").click()

    assert not page.locator("#extractPassphrase").evaluate(
        "element => element.validity.valid"
    )


def test_audio_extracted_message_readonly(page: Page):
    page.goto(AUDIO_URL)

    extracted_message = page.locator("#extractedMessage")

    assert extracted_message.count() == 1
    assert extracted_message.get_attribute("readonly") is not None



# ==================================================
#    ZERO-WIDTH STEGANOGRAPHY - DECRYPTION TESTS
# ==================================================

def test_zero_width_missing_encoded_text(page: Page):
    page.goto(ZERO_WIDTH_URL)

    page.locator("#decodePassphrase").fill("test123")
    page.locator("#zeroWidthDecodeForm button[type='submit']").click()

    assert not page.locator("#stegoText").evaluate(
        "element => element.validity.valid"
    )


def test_zero_width_missing_decode_passphrase(page: Page):
    page.goto(ZERO_WIDTH_URL)

    page.locator("#stegoText").fill("Sample encoded text")
    page.locator("#zeroWidthDecodeForm button[type='submit']").click()

    assert not page.locator("#decodePassphrase").evaluate(
        "element => element.validity.valid"
    )


def test_zero_width_decoded_message_readonly(page: Page):
    page.goto(ZERO_WIDTH_URL)

    decoded_message = page.locator("#decodedMessage")

    assert decoded_message.count() == 1
    assert decoded_message.get_attribute("readonly") is not None



# ==================================================
#          STATISTICAL DETECTION TESTS
# ==================================================

def test_image_statistical_detection_ui(page: Page):
    page.goto(IMAGE_URL)

    assert page.locator("#imageDetectionForm").is_visible()
    assert page.locator("#detectionImageUpload").is_visible()
    assert page.locator("#imageDetectionStatus").count() == 1
    assert page.locator("#imageDetectionResults").is_hidden()


def test_audio_statistical_detection_ui(page: Page):
    page.goto(AUDIO_URL)

    assert page.locator("#audioDetectionForm").is_visible()
    assert page.locator("#detectionAudioUpload").is_visible()
    assert page.locator("#audioDetectionStatus").count() == 1
    assert page.locator("#audioDetectionResults").is_hidden()


def test_zero_width_statistical_detection_ui(page: Page):
    page.goto(ZERO_WIDTH_URL)

    assert page.locator("#zeroWidthDetectionForm").is_visible()
    assert page.locator("#detectionZeroWidthText").is_visible()
    assert page.locator("#analyzeTextButton").is_visible()
    assert page.locator("#zeroWidthDetectionStatus").count() == 1
    assert page.locator("#zeroWidthDetectionResults").is_hidden()



# ==================================================
#                 PDF REPORT TESTS
# ==================================================

def test_image_pdf(page: Page):
    page.goto(IMAGE_URL)

    assert page.locator("#imagePDFReport").is_hidden()
    assert page.locator("#imagePDFDownload").count() == 1


def test_audio_pdf(page: Page):
    page.goto(AUDIO_URL)

    assert page.locator("#audioPDFReport").is_hidden()
    assert page.locator("#audioPDFDownload").count() == 1


def test_zero_width_pdf(page: Page):
    page.goto(ZERO_WIDTH_URL)

    assert page.locator("#zeroWidthPDFReport").is_hidden()
    assert page.locator("#zeroWidthPDFDownload").count() == 1
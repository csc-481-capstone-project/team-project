PAGE_URL = "http://127.0.0.1:3000/csc481-team2/code/backend/app/templates/audio_stego.html?"


## Test Missing Audio File
def test_missing_extraction_audio(page):
    page.goto(PAGE_URL)

    page.locator("#extractPassphrase").fill("test123")

    page.locator("#audioExtractForm button[type='submit']").click()

    is_valid = page.locator("#audioExtractUpload").evaluate(
        "element => element.validity.valid"
    )

    assert is_valid is False

## Test Missing Passphrase
def test_missing_extraction_passphrase(page):
    page.goto(PAGE_URL)

    page.set_input_files("#audioExtractUpload", "tests/sample.wav")

    page.locator("#audioExtractForm button[type='submit']").click()

    is_valid = page.locator("#extractPassphrase").evaluate(
        "element => element.validity.valid"
    )

    assert is_valid is False

## Test Extracted Message Output
def test_extracted_message_readonly(page):
    page.goto(PAGE_URL)

    extracted_message = page.locator("#extractedMessage")

    assert extracted_message.count() == 1
    assert extracted_message.get_attribute("readonly") is not None
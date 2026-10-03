PAGE_URL = "http://127.0.0.1:3000/csc481-team2/code/backend/app/templates/zero_width_stego.html?"

## Test Missing Encoded Text
def test_missing_encoded_text(page):
    page.goto(PAGE_URL)

    page.locator("#decodePassphrase").fill("test123")

    page.locator("#zeroWidthDecodeForm button[type='submit']").click()

    is_valid = page.locator("#stegoText").evaluate(
        "element => element.validity.valid"
    )

    assert is_valid is False


## Test Missing Decode Passphrase
def test_missing_decode_passphrase(page):
    page.goto(PAGE_URL)

    page.locator("#stegoText").fill("Sample encoded text")

    page.locator("#zeroWidthDecodeForm button[type='submit']").click()

    is_valid = page.locator("#decodePassphrase").evaluate(
        "element => element.validity.valid"
    )

    assert is_valid is False


## Test Decoded Message Output
def test_decoded_message_readonly(page):
    page.goto(PAGE_URL)

    decoded_message = page.locator("#decodedMessage")

    assert decoded_message.count() == 1
    assert decoded_message.get_attribute("readonly") is not None
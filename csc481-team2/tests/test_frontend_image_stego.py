PAGE_URL = "http://127.0.0.1:3000/csc481-team2/code/backend/app/templates/image_stego.html?"

## Test Missing Image
def test_missing_image(page):
    page.goto(PAGE_URL)

    page.locator("#secretMessage").fill("Hello world")
    page.locator("#passphrase").fill("test123")

    page.locator("button[type='submit']").click()

    is_valid = page.locator("#imageUpload").evaluate(
        "element => element.validity.valid"
    )

    assert is_valid is False


## Test Missing Secret Message
def test_missing_secret_message(page):
    page.goto(PAGE_URL)

    page.set_input_files("#imageUpload", "csc481-team2/tests/sample.png")
    page.locator("#passphrase").fill("test123")

    page.locator("button[type='submit']").click()

    is_valid = page.locator("#secretMessage").evaluate(
        "element => element.validity.valid"
    )

    assert is_valid is False


## Test Missing Passphrase
def test_missing_passphrase(page):
    page.goto(PAGE_URL)

    page.set_input_files("#imageUpload", "csc481-team2/tests/sample.png")
    page.locator("#secretMessage").fill("Hello world")

    page.locator("button[type='submit']").click()

    is_valid = page.locator("#passphrase").evaluate(
        "element => element.validity.valid"
    )

    assert is_valid is False


### Test Valid Submission
def test_valid_submission(page):
    page.goto(PAGE_URL)

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

    page.set_input_files("#imageUpload", "csc481-team2/tests/sample.png")
    page.locator("#secretMessage").fill("Hello world")
    page.locator("#passphrase").fill("test123")

    page.locator("button[type='submit']").click()

    page.locator("#statusMessage").get_by_text("Message embedded successfully.").wait_for()

    status = page.locator("#statusMessage").inner_text()

    assert "Message embedded successfully." in status


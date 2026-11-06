from playwright.sync_api import Page


## Image PDF Report
def test_image_pdf(page: Page):
    page.goto("http://127.0.0.1:3000/csc481-team2/code/backend/app/templates/image_stego.html?")

    assert page.locator("#imagePDFReport").is_hidden()
    assert page.locator("#imagePDFDownload").count() == 1


## Audio PDF Report
def test_audio_pdf(page: Page):
    page.goto("http://127.0.0.1:3000/csc481-team2/code/backend/app/templates/audio_stego.html?")

    assert page.locator("#audioPDFReport").is_hidden()
    assert page.locator("#audioPDFDownload").count() == 1


## Zero-Width PDF Report
def test_zero_width_pdf(page: Page):
    page.goto("http://127.0.0.1:3000/csc481-team2/code/backend/app/templates/zero_width_stego.html?")

    assert page.locator("#zeroWidthPDFReport").is_hidden()
    assert page.locator("#zeroWidthPDFDownload").count() == 1
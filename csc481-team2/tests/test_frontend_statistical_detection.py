import pytest
from playwright.sync_api import Page

## Image Statistical Detection
def test_image_statistical_detection_ui(page: Page):
    page.goto("http://127.0.0.1:3000/csc481-team2/code/backend/app/templates/image_stego.html?")

    assert page.locator("#imageDetectionForm").is_visible()
    assert page.locator("#detectionImageUpload").is_visible()
    assert page.locator("#imageDetectionStatus").count() == 1
    assert page.locator("#imageDetectionResults").is_hidden()

## Audio Statistical Detection
def test_audio_statistical_detection_ui(page: Page):
    page.goto("http://127.0.0.1:3000/csc481-team2/code/backend/app/templates/audio_stego.html?")

    assert page.locator("#audioDetectionForm").is_visible()
    assert page.locator("#detectionAudioUpload").is_visible()
    assert page.locator("#audioDetectionStatus").count() == 1
    assert page.locator("#audioDetectionResults").is_hidden()

## Zero-Width Statistical Detection
def test_zero_width_statistical_detection_ui(page: Page):
    page.goto("http://127.0.0.1:3000/csc481-team2/code/backend/app/templates/zero_width_stego.html?")

    assert page.locator("#zeroWidthDetectionForm").is_visible()
    assert page.locator("#detectionZeroWidthText").is_visible()
    assert page.locator("#analyzeTextButton").is_visible()
    assert page.locator("#zeroWidthDetectionStatus").count() == 1
    assert page.locator("#zeroWidthDetectionResults").is_hidden()
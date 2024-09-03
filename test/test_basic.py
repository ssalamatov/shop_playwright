from playwright.sync_api import Page


def test_app_works(base_url, page: Page):
    page.goto(base_url)

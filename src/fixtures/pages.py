import pytest

from playwright.sync_api import Page

from src.pages.products import Products
from src.pages.navigation import Navigation
from src.pages.checkout import Checkout


@pytest.fixture()
def products(page: Page):
    return Products(page)


@pytest.fixture()
def nav(page: Page):
    return Navigation(page)


@pytest.fixture()
def checkout(page: Page):
    return Checkout(page)

import pytest

from dataclasses import dataclass


from playwright.sync_api import Page

from src.pages.products import Products
from src.pages.navigation import Navigation
from src.pages.checkout import Checkout


@dataclass
class App:
    products: Products
    nav: Navigation
    checkout: Checkout


@pytest.fixture()
def products(page: Page):
    return Products(page)


@pytest.fixture()
def nav(page: Page):
    return Navigation(page)


@pytest.fixture()
def checkout(page: Page):
    return Checkout(page)


@pytest.fixture()
def app(products, nav, checkout):
    return App(
        products=products, nav=nav, checkout=checkout
    )

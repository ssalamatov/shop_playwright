import pytest
from playwright.sync_api import Page

from src.pages.products import Products


@pytest.fixture()
def products(page: Page):
    return Products(page)


def test_add_product_to_basket(base_url, products: Products):
    products.visit(base_url)
    products.add_product_to_basket(1)

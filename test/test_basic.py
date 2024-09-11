import pytest

from src.fixtures.pages import App
from test.data.products import test_products


param = pytest.mark.parametrize


def test_get_all_products(base_url, app: App):
    """
        1. go to products page
        2. all products are existed on page
    """
    app.products.visit(base_url)
    app.products.find_products(test_products)


@param("product_id", [1])
def test_add_product_to_basket(
        base_url, product_id: int, app: App
):
    """
        1. go to products page
        2. add 1 product to basket
        3. move to checkout
    """
    app.products.visit(base_url)
    app.products.add_product_to_basket(product_id)

    app.nav.go_to_checkout()


@param("product_id", [1])
def test_remove_product_from_basket(
        base_url, product_id: int, app: App
):
    """
        1. go to products page
        2. add 1 product to basket
        3. move to checkout
        4. remove product from basket
        5. product is removed
    """
    app.products.visit(base_url)
    app.products.add_product_to_basket(product_id)
    app.nav.go_to_checkout()

    first = 0
    app.checkout.remove_product_from_basket(first)

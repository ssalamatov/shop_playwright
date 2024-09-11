import pytest

from src.fixtures.pages import App
from test.data.products import test_products


param = pytest.mark.parametrize


def test_get_all_products(base_url, app: App):
    app.products.visit(base_url)
    app.products.find_products(test_products)


@param("product_id", [1])
def test_add_product_to_basket(
        base_url, product_id: int, app: App
):
    app.products.visit(base_url)
    app.products.add_product_to_basket(product_id)
    app.nav.go_to_checkout()


def test_remove_product_from_basket(base_url, app: App):
    app.products.visit(base_url)

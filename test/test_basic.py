import pytest

from src.pages.products import Products, Navigation
from src.pages.checkout import Checkout

from test.data.products import test_products


param = pytest.mark.parametrize


def test_get_all_products(base_url, products: Products):
    products.visit(base_url)
    products.find_products(test_products)


@param("product_id", [1])
def test_add_product_to_basket(
        base_url, product_id: int, products: Products,
        nav: Navigation, checkout: Checkout
):
    products.visit(base_url)
    products.add_product_to_basket(product_id)
    nav.go_to_checkout()

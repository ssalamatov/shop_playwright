from playwright.sync_api import Page, expect

from typing import List

from src.pages.navigation import Navigation
from src.models.product import ProductModel


class Products:
    url = "/"

    def __init__(self, page: Page):
        self.page = page
        self.add_buttons = '[data-qa="product-button"]'
        self.list_cards = '[data-qa="product-title"]'

    def get_path(self, base_url):
        return f"{base_url}/{self.url}"

    def visit(self, base_url):
        url = self.get_path(base_url)
        self.page.goto(url)

    def add_product_to_basket(self, product_id: int):
        buttons = self.page.locator(self.add_buttons)

        button = buttons.nth(product_id)
        button.wait_for()

        expect(button).to_have_text("Add to Basket")

        nav = Navigation(self.page)
        before = nav.get_basket_counter()

        button.click()
        expect(button).to_have_text("Remove from Basket")

        after = nav.get_basket_counter()
        assert after > before

    def find_products(self, products: List[ProductModel]):
        inner_texts = self.page.locator(self.list_cards).all_inner_texts()

        titles = [p.title for p in products]
        assert titles == inner_texts

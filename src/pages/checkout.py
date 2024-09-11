from playwright.sync_api import Page


class Checkout:
    def __init__(self, page: Page):
        self.page = page

        self.basket_cards = '[data-qa="basket-card"]'
        self.basket_item_price = '[data-qa="basket-item-price"]'
        self.basket_counter = '[data-qa="basket-card-remove-item"]'

    def remove_product(self, product_id):
        pass

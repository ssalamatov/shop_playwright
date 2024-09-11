from playwright.sync_api import Page, expect



class Checkout:
    def __init__(self, page: Page):
        self.page = page

        self.basket_cards = self.page.locator('[data-qa="basket-card"]')
        self.basket_item_price = self.page.locator('[data-qa="basket-item-price"]')
        self.basket_remove_item = self.page.locator('[data-qa="basket-card-remove-item"]')

    def remove_product_from_basket(self, product_id: int):
        self.basket_cards.wait_for()
        before = self.basket_cards.count()

        remove_button = self.basket_remove_item.nth(product_id)
        remove_button.wait_for()
        remove_button.click()

        expect(self.basket_cards).to_have_count(before - 1)

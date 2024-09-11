from playwright.sync_api import Page


class Navigation:

    def __init__(self, page: Page):
        self.page = page
        self.basket_counter = '[data-qa="header-basket-count"]'
        self.checkout_link = self.page.get_by_role("link", name="Checkout")

    def get_basket_counter(self):
        self.page.locator(self.basket_counter).wait_for()
        counter = int(self.page.locator(self.basket_counter).inner_text())
        return counter

    def go_to_checkout(self):
        self.checkout_link.wait_for()
        self.checkout_link.click()
        self.page.wait_for_url("/basket")

from selenium.webdriver.common.by import By

class Catalog:

    def __init__(self, driver):
        self.driver = driver

    def add_item(self):
        item_1 = self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
        item_1.click()

        item_2 = self.driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-bolt-t-shirt']")
        item_2.click()

        item_3 = self.driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-onesie']")
        item_3.click()

        cart = self.driver.find_element(By.CSS_SELECTOR, "[class='shopping_cart_link']")
        cart.click()
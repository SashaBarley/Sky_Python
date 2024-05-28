from selenium.webdriver.common.by import By

class CheckCart:

    def __init__(self, driver):
        self.driver = driver

    def chekout(self):
        cart = self.driver.find_element(By.CSS_SELECTOR, "button[name='checkout']")
        cart.click()
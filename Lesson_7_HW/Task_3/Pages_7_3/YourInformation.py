from selenium.webdriver.common.by import By

class YourInformation:
    def __init__(self, driver):
        self.driver = driver
    

    def login(self):
        first_name = self.driver.find_element(By.CSS_SELECTOR, "[name='firstName']")
        first_name.send_keys("Александр")

        last_name = self.driver.find_element(By.CSS_SELECTOR, "[name='lastName']")
        last_name.send_keys("Ячменев")

        postal_code = self.driver.find_element(By.CSS_SELECTOR, "[name='postalCode'")
        postal_code.send_keys("555555")

        continue_page = self.driver.find_element(By.ID, 'continue')
        continue_page.click()
from selenium.webdriver.common.by import By

class WaitSec:
    
    url = 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def test_calculator(self):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")


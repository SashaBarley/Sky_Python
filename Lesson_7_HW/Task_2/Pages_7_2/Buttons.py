from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Buttons:

    def __init__(self, driver):
        self.driver = driver
    
    def tap_on_buttons(self):
        buttons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "span"))
            )

        for i in ["7", "+", "8", "="]:
            for button in buttons:
                if button.text == i:
                    button.click()
                    break

    def check_results(self):
        result = WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class=screen]"), "15")
            )
        return result
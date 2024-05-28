from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TotalPrice:

    def __init__(self, driver):
        self.driver = driver

    def check_total_price(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[class='summary_total_label']"))
        )
        txt = element.text
        return txt
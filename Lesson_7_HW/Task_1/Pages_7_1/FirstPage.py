from selenium.webdriver.common.by import By

class SecondPage:

    def __init__(self, driver):
        self.driver = driver

    def check_color_red(self):
        zip_code_red = self.driver.find_element(By.CSS_SELECTOR, "#zip-code")
        class_attribute = zip_code_red.get_attribute("class")
        return "alert py-2 alert-danger" in class_attribute

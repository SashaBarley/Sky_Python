from selenium.webdriver.common.by import By

class FirstPage:

    url = 'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
    
    def enter_form(self, data):
        for selector, value in data.items():
            self.driver.find_element(By.CSS_SELECTOR, selector).send_keys(value)

    def click_form(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

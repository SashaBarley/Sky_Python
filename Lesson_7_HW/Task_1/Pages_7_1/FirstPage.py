from selenium.webdriver.common.by import By

class FirstPage:

    url = 'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
    
    def enter_form(self):
        data = {
            '[name=first-name]': 'Иван',
            '[name=last-name]': 'Петров',
            '[name=address]': 'Ленина, 55-3',
            '[name=e-mail]': 'test@skypro.com',
            '[name=phone]': '+7985899998787',
            '[name=zip-code]': '',
            '[name=city]': 'Москва',
            '[name=country]': 'Россия',
            '[name=job-position]': 'QA',
            '[name=company]': 'SkyPro',
        }

        for selector, value in data.items():
            self.driver.find_element(By.CSS_SELECTOR, selector).send_keys(value)
        
        self.driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
        


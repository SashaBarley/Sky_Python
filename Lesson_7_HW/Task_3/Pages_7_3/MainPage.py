from selenium.webdriver.common.by import By

class MainPage:

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.url)
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()
    
    def enter_login(self, user_name, password_in):
        user = self.driver.find_element(By.CSS_SELECTOR, "[id='user-name']")
        user.send_keys(user_name)

        password = self.driver.find_element(By.CSS_SELECTOR, "[name='password']")
        password.send_keys(password_in)
        
        login = self.driver.find_element(By.ID, 'login-button')
        login.click()



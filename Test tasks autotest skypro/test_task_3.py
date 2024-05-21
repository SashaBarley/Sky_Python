import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_shop(driver):
    driver.get("https://www.saucedemo.com/")

    user = driver.find_element(By.CSS_SELECTOR, "[id='user-name']")
    user.send_keys("standard_user")

    password = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    password.send_keys("secret_sauce")
    
    login = driver.find_element(By.ID, 'login-button')
    login.click()

    item_1 = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
    item_1.click()

    item_2 = driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-bolt-t-shirt']")
    item_2.click()

    item_3 = driver.find_element(By.CSS_SELECTOR, "button[id='add-to-cart-sauce-labs-onesie']")
    item_3.click()

    cart = driver.find_element(By.CSS_SELECTOR, "[class='shopping_cart_link']")
    cart.click()

    cart = driver.find_element(By.CSS_SELECTOR, "button[name='checkout']")
    cart.click()

    first_name = driver.find_element(By.CSS_SELECTOR, "[name='firstName']")
    first_name.send_keys("Александр")

    last_name = driver.find_element(By.CSS_SELECTOR, "[name='lastName']")
    last_name.send_keys("Ячменев")

    last_name = driver.find_element(By.CSS_SELECTOR, "[name='postalCode'")
    last_name.send_keys("555555")

    continue_page = driver.find_element(By.ID, 'continue')
    continue_page.click()

    txt = driver.find_element(By.CSS_SELECTOR, "[class='summary_total_label']").text
    print(txt)

    driver.quit()

    assert txt == "Total: $58.29"

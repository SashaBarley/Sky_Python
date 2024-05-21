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

def test_calculator(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#delay"))
    )
    delay_input.clear()
    delay_input.send_keys("45")

    buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "span"))
    )

    for i in ["7", "+", "8", "="]:
        for button in buttons:
            if button.text == i:
                button.click()
                break
            

    result = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[class=screen]"), "15")
    )

    assert result

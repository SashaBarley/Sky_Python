import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_color(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.CSS_SELECTOR, "[name=first-name]").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "[name=last-name]").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "[name=address]").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "[name=e-mail]").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "[name=phone]").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "[name=city]").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "[name=country]").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "[name=job-position]").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "[name=company]").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
    WebDriverWait(driver, 40, 0.1)

    zip_code_red = driver.find_element(By.CSS_SELECTOR, "#zip-code")
    assert "alert py-2 alert-danger" in zip_code_red.get_attribute("class")

    other_green = driver.find_elements(By.CSS_SELECTOR, "[class='alert py-2 alert-success']")
    assert len(other_green) == 9

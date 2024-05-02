from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://uitestingplayground.com/dynamicid")

sleep(5)

blue_b = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary[type='button']")
blue_b.click()

sleep(5)
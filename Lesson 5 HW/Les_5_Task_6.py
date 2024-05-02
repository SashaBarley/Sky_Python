from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(5)

modal_b = driver.find_element(By.CSS_SELECTOR, "div.modal-footer")
modal_b.click()



sleep(5)

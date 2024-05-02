from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(5)

search_input = driver.find_element(By.XPATH, "//input[@type='number']")

search_input.send_keys("1000")
sleep(5)
search_input.clear()
sleep(5)
search_input.send_keys("999")

sleep(5)
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")
sleep(5)

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
button = driver.find_element(By.CSS_SELECTOR, "button.radius[type='submit'] > i.fa.fa-2x.fa-sign-in")

username.send_keys("tomsmith")
sleep(5)
password.send_keys("SuperSecretPassword")
sleep(5)
button.click()

sleep(5)
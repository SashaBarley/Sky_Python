from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

sleep(10)

for i in range(5):
    add_b = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
    add_b.click()

sleep(10)

delete_b = driver.find_elements(By.CSS_SELECTOR, "#elements button")

print("Размер списка кнопок 'Delete': ", len(delete_b))

sleep(10)
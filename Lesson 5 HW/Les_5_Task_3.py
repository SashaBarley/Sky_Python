from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


edge = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

chrome = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

def task_3(driver):
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
    sleep(3)
    
    for i in range(5):
        add_b = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
        add_b.click()
    
    sleep(3)
    delete_b = driver.find_elements(By.CSS_SELECTOR, "#elements button")
    print("Размер списка кнопок 'Delete': ", len(delete_b))
    sleep(3)

task_3(ff)
task_3(edge)
task_3(chrome)
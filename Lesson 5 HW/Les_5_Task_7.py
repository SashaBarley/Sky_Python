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

def task_7(driver):
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

task_7(ff)
task_7(edge)
task_7(chrome)
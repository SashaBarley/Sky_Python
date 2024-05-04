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

def task_4(driver):
    driver.maximize_window()
    driver.get("http://uitestingplayground.com/dynamicid")
    sleep(3)
    blue_b = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")
    blue_b.click()
    sleep(3)

task_4(ff)
task_4(edge)
task_4(chrome)
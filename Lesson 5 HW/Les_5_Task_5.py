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

def task_5(driver):
    driver.maximize_window()
    driver.get("http://uitestingplayground.com/classattr")
    sleep(3)
    blue_b = driver.find_element(By.CSS_SELECTOR, ".btn-primary[type='button']")
    blue_b.click(3)
    sleep(3)

task_5(ff)
task_5(edge)
task_5(chrome)
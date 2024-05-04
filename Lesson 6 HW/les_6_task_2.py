from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

browser.implicitly_wait(20)
browser.get("http://uitestingplayground.com/textinput")

text = browser.find_element(By.ID, "newButtonName")
text.clear()  
text.send_keys("SkyPro")

browser.find_element(By.ID, "updatingButton").click()

txt = browser.find_element(By.ID, "updatingButton").text
print(txt)

browser.quit()


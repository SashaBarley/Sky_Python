from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 

browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

browser.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')


wait = WebDriverWait(browser, 10)
wait.until(lambda all_picture: len(all_picture.find_elements(By.TAG_NAME, 'img')) == 4)

picture_3 = browser.find_element(By.ID, "award")
src_value = picture_3.get_attribute("src")

print(src_value)

browser.quit()


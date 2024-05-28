from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 

from Lesson_7_HW.Task_1.Pages_7_1.FirstPage import FirstPage
from Lesson_7_HW.Task_1.Pages_7_1.SecondPage import SecondPage

def test_zip_code_red():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    first_page = FirstPage(driver)
    first_page.enter_form()

    second_page = SecondPage(driver)
    q = second_page.check_color_red()

    driver.quit()

    assert q == True
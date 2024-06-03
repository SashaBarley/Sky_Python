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

    form_data = {
        '[name=first-name]': 'Иван',
        '[name=last-name]': 'Петров',
        '[name=address]': 'Ленина, 55-3',
        '[name=e-mail]': 'test@skypro.com',
        '[name=phone]': '+7985899998787',
        '[name=zip-code]': '',  # Здесь оставляем пустым для проверки
        '[name=city]': 'Москва',
        '[name=country]': 'Россия',
        '[name=job-position]': 'QA',
        '[name=company]': 'SkyPro',
    }

    first_page.enter_form(form_data)
    first_page.click_form()

    second_page = SecondPage(driver)
    q = second_page.check_color_red()

    driver.quit()

    assert q == True

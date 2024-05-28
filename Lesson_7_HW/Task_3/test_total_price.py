from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 

from Pages_7_3.MainPage import MainPage
from Pages_7_3.Catalog import Catalog
from Pages_7_3.CheckCart import CheckCart
from Pages_7_3.YourInformation import YourInformation
from Pages_7_3.TotalPrice import TotalPrice

def test_total_price():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    main_page = MainPage(driver)
    main_page.enter_login("standard_user", "secret_sauce")

    catalog = Catalog(driver)
    catalog.add_item()

    check_cart = CheckCart(driver)
    check_cart.chekout()

    login = YourInformation(driver)
    login.login()

    total_price = TotalPrice(driver)
    q = total_price.check_total_price()
    
    assert q == "Total: $58.29"

    driver.quit()



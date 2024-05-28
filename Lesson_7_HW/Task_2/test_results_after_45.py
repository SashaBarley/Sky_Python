from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 

from Pages_7_2.WaitSec import WaitSec
from Pages_7_2.Buttons import Buttons

def test_results_after_45():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    wait_sec = WaitSec(driver)
    wait_sec.test_calculator()

    buttons = Buttons(driver)
    buttons.tap_on_buttons()
    q = buttons.check_results()

    assert q == True






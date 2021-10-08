from selenium.webdriver import ActionChains

from Locators.Locators import Locators, WPlan_LogoutPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import datetime


class WPlanMainMenu:
    def __init__(self, driver):
        self.driver = driver
        self.W = Locators

    def select_main_menu_workers(self):
        self.driver.find_element_by_link_text(Locators.WPlan_Workers).click()
        time.sleep(2)

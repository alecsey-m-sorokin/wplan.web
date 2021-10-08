from selenium.webdriver import ActionChains

from Locators.Locators import Locators, WPlan_WorkerPage, WPlan_LogoutPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import datetime


class WPlanWorkersMenu:
    def __init__(self, driver):
        self.driver = driver
        self.W = WPlan_WorkerPage

    def press_add_new_worker_button(self):
        self.driver.find_element_by_xpath(WPlan_WorkerPage.WPlan_Add_Worker).click()
        time.sleep(1)



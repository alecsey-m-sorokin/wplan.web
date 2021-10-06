from selenium.webdriver import ActionChains

from Locators.Locators import WPlanLoginPage, WPlan_LogoutPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import datetime


class WPlanLogin:
    def __init__(self, driver):
        self.driver = driver
        self.google_icon = ''

    def enter_login(self, login):
        self.driver.find_element_by_xpath(WPlanLoginPage.WPlan_LOGIN).clear()
        self.driver.find_element_by_xpath(WPlanLoginPage.WPlan_LOGIN).send_keys(login)
        time.sleep(1)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(WPlanLoginPage.WPlan_PASS).clear()
        self.driver.find_element_by_xpath(WPlanLoginPage.WPlan_PASS).send_keys(password)
        time.sleep(1)

    def press_ad_check_button(self):
        self.driver.find_element_by_xpath(WPlanLoginPage.WPlan_AD).click()
        time.sleep(2)

    def press_enter_button(self):
        self.driver.find_element_by_xpath(WPlanLoginPage.WPlan_ENTER_button).click()
        time.sleep(2)

    def press_reddy_id_cancel_button(self):
        self.driver.find_element_by_xpath(WPlanLoginPage.WPlan_Reddy_ID_cancel_button).click()
        time.sleep(2)

    def press_wplan_top_exit_button(self):
        self.driver.find_element_by_xpath(WPlan_LogoutPage.WPlan_top_exit).click()
        time.sleep(2)

    def press_wplan_logout_button(self):
        self.driver.find_element_by_xpath(WPlan_LogoutPage.WPlan_logout).click()
        time.sleep(2)

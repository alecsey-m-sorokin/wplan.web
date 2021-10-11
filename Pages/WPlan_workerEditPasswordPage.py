from selenium.webdriver import ActionChains

from Locators.Locators import WPlan_WorkerEditPasswordPage, WPlan_LogoutPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import datetime


class WPlanWorkerEditPassword:
    def __init__(self, driver):
        self.driver = driver
        self.W = WPlan_WorkerEditPasswordPage

    def press_edit_password_button(self):
        self.driver.find_element_by_xpath(WPlan_WorkerEditPasswordPage.Edit_Password_button).click()
        time.sleep(1)

    def enter_new_password(self, password):
        self.driver.find_element_by_xpath(WPlan_WorkerEditPasswordPage.New_Password).clear()
        self.driver.find_element_by_xpath(WPlan_WorkerEditPasswordPage.New_Password).send_keys(password)
        time.sleep(1)

    def confirm_new_password(self, password):
        self.driver.find_element_by_xpath(WPlan_WorkerEditPasswordPage.Confirm_Password).clear()
        self.driver.find_element_by_xpath(WPlan_WorkerEditPasswordPage.Confirm_Password).send_keys(password)
        time.sleep(1)

    def press_edit_password_cancel_button(self):
        self.driver.find_element_by_xpath(WPlan_WorkerEditPasswordPage.Cancel_Edit_Password_button).click()
        time.sleep(1)

    def press_edit_password_submit_button(self):
        self.driver.find_element_by_css_selector('.ant-modal-wrap:nth-child(2) > .ant-modal > .ant-modal-content > .ant-modal-footer > .ant-btn-primary > span').click()
        time.sleep(1)

    # def press_edit_password_submit_button(self):
    #     self.driver.find_element_by_xpath(WPlan_WorkerEditPasswordPage.Submit_Edit_Password_button).click()
    #     time.sleep(1)

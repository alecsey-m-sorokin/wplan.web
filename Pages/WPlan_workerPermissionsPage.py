from selenium.webdriver import ActionChains

from Locators.Locators import WPlan_WorkerPermissionsPage, WPlan_LogoutPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import datetime


class WPlanWorkerPermissions:
    def __init__(self, driver):
        self.driver = driver
        self.W = WPlan_WorkerPermissionsPage

    def select_worker_permissions_all_offices_groups(self):
        self.driver.find_element_by_xpath(WPlan_WorkerPermissionsPage.Add_Worker_All_Offices_Groups0).click()
        time.sleep(1)

    def press_worker_permissions_submit_button(self):
        # ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_Registration_Submit_button)).click().perform()
        self.driver.find_element_by_xpath(WPlan_WorkerPermissionsPage.Worker_Permissions_Submit_button).click()
        time.sleep(1)


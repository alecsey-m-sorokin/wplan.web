from selenium.webdriver import ActionChains

from Locators.Locators import WPlan_WorkerRegistrationPage, WPlan_LogoutPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import datetime


class WPlanWorkerRegistration:
    def __init__(self, driver):
        self.driver = driver
        self.W = WPlan_WorkerRegistrationPage

    def select_login_type(self):
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.AD_switch_button0).click()
        time.sleep(1)

    def enter_login(self, login):
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Login).clear()
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Login).send_keys(login)
        time.sleep(1)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Password).clear()
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Password).send_keys(password)
        time.sleep(1)

    def enter_timex_id(self, timexId):
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Timex_Id).clear()
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Timex_Id).send_keys(timexId)
        time.sleep(1)

    def enter_date(self, date):
        """
            # driver.find_element_by_id('dff618ee3ff92d1fa9984129d7e2449b').send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
            # ActionChains(driver).move_to_element(driver.find_element_by_id('dff618ee3ff92d1fa9984129d7e2449b')).click().key_down(Keys.CONTROL).send_keys("a").send_keys(Keys.DELETE).perform()
        """
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Select_Date).click()
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Select_Date).send_keys(Keys.END)
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Select_Date).send_keys('\b\b\b\b\b\b\b\b\b\b')
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Select_Date).send_keys(date)
        # self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Select_Date).send_keys(Keys.ENTER)
        self.driver.find_element_by_css_selector(".ant-form").submit()

        time.sleep(1)

    def enter_worker_name(self, name):
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Name).clear()
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Name).send_keys(name)
        time.sleep(1)

    def enter_worker_family(self, family):
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Family).clear()
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Family).send_keys(family)
        time.sleep(1)

    def enter_worker_midname(self, midname):
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_MidName).clear()
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_MidName).send_keys(midname)
        time.sleep(1)

    def enter_worker_reddy_id(self, reddyid):
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Reddy_Id).clear()
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Reddy_Id).send_keys(reddyid)
        time.sleep(1)

    def enter_worker_office(self, office):
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Office).clear()
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Office).send_keys(office)
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Office_BY1).click()
        time.sleep(1)

    def enter_worker_role(self, role):
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Role).clear()
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Role).send_keys(role)
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Role_Root).click()
        time.sleep(1)

    def enter_worker_group_id(self, groupid):
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Group_Id).clear()
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Group_Id).send_keys(groupid)
        time.sleep(1)

    def enter_worker_schedule(self, schedule):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Schedule)).click().perform()
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Schedule_1).click()
        time.sleep(1)

    def press_worker_submit_button(self):
        # ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_Registration_Submit_button)).click().perform()
        self.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_Registration_Submit_button).click()
        time.sleep(1)



# ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(REGISTRATIONPage.IURU_input_field_phone)).click().key_down(Keys.CONTROL).send_keys("a").send_keys(Keys.DELETE).send_keys(phone).perform()
# self.driver.find_element_by_xpath(REGISTRATIONPage.IURU_input_field_phone).send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)

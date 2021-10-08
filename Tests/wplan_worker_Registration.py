from datetime import datetime
import time
import unittest
import pytest
from selenium import webdriver
from russian_names import RussianNames
import mimesis
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

import global_functions
from Locators.Locators import WPlan_WorkerRegistrationPage

from Pages.WPlan_loginPage import WPlanLogin
from conftest import FIREFOX_PATH_64
from conftest import StandSettings
from Pages.WPlan_workerRegistrationPage import WPlanWorkerRegistration
from Pages.WPlan_mainPage import WPlanMainMenu
from Pages.WPlan_workerPage import WPlanWorkersMenu


@pytest.fixture(scope='class')
def go_to_wplan_page(driver, request):
    driver = request.cls.driver
    driver.get("https://wplan.zhdun.space/")

@pytest.fixture(scope='class')
def go_to_worker_page(go_to_wplan_page, request):
    driver = request.cls.driver
    wPlanLogin = WPlanLogin(driver)
    wPlanLogin.enter_login(StandSettings.root_reddy_user)
    wPlanLogin.enter_password(StandSettings.root_reddy_user_password)
    wPlanLogin.press_ad_check_button()
    wPlanLogin.press_enter_button()
    wPlanLogin.press_reddy_id_cancel_button()

    wPlanWorker = WPlanMainMenu(driver)
    wPlanWorker.select_main_menu_workers()


@pytest.fixture(scope='function')
def register_new_worker(request):
    driver = request.cls.driver
    RN = RussianNames(count=1, output_type='list', transliterate=False).get_batch()
    login = global_functions.random_string(8)
    password = global_functions.user_password(1, 8)
    timexId = global_functions.random_number(6)
    workDay = datetime.today().strftime("%d.%m.%Y")

    todays_date = datetime.today().strftime("%Y-%m-%d %H-%M-%S")
    wPlanWorkerRegistration = WPlanWorkerRegistration(driver)
    wPlanAddNewWorker = WPlanWorkersMenu(driver)
    wPlanAddNewWorker.press_add_new_worker_button()

    wPlanWorkerRegistration.enter_worker_reddy_id('6645311')
    # ActionChains(wPlanWorkerRegistration.driver).move_to_element(wPlanWorkerRegistration.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Schedule)).click().send_keys("Нед Без Вых 8").perform()
    ActionChains(wPlanWorkerRegistration.driver).move_to_element(wPlanWorkerRegistration.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Schedule)).click().perform()
    # wPlanWorkerRegistration.driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Schedule_1).click()
    # sel = '//div[@class="rc-virtual-list"]//div[@class="rc-virtual-list-holder"]//div[@class="rc-virtual-list-holder-inner"]//*'
    sel = '//div[@label="Нед Без вых 8 and @aria-selected="false"]'
    wPlanWorkerRegistration.driver.find_element_by_xpath(sel).click()


    # wPlanWorkerRegistration.select_login_type()
    # wPlanWorkerRegistration.enter_login('justatest')
    # wPlanWorkerRegistration.enter_password('11111111')
    # wPlanWorkerRegistration.enter_timex_id(timexId)
    # # wPlanWorkerRegistration.enter_date('05.10.2021')
    # wPlanWorkerRegistration.enter_worker_name(RN[0][0])
    # wPlanWorkerRegistration.enter_worker_family(RN[0][1])
    # wPlanWorkerRegistration.enter_worker_midname(RN[0][2])
    # wPlanWorkerRegistration.enter_worker_office('BY1')
    # wPlanWorkerRegistration.enter_worker_role('Root')
    # wPlanWorkerRegistration.enter_worker_schedule('Нед Без Вых 8')
    # wPlanWorkerRegistration.press_worker_submit_button()
    time.sleep(3)

@pytest.mark.usefixtures('go_to_worker_page')
class TestWPlanWorkerRegistration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.todays_date = datetime.today().strftime("%Y-%m-%d %H-%M-%S")
        pass

    def setUp(self):
        pass

    def tearDown(self):
        # dt = '{}'.format(datetime.datetime.today().strftime("%d-%m-%Y %H-%M-%S"))
        # shd = 'd:\\iu.python\\IU.RU\\Screenshots' + '\\Error {} {}.png'.format(self.id(), dt)
        # take_screenshots_error(self, shd)
        pass

    @pytest.mark.usefixtures('register_new_worker')
    def test_register_new_worker(self):
        driver = self.driver
        # self.driver.set_window_size(1376, 895)
        time.sleep(1)

# browser = webdriver.Firefox(executable_path=FIREFOX_PATH_64)
# browser.get('https://www.google.com')
# time.sleep(10)
# browser.quit()

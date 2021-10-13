from datetime import datetime
import time
import unittest

from parameterized import parameterized
import pytest
from selenium import webdriver
from russian_names import RussianNames
import mimesis
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import global_functions
from Locators.Locators import WPlan_WorkerRegistrationPage
from conftest import FIREFOX_PATH_64

from Pages.WPlan_loginPage import WPlanLogin
from Pages.WPlan_workerPermissionsPage import WPlanWorkerPermissions
from conftest import StandSettings
from Pages.WPlan_workerEditPasswordPage import WPlanWorkerEditPassword
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
    wPlanLogin.enter_login(StandSettings.lead_reddy_user)
    wPlanLogin.enter_password(StandSettings.lead_reddy_user_password)
    # wPlanLogin.enter_password(StandSettings.lead_reddy_user_password)
    wPlanLogin.press_ad_check_button()
    wPlanLogin.press_enter_button()
    wPlanLogin.press_reddy_id_cancel_button()

    wPlanWorker = WPlanMainMenu(driver)
    wPlanWorker.select_main_menu_workers()

    wPlanEditWorkerPassword = WPlanWorkerEditPassword(driver)
    wPlanEditWorkerPassword.press_edit_password_button()


@pytest.fixture(scope='function')
# @parameterized.expand(['gsyw2#Edd', 'gs~w2#Edd'])
def edit_worker_lead_Password(request):
    driver = request.cls.driver
    RN = RussianNames(count=1, output_type='list', transliterate=False).get_batch()
    login = global_functions.random_string(10)
    password = global_functions.user_password(1, 20)
    timexId = global_functions.random_number(7)
    workDate = datetime.today().strftime("%d.%m.%Y")

    wPlanEditWorkerPassword = WPlanWorkerEditPassword(driver)
    # wPlanEditWorkerPassword.press_edit_password_button()
    wPlanEditWorkerPassword.enter_new_password(password=password)
    wPlanEditWorkerPassword.confirm_new_password(password=password)
    wPlanEditWorkerPassword.press_edit_password_submit_button()
    time.sleep(3)

@pytest.mark.usefixtures('go_to_worker_page')
class TestWPlanWorkerEditPassword(unittest.TestCase):

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

    @pytest.mark.usefixtures('edit_worker_lead_Password')
    def test_01_edit_worker_password(self):
        driver = self.driver
        # self.driver.set_window_size(1376, 895)
        time.sleep(2)

    @parameterized.expand([
        'gsyw2#Edd',
        'gs~w2#Edd'
    ])
    def test_02_edit_worker_password(self, password):
        driver = self.driver

        # password = global_functions.user_password(1, 20)
        wPlanEditWorkerPassword = WPlanWorkerEditPassword(driver)
        # wPlanEditWorkerPassword.press_edit_password_button()
        wPlanEditWorkerPassword.enter_new_password(password=password)
        wPlanEditWorkerPassword.confirm_new_password(password=password)
        wPlanEditWorkerPassword.press_edit_password_submit_button()
        time.sleep(3)

        # self.driver.set_window_size(1376, 895)
        # time.sleep(2)

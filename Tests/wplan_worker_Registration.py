from datetime import datetime
import time
import unittest
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
from Locators.Locators import WPlan_WorkerRegistrationPage, WPlanLoginPage
from conftest import FIREFOX_PATH_64

from Pages.WPlan_loginPage import WPlanLogin
from Pages.WPlan_workerPermissionsPage import WPlanWorkerPermissions
from conftest import StandSettings
from Pages.WPlan_workerRegistrationPage import WPlanWorkerRegistration
from Pages.WPlan_mainPage import WPlanMainMenu
from Pages.WPlan_workerPage import WPlanWorkersMenu


@pytest.fixture(scope='class')
def go_to_wplan_page(driver, request):
    driver = request.cls.driver
    driver.get("https://wplan.zhdun.space/")

@pytest.fixture(scope='class')
def go_to_wplan_login_page(go_to_wplan_page, request):
    driver = request.cls.driver
    wPlanLogin = WPlanLogin(driver)
    wPlanLogin.enter_login(StandSettings.root_reddy_user)
    wPlanLogin.enter_password(StandSettings.root_reddy_user_password)
    wPlanLogin.press_ad_check_button()
    wPlanLogin.press_enter_button()
    if wPlanLogin.check_exists_by_xpath(xpath=WPlanLoginPage.WPlan_Reddy_ID_cancel_button):
        wPlanLogin.press_reddy_id_cancel_button()
    else:
        pass

@pytest.fixture(scope='class')
def go_to_worker_page(go_to_wplan_login_page, request):
    driver = request.cls.driver
    wPlanWorker = WPlanMainMenu(driver)
    wPlanWorker.select_main_menu_workers()


@pytest.fixture(scope='function')
def register_new_worker_root(request):
    driver = request.cls.driver
    RN = RussianNames(count=1, output_type='list', transliterate=False).get_batch()
    login = global_functions.random_string(10)
    password = global_functions.user_password(1, 20)
    timexId = global_functions.random_number(7)
    workDate = datetime.today().strftime("%d.%m.%Y")

    wPlanWorkerRegistration = WPlanWorkerRegistration(driver)
    wPlanAddNewWorker = WPlanWorkersMenu(driver)
    wPlanAddNewWorker.press_add_new_worker_button()
    wPlanWorkerRegistration.select_login_type()
    wPlanWorkerRegistration.enter_login(login=login)
    wPlanWorkerRegistration.enter_password(password=password)
    wPlanWorkerRegistration.enter_timex_id(timexId=timexId)
    wPlanWorkerRegistration.enter_date(workDate=workDate)
    wPlanWorkerRegistration.enter_worker_name(name=RN[0][0])
    wPlanWorkerRegistration.enter_worker_family(family=RN[0][1])
    wPlanWorkerRegistration.enter_worker_midname(midname=RN[0][2])
    wPlanWorkerRegistration.enter_worker_office(office='BY1')
    wPlanWorkerRegistration.enter_worker_role_root(role='Root')
    wPlanWorkerRegistration.enter_worker_schedule(schedule='')
    # driver.find_element_by_xpath(u'(.//*[normalize-space(text()) and normalize-space(.)="Отмена"])[2]/following::span[1]').click()
    wPlanWorkerRegistration.press_worker_submit_button()
    time.sleep(3)

@pytest.fixture(scope='function')
def register_new_worker_manager(request):
    driver = request.cls.driver
    RN = RussianNames(count=1, output_type='list', transliterate=False).get_batch()
    login = global_functions.random_string(10)
    password = global_functions.user_password(1, 20)
    timexId = global_functions.random_number(7)
    workDate = datetime.today().strftime("%d.%m.%Y")

    wPlanWorkerRegistration = WPlanWorkerRegistration(driver)
    wPlanAddNewWorker = WPlanWorkersMenu(driver)
    wPlanAddNewWorker.press_add_new_worker_button()
    wPlanWorkerRegistration.select_login_type()
    wPlanWorkerRegistration.enter_login(login=login)
    wPlanWorkerRegistration.enter_password(password=password)
    wPlanWorkerRegistration.enter_timex_id(timexId=timexId)
    wPlanWorkerRegistration.enter_date(workDate=workDate)
    wPlanWorkerRegistration.enter_worker_name(name=RN[0][0])
    wPlanWorkerRegistration.enter_worker_family(family=RN[0][1])
    wPlanWorkerRegistration.enter_worker_midname(midname=RN[0][2])
    wPlanWorkerRegistration.enter_worker_office(office='BY1')
    wPlanWorkerRegistration.enter_worker_role_manager(role='Менеджер')
    wPlanWorkerRegistration.enter_worker_schedule(schedule='')
    # driver.find_element_by_xpath(u'(.//*[normalize-space(text()) and normalize-space(.)="Отмена"])[2]/following::span[1]').click()
    wPlanWorkerRegistration.press_worker_submit_button()
    time.sleep(3)
    wPlanWorkerPermissions = WPlanWorkerPermissions(driver)
    # driver.find_element_by_xpath('//*[@id="753cd56cf78d66147b1cf76c30226c4f"]').click()
    wPlanWorkerPermissions.select_worker_permissions_all_offices_groups()
    time.sleep(2)
    wPlanWorkerPermissions.press_worker_permissions_submit_button()
    time.sleep(3)

@pytest.fixture(scope='function')
def register_new_worker_lead(request):
    driver = request.cls.driver
    RN = RussianNames(count=1, output_type='list', transliterate=False).get_batch()
    login = global_functions.random_string(10)
    password = global_functions.user_password(1, 20)
    timexId = global_functions.random_number(7)
    workDate = datetime.today().strftime("%d.%m.%Y")

    wPlanWorkerRegistration = WPlanWorkerRegistration(driver)
    wPlanAddNewWorker = WPlanWorkersMenu(driver)
    wPlanAddNewWorker.press_add_new_worker_button()
    wPlanWorkerRegistration.select_login_type()
    wPlanWorkerRegistration.enter_login(login=login)
    wPlanWorkerRegistration.enter_password(password=password)
    wPlanWorkerRegistration.enter_timex_id(timexId=timexId)
    wPlanWorkerRegistration.enter_date(workDate=workDate)
    wPlanWorkerRegistration.enter_worker_name(name=RN[0][0])
    wPlanWorkerRegistration.enter_worker_family(family=RN[0][1])
    wPlanWorkerRegistration.enter_worker_midname(midname=RN[0][2])
    wPlanWorkerRegistration.enter_worker_office(office='BY1')
    wPlanWorkerRegistration.enter_worker_role_lead(role='Руководитель')
    wPlanWorkerRegistration.enter_worker_schedule(schedule='')
    wPlanWorkerRegistration.press_worker_submit_button()
    time.sleep(3)

@pytest.fixture(scope='function')
def register_new_worker_executor(request):
    driver = request.cls.driver
    RN = RussianNames(count=1, output_type='list', transliterate=False).get_batch()
    login = global_functions.random_string(10)
    password = global_functions.user_password(1, 20)
    timexId = global_functions.random_number(7)
    workDate = datetime.today().strftime("%d.%m.%Y")

    wPlanWorkerRegistration = WPlanWorkerRegistration(driver)
    wPlanAddNewWorker = WPlanWorkersMenu(driver)
    wPlanAddNewWorker.press_add_new_worker_button()
    wPlanWorkerRegistration.select_login_type()
    wPlanWorkerRegistration.enter_login(login=login)
    wPlanWorkerRegistration.enter_password(password=password)
    wPlanWorkerRegistration.enter_timex_id(timexId=timexId)
    wPlanWorkerRegistration.enter_date(workDate=workDate)
    wPlanWorkerRegistration.enter_worker_name(name=RN[0][0])
    wPlanWorkerRegistration.enter_worker_family(family=RN[0][1])
    wPlanWorkerRegistration.enter_worker_midname(midname=RN[0][2])
    wPlanWorkerRegistration.enter_worker_office(office='BY1')
    wPlanWorkerRegistration.enter_worker_role_executor(role='Исполнитель')
    wPlanWorkerRegistration.enter_worker_schedule(schedule='')
    # driver.find_element_by_xpath('//button[@type="button" and contains(span, "Добавить сотрудника")]').click()
    wPlanWorkerRegistration.press_worker_submit_button()
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

    @pytest.mark.usefixtures('register_new_worker_root')
    def test_01_register_new_worker_root(self):
        driver = self.driver
        # self.driver.set_window_size(1376, 895)
        time.sleep(2)

    @pytest.mark.usefixtures('register_new_worker_manager')
    def test_02_register_new_worker_manager(self):
        driver = self.driver
        # self.driver.set_window_size(1376, 895)
        time.sleep(2)

    @pytest.mark.usefixtures('register_new_worker_lead')
    def test_03_register_new_worker_lead(self):
        driver = self.driver
        # self.driver.set_window_size(1376, 895)
        time.sleep(2)

    @pytest.mark.usefixtures('register_new_worker_executor')
    def test_04_register_new_worker_executor(self):
        driver = self.driver
        # self.driver.set_window_size(1376, 895)
        time.sleep(2)

    # @pytest.mark.usefixtures('register_new_worker_executor')
    def test_05_register_new_worker(self):
        driver = self.driver
        RN = RussianNames(count=1, output_type='list', transliterate=False).get_batch()
        login = global_functions.random_string(10)
        password = global_functions.user_password(1, 20)
        timexId = global_functions.random_number(7)
        workDate = datetime.today().strftime("%d.%m.%Y")

        wPlanWorkerRegistration = WPlanWorkerRegistration(driver)
        wPlanAddNewWorker = WPlanWorkersMenu(driver)
        wPlanAddNewWorker.press_add_new_worker_button()
        wPlanWorkerRegistration.select_login_type()
        wPlanWorkerRegistration.enter_login(login=login)
        wPlanWorkerRegistration.enter_password(password=password)
        wPlanWorkerRegistration.enter_timex_id(timexId=timexId)
        wPlanWorkerRegistration.enter_date(workDate=workDate)
        wPlanWorkerRegistration.enter_worker_name(name=RN[0][0])
        wPlanWorkerRegistration.enter_worker_family(family=RN[0][1])
        wPlanWorkerRegistration.enter_worker_midname(midname=RN[0][2])
        wPlanWorkerRegistration.enter_worker_office(office='BY1')
        wPlanWorkerRegistration.enter_worker_role_root(role='Root')
        wPlanWorkerRegistration.enter_worker_schedule(schedule='')

        driver.find_element_by_xpath(u'(.//*[normalize-space(text()) and normalize-space(.)="Отмена"])[2]/following::span[1]').click()

        # wPlanWorkerRegistration.press_worker_submit_button()
        time.sleep(3)



# browser = webdriver.Firefox(executable_path=FIREFOX_PATH_64)
# browser.get('https://www.google.com')
# time.sleep(10)
# browser.quit()

# ActionChains(driver).move_to_element(driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Schedule)).click().perform()
# driver.find_element_by_xpath(WPlan_WorkerRegistrationPage.Worker_WPlan_Schedule_1).click()

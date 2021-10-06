import datetime
import time
import unittest
import pytest
from selenium import webdriver
from conftest import FIREFOX_PATH_64
from Pages.WPlan_loginPage import LOGIN


@pytest.fixture(scope='class')
def go_to_wplan_page(driver, request):
    driver = request.cls.driver
    driver.get("https://wplan.zhdun.space/")


@pytest.mark.usefixtures('go_to_wplan_page')
class TestPython(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.todays_date = datetime.datetime.today().strftime("%Y-%m-%d %H-%M-%S")
        pass

    def setUp(self):
        pass

    def tearDown(self):
        # dt = '{}'.format(datetime.datetime.today().strftime("%d-%m-%Y %H-%M-%S"))
        # shd = 'd:\\iu.python\\IU.RU\\Screenshots' + '\\Error {} {}.png'.format(self.id(), dt)
        # take_screenshots_error(self, shd)
        pass

    def test_wplan_login(self):
        driver = self.driver
        LG = LOGIN(driver)
        # self.driver.set_window_size(1376, 895)
        LG.enter_login('test_reddy_root')
        LG.enter_password('11111111')
        LG.press_ad_check_button()
        LG.press_enter_button()
        LG.press_reddy_id_cancel_button()
        LG.press_wplan_top_exit_button()
        LG.press_wplan_logout_button()
        time.sleep(2)

# browser = webdriver.Firefox(executable_path=FIREFOX_PATH_64)
# browser.get('https://www.google.com')
# time.sleep(10)
# browser.quit()

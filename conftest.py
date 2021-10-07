"""
This module contains shared fixtures for web UI tests.
"""
import datetime
import json
import pytest
import os

from selenium.webdriver import Chrome, Firefox, FirefoxProfile

# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# CONFIG_PATH = os.path.join(ROOT_DIR, 'config.json')
CONFIG_PATH = 'C://Python//wplan//wplan.web//config.json'
CHROME_PATH = 'E://Python//wplan//wplan.web//drivers//chromedriver.exe'
FIREFOX_PATH_32 = '/drivers/geckodriver32.exe'
FIREFOX_PATH_64 = '/drivers/geckodriver64.exe'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']

class StandSettings:
    test_stand = 'https://wplan.zhdun.space/'
    prod_stand = 'https://front-test.kube-main.iu.ru/'
    usable_stand = test_stand
    # test_reddy_root = "https://test_reddy_root:11111111@{}".format(test_stand)
    root_reddy_user = 'test_reddy_root'
    manager_reddy_user = 'test_reddy_manager'
    lead_reddy_user = 'test_reddy_lead'
    executor_reddy_user = 'test_reddy_lead'
    root_reddy_user_password = '11111111'
    manager_reddy_user_password = '11111111'
    lead_reddy_user_password = '11111111'
    executor_reddy_user_password = '11111111'
    WPlan_test_group = 'WPlan_test_group'


@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data

@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']

@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME

@pytest.fixture(scope='session')
def browser_path(config):
    # Validate and return the browser path from the config data
    chrome_driver_path = config['chrome_driver_path']
    ff_driver_path = config['ff_driver_path']

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="my option: chrome or ff")

@pytest.fixture(scope='class')
def driver(request, config_wait_time, browser_path):
    browser = request.config.getoption("--browser")
    # Initialize WebDriver
    if browser == 'chrome':
        driver = Chrome("/python/wplan/wplan.web/drivers/chromedriver.exe")
    elif browser == 'firefox':
        fp = FirefoxProfile()
        fp.set_preference("network.negotiate-auth.trusted-uris", StandSettings.usable_stand)
        driver = Firefox(fp, executable_path="/python/wplan/wplan.web//drivers/geckodriverpython.exe")
    else:
        raise Exception(f'"{browser}" is not a supported browser')
    request.cls.driver = driver
    driver.maximize_window()
    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)
    yield
    driver.quit()

@pytest.fixture(scope='function')
def second_driver(request, config_wait_time):
    browser = request.config.getoption("--browser")
    # Initialize WebDriver
    if browser == 'chrome':
        second_driver = Chrome("/python/wplan/drivers/chromedriver.exe")
    elif browser == 'firefox':
        fp = FirefoxProfile()
        fp.set_preference("network.negotiate-auth.trusted-uris", StandSettings.usable_stand)
        second_driver = Firefox(fp, executable_path="/python/wplan/drivers/geckodriverpython.exe")
    else:
        raise Exception(f'"{browser}" is not a supported browser')
    request.cls.second_driver = second_driver
    second_driver.maximize_window()
    # Wait implicitly for elements to be ready before attempting interactions
    second_driver.implicitly_wait(config_wait_time)
    yield
    second_driver.quit()

    # # Return the driver object at the end of setup
    # yield request.instance.driver
    #
    # # For cleanup, quit the driver
    # request.instance.driver.quit()

def take_screenshots_error(self, savelocation):
    dt = '{}'.format(datetime.datetime.today().strftime("%d-%m-%Y %H-%M-%S"))
    # shd = 'D:\\ASD\\PY test\\example\\Assobo\\Screenshots' + '\\Error {} {}.png'.format(self.id(), dt)
    for method, error in self._outcome.errors:
        if error:
            shd = savelocation
            self.driver.save_screenshot(shd)
            #  self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Screenshots', 'Error {} {}.png'.format(self.id(), dt)))
            print('Check Error {} {}.png'.format(self.id(), dt))

def write_user_data_to_disk(F, N, MN, C, EM, P, P2):
    """ Функция записывает массив user_data в файл
    """
    dt = '{}'.format(datetime.datetime.today().strftime("%d-%m-%Y %H-%M-%S"))
    file = open('d:\\iu.python\\IU.RU\\userdata' + '\\User {}.txt'.format(dt), 'a')  # открываем куда писать полученные данные
    user_data = "\n" + F + "\n" + N + "\n" + MN + "\n" + C + "\n" + EM + "\n" + P + "\n" + P2
    file.write(user_data)  # записываем в файл данные созданного пользователя
    file.close()  # закрываем файл


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
        self.errorXpath = '//div[@role="alert"]'  # selector, по которому получаем статусы всех ошибок при смене пароля
        self.ERR = []  # список, куда помещаем статусы ошибок при смене пароля
        self.errorSummary = ['Слабый пароль. Пароль должен содержать только латинские буквы, минимум одну цифру, букву верхнего и букву нижнего регистра',
                             'Не менее 6 символов',
                             'Не совпадает с паролем',
                             'Поле должно быть заполнено'
                             ]

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
        self.driver.find_element_by_css_selector(WPlan_WorkerEditPasswordPage.Submit_Edit_Password_button).click()
        time.sleep(1)

    # def press_edit_password_submit_button(self):
    #     # self.driver.find_element_by_xpath('//button[@ant-click-animating-without-extra-node="false"]//span[contains(text(),"Подтвердить")]').click()
    #     time.sleep(1)

    def compare_edit_password_errors(self):
        errors = self.driver.find_elements_by_xpath(self.errorXpath)
        for elem in errors:
            self.ERR.append(elem.text)  # помещаем в список все сообщения об ошибках при смене пароля
            # print(elem.text)
        for elem in errors:
            if elem.text in self.errorSummary:  # проверяем, что элемент в списке errorSummary
                print(f'alert message = {elem.text}')
                pass
            else:
                raise AssertionError('element status error. element value = ',
                                     elem.text)  # вываливаемся с ошибкой, если статус ERROR не в списке ошибок при смене пароля
        return self.ERR

import time


class Locators():
    """ MAIN PAGE """
    Project_mainPage = ''

class LOGINPage(Locators):
    def __init__(self, driver):
        self.driver = driver

    """ LOGIN """
    WPlan_ENTER_button = '//*[@type="submit"]'
    WPlan_LOGIN = '//*[@id="bf9050319489c6fa7191ee2ff8c66653"]'
    WPlan_PASS = '//*[@id="ebe42bdec5691c9ceded1258280a0a06"]'
    WPlan_AD = '//*[@id="2bfc2c7b37a7416a733ff2dd653df9c0"]'
    WPlan_Reddy_ID = '//*[@name="reddyId"]'
    WPlan_Reddy_ID_cancel_button = '//*[@class="ant-btn"]'
    WPlan_Reddy_ID_submit_button = '//*[@class="ant-btn ant-btn-primary"]'

class LOGOUTPage(Locators):
    def __init__(self, driver):
        self.driver = driver

    """ LOGOUT """
    Project_logout_button = 'Logout'
    WPlan_top_exit = '//*[@class="ant-btn ant-dropdown-trigger StyledRightMenuDropdown-un2zdn-2 ntLQD"]'
    WPlan_logout = '//*[@class="ant-btn ant-btn-link ButtonSC-vezrop-0 iUXEUv"]'

    def logout_page(self):
        # from selenium.webdriver import ActionChains
        # ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.IU_button_LOGOUT)).perform()
        time.sleep(1)
        self.driver.find_element_by_link_text(self.Project_logout_button).click()

class REGISTRATIONPage(Locators):
    """ REGISTRATION """
    Project_button_ENTER = 'Войти'  # '//div[@class="style_auth__links__eNZeW"]'
    Project_button_REGISTRATION = 'Зарегистрироваться'
    Project_button_REGISTRATION_submit = '//button[@type ="submit"]'
    Project_button_EMAIL = '/html/body/div/div/div/div[2]/form/a'
    Project_button_PHONE = '/html/body/div/div/div/div[2]/form/a'
    Project_input_field_phone_code = '//div[@id="__next"]//div[@class="full-height"]//div[@class="style_authorization__ZsrCS container"]//div[@class="style_sms-code__3udhR style_authorization-box__sms-code__3ixTs"]//div[@class="style_sms-code__item__249Nd style_input__3umsS "]//input[@id="sms-code"]'
    '//div[@id="__next"]//input[@id="sms-code"]'
    Project_input_field_email = ''
    Project_input_field_phone= '//input[@type="tel" and @name="phone"]'
    Project_input_field_password = '//input[@name="password"]'
    Project_button_REGISTRATION_finish = '//button[@type="submit"]'

class CONTACT_FORMPage(Locators):
    """ ФОРМА ЗАПИСИ НА ЗАНЯТИЕ """
    Project_contact_form_EMAIL = '//section[@class="style_main-screen__3oGaJ"]//input[@type="text" and @name="email"]'
    Project_contact_form_PHONE = '//section[@class="style_main-screen__3oGaJ"]//input[@type="tel" and @name="phone"]'
    Project_contact_form_NAME = '//section[@class="style_main-screen__3oGaJ"]//input[@type="text" and @name="name"]'
    Project_contact_form_submit_button = '//button[@type="submit" and contains(text(), "Запланировать занятие")]'
    Project_contact_form_phone_code = '//div[@class="style_sms-code__item__249Nd style_input__3umsS "]//input[@id="sms-code"]'
    Project_contact_form_password = '//form[@action="#"]//input[@name="password"]'
    Project_contact_form_password_submit_button = '//button[@type="submit" and contains(text(), "Готово")]'
    Project_contact_form_SUBJECT = '//button[@type="button" and contains(text(), "Алгебра")]'
    Project_contact_form_SUBJECT_class = '//label[@for="radio7" and contains(text(), "7 класс")]'
    Project_contact_form_next_button = '//button[@type="button" and contains(text(), "Далее")]'
    Project_contact_form_tutor = '//span[@class="style_checkbox__text__2eyhR" and contains(text(), "Подготовка к сдаче ОГЭ")]'
    Project_contact_form_text = '//div[@class=" style_textarea__3BZB3 "]//textarea[@class = "style_textarea__field__1MY9S"]'
    Project_contact_form_finish_button = '//button[@type="button" and contains(text(), "Готово")]'

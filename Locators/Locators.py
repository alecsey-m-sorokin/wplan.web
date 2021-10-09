import time


class Locators:
    """ MAIN PAGE """
    Project_mainPage = ''
    WPlan_Reports = 'Отчеты'
    WPlan_Workers = 'Сотрудники'
    WPlan_Groups = ''
    WPlan_Schedules = ''
    WPlan_Personal_Schedules = ''
    WPlan_Missed = ''
    WPlan_Offices = ''
    WPlan_History = ''
    WPlan_Documentation = ''

class WPlanLoginPage(Locators):
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

class WPlan_LogoutPage(Locators):
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

class WPlan_WorkerPage(Locators):
    """ WORKER """
    WPlan_Add_Worker = '//*[@id="root"]/div/section/section/main/div[2]/div/div/div[1]/button/span[2]'

class WPlan_WorkerRegistrationPage(Locators):
    """ REGISTRATION new worker """
    AD_switch_button0 = '//div[@class="FormItemIfADSC-sc-17npaor-1 ikICGY"]//div[@class="ant-switch-handle"]'
    AD_switch_button = '//div[@class="FormItemIfADSC-sc-17npaor-1 ikICGY"]//button[@type="button" and @aria-checked ="true"]'
    WPlan_switch_button = '//div[@class="FormItemIfADSC-sc-17npaor-1 ikICGY"]//button[@type="button" and @aria-checked ="false"]'
    Worker_AD_Login = '//div[@class="ant-col ant-col-24 ant-form-item-control"]//*[@id="cdcaf970ea8405197f261f9c55def47b"]'
    Worker_WPlan_Login = '//div[@class="ant-col ant-col-24 ant-form-item-control"]//*[@id="ad08de129f8fc04b1765b08450bf3b56"]'
    Worker_WPlan_Password = '//div[@class="ant-col ant-col-24 ant-form-item-control"]//*[@id="58d90d03dfa7cbc71d2f6b3f4d5dc78e"]'
    Worker_WPlan_Timex_Select = '//div[@class="ant-col ant-form-item-control ant-col-xs-24 ant-col-sm-24 ant-col-md-16 ant-col-lg-16"]//span[@class="ant-select-selection-search"]//*[@id = "9a9b64f5c5c36ef3974f69c294d13e97"]'
    Worker_WPlan_Timex_Id = '//div[@class="ant-col ant-col-24 ant-form-item-control"]//*[@id="3bee3e156d0ace6db096f503b27c12ed"]'
    Worker_WPlan_Select_Date = '//div[@class="ant-col ant-col-24 ant-form-item-control"]//*[@id="dff618ee3ff92d1fa9984129d7e2449b"]'
    Worker_WPlan_Name = '//div[@class="ant-col ant-col-24 ant-form-item-control"]//*[@id="01d251091776b0b0119e987159930c5b"]'
    Worker_WPlan_Family = '//div[@class="ant-col ant-col-24 ant-form-item-control"]//*[@id="bad80054eddf427b6e2adbfc7f4f7b9a"]'
    Worker_WPlan_MidName = '//div[@class="ant-col ant-col-24 ant-form-item-control"]//*[@id="353ac266bcc21b2d026bb71bfeaefde4"]'
    Worker_WPlan_Reddy_Id = '//div[@class="ant-col ant-col-24 ant-form-item-control"]//*[@id="44744aae4f39b3cbf59e965b438e7d76"]'

    """ OFFICE"""
    Worker_WPlan_Office = '//div[@class="ant-col ant-col-24 ant-form-item-control"]//div[@class="ant-select-selector"]//*[@id="5e58afebf604780a9fc25c82b5ded909"]'
    Worker_WPlan_Office_BY1 = '//div[@label="BY1"]'
    Worker_WPlan_Office_BY2 = '//div[@label="BY2,BY4,BY6"]'
    Worker_WPlan_Office_BY3 = '//div[@label="BY3"]'
    # Worker_WPlan_Office_BY1 = './/*[normalize-space(text()) and normalize-space(.)="BY1"])[4]/following::div[2]'
    # Worker_WPlan_Office_BY2 = './/*[normalize-space(text()) and normalize-space(.)="BY2,BY4,BY6"])[2]/following::div[2]'
    # Worker_WPlan_Office_BY3 = '(.//*[normalize-space(text()) and normalize-space(.)="BY3"])[2]/following::div[2]'

    """ WORKER ROLE"""
    # Worker_WPlan_Role = '//div[@class="ant-col ant-col-24 ant-form-item-control"]//span[@class="ant-select-selection-item" and @title = "Root"]'
    Worker_WPlan_Role = '//div[@class="ant-col ant-col-24 ant-form-item-control"]//div[@class="ant-select-selector"]//*[@id="21e6806b7db4cae32ee9e82794aed1f0"]'
    Worker_WPlan_Role_Root = '//div[@label="Root"]'
    Worker_WPlan_Role_Manager = '//div[@label="Менеджер"]'
    Worker_WPlan_Role_Lead = '//div[@label="Руководитель"]'
    Worker_WPlan_Role_Executor = '//div[@label="Исполнитель"]'
    # Worker_WPlan_Role_Root = '(.//*[normalize-space(text()) and normalize-space(.)="Root"])[3]/following::div[2]'
    # Worker_WPlan_Role_Manager = '(.//*[normalize-space(text()) and normalize-space(.)="Менеджер"])[2]/following::div[2]'
    # Worker_WPlan_Role_Executor = 'xpath=(.//*[normalize-space(text()) and normalize-space(.)="Исполнитель"])[19]/following::div[14]'
    # Worker_WPlan_Role_Lead = '(.//*[normalize-space(text()) and normalize-space(.)="Руководитель"])[3]/following::div[2]'

    Worker_WPlan_Group_Id = '//div[@class="ant-col ant-col-24 ant-form-item-control"]//div[@class="ant-select-selector"]//*[@id="782f16b1199d46a5961ddee06b782d60"]'
    Worker_WPlan_Schedule = '//div[@class="ant-col ant-col-24 ant-form-item-control"]//div[@class="ant-select-selector"]//*[@id="bedcd65b962e3b97eb7e769cc31d39df"]'
    Worker_WPlan_Schedule_1 = u'(.//*[normalize-space(text()) and normalize-space(.)="Нед Без вых 8"])[1]/following::div[2]'
    # Worker_WPlan_Schedule_2 = '//div[@label="Нед Вых:Вс 8.5" and @aria-selected="false"]'
    # Worker_WPlan_Schedule_3 = '//div[@label="Нед Вых:Вс 8.5"]'
    # Worker_WPlan_Schedule_4 = '//div[@class="ant-select-dropdown ant-select-dropdown-placement-topLeft "]//div[@role="listbox" and @id="bedcd65b962e3b97eb7e769cc31d39df_list"]//div[@aria-label="Нед Без вых 8" and @id="bedcd65b962e3b97eb7e769cc31d39df_list_0"]'
    Worker_Registration_Cancel_button = '//button[@type="button" and contains(span, "Отмена")]'
    Worker_Registration_Submit_button = '//button[@type="button" and contains(span, "Добавить сотрудника")]'

class WPlan_WorkerPermissionsPage(Locators):
    """ OFFICE """
    Add_Worker_All_Offices_Groups0 = '//*[@id="753cd56cf78d66147b1cf76c30226c4f"]/div'
    Add_Worker_All_Offices_Groups = '//*[@id="753cd56cf78d66147b1cf76c30226c4f"]'
    BY1 = '//*[@id="rc-tabs-0-panel-offices"]/div/div/div/div/div/div[1]/div[2]/ul/li[1]/label/span/input'
    BY2 = '//*[@id="rc-tabs-0-panel-offices"]/div/div/div/div/div/div[1]/div[2]/ul/li[2]/label/span/input'
    BY3 = '//*[@id="rc-tabs-0-panel-offices"]/div/div/div/div/div/div[1]/div[2]/ul/li[3]/label/span/input'

    """ GROUPS """
    Add_Groups_to_Worker_checkbox = '//*[@id="rc-tabs-0-panel-groups"]/div/div/div/div/div/div[1]/div[2]/ul/li[1]/label/span/input'
    Add_Groups_to_Worker_arrow = '//*[@id="rc-tabs-0-panel-offices"]/div/div/div/div/div/div[2]/button[1]/span/svg'
    Remove_Groups_from_Worker_checkbox = '//*[@id="rc-tabs-0-panel-offices"]/div/div/div/div/div/div[3]/div[2]/ul/li/label/span/input'
    Remove_Groups_from_Worker_arrow = '//*[@id="rc-tabs-0-panel-offices"]/div/div/div/div/div/div[2]/button[2]/span/svg'

    Worker_Permissions_Submit_button = '//button[@type="button" and contains(span, "Сохранить изменения")]'

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
    Project_input_field_phone = '//input[@type="tel" and @name="phone"]'
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




# "//div[contains(@class,'ajs-error') and contains(text(),'%s')]"
# //div[@class="ant-select-dropdown ant-select-dropdown-placement-topLeft "]//div[@role="listbox" and @id="bedcd65b962e3b97eb7e769cc31d39df_list"]//div[@aria-label="Нед Без вых 8" and @id="bedcd65b962e3b97eb7e769cc31d39df_list_0"]
# ActionChains(wPlanWorkerRegistration.driver).move_to_element(wPlanWorkerRegistration.driver.find_element_by_xpath('//*[@id="bedcd65b962e3b97eb7e769cc31d39df"]')).click().send_keys('Нед Вых:Вс 8.5').perform()
# wPlanWorkerRegistration.driver.find_element_by_id('bedcd65b962e3b97eb7e769cc31d39df').click()
# wPlanWorkerRegistration.driver.find_element_by_xpath('(.//*[normalize-space(text()) and normalize-space(.)="Нед Без вых 8"])[1]/following::div[2]').click()


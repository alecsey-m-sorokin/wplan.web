from datetime import datetime

from Pages.WPlan_apiPage import API_TestWPlan
from russian_names import RussianNames
import random
import string
import global_functions


authLogin, authToken = API_TestWPlan.AuthLogin('test_reddy_root', '11111111', useActiveDirectory=False)

print(f'authLogin = {authLogin}')
print(f'authToken = {authToken}')
#

postWorker, workerId = API_TestWPlan.PostWorker(authToken, name='Имммя', surName='Фамммилия', middleName='Отттчествво',
                                                wtEmploeeId=100502, startWork='2021-09-21T00:00:00', chatId='', officeId=1,
                                                scheduleId=60, scheduleName=None, roleId=3, groupIds=[10],
                                                login='nnname777', password='zaqWSX123#$', IsOnlyADProfileType=False,
                                                activeDirectoryLogin='', canEditTime=False, canEditSchedule=False)
#
# workerId = '4966'

getWorker, workerId = API_TestWPlan.GetWorker(authToken, workerId)

putWorker = API_TestWPlan.PutWorker(authToken, workerId, login='nnname888', password=None, activeDirectoryLogin='',
                                    isOnlyADProfileType=False, wtEmploeeId=100502, name='Имммяя2', surName='Фамммилияя2',
                                    middleName='Отттчестввоо2', startWork='2021-09-21T00:00:00', chatid='', officeId=1,
                                    scheduleId=60, scheduleName=None, roleId=3, groupIds=[10], canEditTime=False,
                                    canEditSchedule=False, canEditDayOffForHimself=False)

getWorker, workerId = API_TestWPlan.GetWorker(authToken, workerId)

# changePassword = API_TestWPlan.ChangePassword(authToken, iD=workerId, password='22222222', confirmPassword='22222222')
#
deleteWorker = API_TestWPlan.DeleteWorker(authToken, workerId)

workDay = datetime.today().strftime("%d.%m.%Y")
# print(workDay)

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
# postWorker, workerId = API_TestWPlan.PostWorker(authToken)
#
workerId = '4889'

getWorker = API_TestWPlan.GetWorker(workerId, authToken)
#
# deleteWorker = API_TestWPlan.DeleteWorker(workerId, authToken)

workDay = datetime.today().strftime("%d.%m.%Y")
print(workDay)

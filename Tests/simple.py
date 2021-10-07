from Pages.WPlan_apiPage import API_TestWPlan

authLogin, authToken = API_TestWPlan.AuthLogin('test_reddy_root', '11111111', useActiveDirectory=False)

print(f'authLogin = {authLogin}')
print(f'authToken = {authToken}')

postWorker, workerId = API_TestWPlan.PostWorker(authToken)

# workerId = '4916'

getWorker = API_TestWPlan.GetWorker(workerId, authToken)

deleteWorker = API_TestWPlan.DeleteWorker(workerId, authToken)

import requests


class API_TestWPlan:

    @staticmethod
    def AuthLogin(login, password, useActiveDirectory):
        params = {'login': login, 'password': password, 'useActiveDirectory': useActiveDirectory}
        print(f'params = {params}')
        response = requests.post('http://weplan-docker.xbet.lan:4011/Auth/Login', json=params,
                                 headers={'Connection': 'close'})
        print(response.url)
        assert response.status_code == 200
        response = response.json()
        authToken = response["token"]
        print(f'response = {response}')
        return response, authToken

    @staticmethod
    def PostWorker(token, name, surName, middleName, wtEmploeeId, startWork, chatId, officeId, scheduleId, scheduleName,
                   roleId, groupIds, login, password, IsOnlyADProfileType, activeDirectoryLogin, canEditTime,
                   canEditSchedule):
        params = {"name": name, "surName": surName, "middleName": middleName, "wtEmploeeId": wtEmploeeId,
                  "startWork": startWork, "chatid": chatId, "officeId": officeId, "scheduleId": scheduleId,
                  "scheduleName": scheduleName,
                  "roleId": roleId, "groupIds": groupIds, "login": login, "password": password,
                  "IsOnlyADProfileType": IsOnlyADProfileType, "activeDirectoryLogin": activeDirectoryLogin,
                  "canEditTime": canEditTime,
                  "canEditSchedule": canEditSchedule}
        print(f'params = {params}')
        response = requests.post('http://weplan-docker.xbet.lan:4011/Workers/Post', json=params,
                                 headers={'Authorization': f'Bearer {token}', 'Connection': 'close'})
        print(response.url)
        assert response.status_code == 200
        response = response.json()
        workerId = response
        print(f'response = {response}')
        print(f'workerId = {workerId}')
        return response, workerId

    @staticmethod
    def PutWorker(token, iD, login, password, activeDirectoryLogin, isOnlyADProfileType, wtEmploeeId, name, surName,
                  middleName, startWork, chatid, officeId, scheduleId, scheduleName, roleId, groupIds, canEditTime,
                  canEditSchedule, canEditDayOffForHimself):
        params = {"id": iD, "login": login, "password": password, "activeDirectoryLogin": activeDirectoryLogin,
                  "isOnlyADProfileType": isOnlyADProfileType, "wtEmploeeId": wtEmploeeId, "name": name,
                  "surName": surName, "middleName": middleName, "startWork": startWork, "chatid": chatid,
                  "officeId": officeId, "scheduleId": scheduleId, "scheduleName": scheduleName, "roleId": roleId,
                  "groupIds": groupIds, "canEditTime": canEditTime, "canEditSchedule": canEditSchedule,
                  "canEditDayOffForHimself": canEditDayOffForHimself}
        print(f'params = {params}')
        response = requests.put('http://weplan-docker.xbet.lan:4011/Workers/Put', json=params,
                                headers={'Authorization': f'Bearer {token}', 'Connection': 'close'})
        print(response.url)
        assert response.status_code == 200
        response = response
        print(f'response = {response}')
        return response

    @staticmethod
    def ChangePassword(token, iD, password, confirmPassword):
        params = {"id": iD, "password": password, "confirmPassword": confirmPassword}
        print(f'params = {params}')
        response = requests.put('http://weplan-docker.xbet.lan:4011/Workers/ChangePassword', json=params,
                                headers={'Authorization': f'Bearer {token}', 'Connection': 'close'})
        print(response.url)
        assert response.status_code == 200
        response = response
        print(f'response = {response}')
        return response

    @staticmethod
    def GetWorker(token, iD):
        params = {'Id': iD}
        print(f'params = {params}')
        response = requests.get('http://weplan-docker.xbet.lan:4011/Workers/GetWorker', params=params,
                                headers={'Authorization': f'Bearer {token}', 'Connection': 'close'})
        print(response.url)
        assert response.status_code == 200
        response = response.json()
        workerId = response["id"]
        print(f'response = {response}')
        print(f'workerId = {workerId}')
        return response, workerId

    @staticmethod
    def DeleteWorker(token, iD):
        params = {'Id': iD}
        print(f'params = {params}')
        response = requests.delete('http://weplan-docker.xbet.lan:4011/Workers/Delete', params=params,
                                   headers={'Authorization': f'Bearer {token}', 'Connection': 'close'})
        print(response.url)
        assert response.status_code == 200
        # response = response.json()
        print(f'response = {response}')
        return response

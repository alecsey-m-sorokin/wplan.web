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
    def PostWorker(token):
        params = {"name": "Имммя", "surName": "Фамммилия", "middleName": "Отттчествво", "wtEmploeeId": 100501,
                  "startWork": "2021-09-21T00:00:00",
                  "chatid": "", "officeId": 1, "scheduleId": 60, "scheduleName": 'null', "roleId": 3, "groupIds": [10],
                  "login": "nnname666", "password": "11111111",
                  "IsOnlyADProfileType": False, "activeDirectoryLogin": "", "canEditTime": False,
                  "canEditSchedule": False}
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
    def GetWorker(iD, token):
        params = {'Id': iD}
        print(f'params = {params}')
        response = requests.get('http://weplan-docker.xbet.lan:4011/Workers/GetWorker', params=params,
                                headers={'Authorization': f'Bearer {token}', 'Connection': 'close'})
        print(response.url)
        assert response.status_code == 200
        response = response.json()
        print(f'response = {response}')
        return response

    @staticmethod
    def DeleteWorker(iD, token):
        params = {'Id': iD}
        print(f'params = {params}')
        response = requests.delete('http://weplan-docker.xbet.lan:4011/Workers/Delete', params=params,
                                   headers={'Authorization': f'Bearer {token}', 'Connection': 'close'})
        print(response.url)
        assert response.status_code == 200
        # response = response.json()
        print(f'response = {response}')
        return response

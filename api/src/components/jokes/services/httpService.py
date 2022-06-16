import requests


class Service:
    @staticmethod
    def request(url: str):
        headers = {'Content-type': 'application/json',
                   'Accept': 'application/json'}
        response = requests.get(url, headers=headers)
        return response.json()

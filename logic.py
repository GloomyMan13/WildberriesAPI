import requests
from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
headers["Authorization"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9." \
                           "eyJhY2Nlc3NJRCI6ImJkZDdkODBmLTM5ZWMtN" \
                           "DZjNS1hYzQwLWViZmU5ZWViMTEzMCJ9.xw0Nx" \
                           "D2s58Uu-S8XrvKux6gvULzxRi_8PSiO9jdtQrA"


class Getters:
    def __init__(self, request_link, params, head=headers):
        if isinstance(request_link, str):
            self.link = request_link
        else:
            raise ValueError('Link must be a string')
        if isinstance(headers, requests.structures.CaseInsensitiveDict):
            self.headers = head
        else:
            raise ValueError('Headers must be a dict')
        if isinstance(params, str):
            self.params = params
        else:
            raise ValueError('Params must be a string')

    def responce(self):
        responce = requests.get(self.link + self.params, headers=self.headers)
        return responce.json()



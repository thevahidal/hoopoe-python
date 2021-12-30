import requests

import constants

class Hoopoe:
    def __init__(self, api_key, version, base_url=constants.base_url):
        if not api_key:
            raise ValueError("api_key is required")
        if version and not version:
            raise ValueError("version is not valid")

        self.api_key = api_key
        self.base_url = base_url
        self.version = version or constants.version
        self.session = requests.Session()
        self.session.headers.update(
            {
                "X-API-Key": "Bearer {}".format(self.api_key),
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

    def timestamp(self):
        url = f"{self.base_url}/v{self.version}/timestamp/"
        response = self.session.get(url)
        print(url, response)
        return response.json()

    def upupa(self, message, extra={}):
        url = f"{self.base_url}/v{self.version}/upupa/"
        data = {
            "message": message,
            "extra": extra,
        }
        response = self.session.post(url, json=data)
        return response.json()

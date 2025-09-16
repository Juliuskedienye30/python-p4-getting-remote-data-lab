# lib/GetRequester.py
import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # return raw bytes so it matches JSON_STRING in tests
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # convert the raw bytes into Python data
        body = self.get_response_body()
        return json.loads(body)

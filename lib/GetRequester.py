import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url   # store the API URL when object is created

    def get_response_body(self):
        response = requests.get(self.url)  
        return response.content   # returns raw bytes (b'...')

    def load_json(self):
        body = self.get_response_body()
        return json.loads(body)   # parse bytes into Python dict/list

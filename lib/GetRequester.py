import requests  # to handle HTTP requests
import json  # to parse JSON data

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Sends a GET request to the URL and returns the raw content as bytes
        response = requests.get(self.url)
        response.raise_for_status()  # raises an error if the request failed
        return response.content  # return the raw content as bytes

    def load_json(self):
        # Converts the response body from JSON format to Python data types
        response_body = self.get_response_body()
        return json.loads(response_body.decode('utf-8'))  # Decode bytes to str, then parse JSON

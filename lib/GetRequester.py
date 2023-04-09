import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url = self.url
        print(url)

        response = requests.get(url)
        response_content = response.content
        print(response_content)
        return response_content

    def load_json(self):
        unrefined_json = self.get_response_body()

        refined_json = json.loads(unrefined_json)

        return refined_json

print 
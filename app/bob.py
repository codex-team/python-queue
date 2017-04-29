import json
import requests
from server import Server


class Bob(Server):

    def handle(self, message):
        try:
            print("Got: {}".format(message))
            url = json.loads(str(message, 'ascii'))["url"]
            response = requests.get(url)
        except Exception as e:
            print("Error: {}".format(e))
        else:
            result = {}
            result['status_code'] = response.status_code
            self.send("localhost", 8889, json.dumps(result))


if __name__ == "__main__":
    print("Bob started.")

    getter = Bob("localhost", 8887)
    getter.start_server()
    getter.loop()
    getter.stop_server()

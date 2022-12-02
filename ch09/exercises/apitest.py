import requests
import json

response = requests.get('https://v2.jokeapi.dev/joke/Any').json()

print(response)

import requests

response = requests.get('https://randomuser.me/api/').json()
response.text





  
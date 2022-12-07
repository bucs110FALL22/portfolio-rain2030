import requests
import json
class IndiaCovid():
    def __init__(self, url):
      self.url= url
      self.locations = None
      self.active_case = None
      self.confirmed = None
      self.migrated = None
      self.recovered = None
      self.deceased = None
      
    def get(self):
#print(response_API.status_code)
      response_API = requests.get(self.url)
      data = response_API.text
      json.loads(data)
      parse_json = json.loads(data)
  
      location = int(input("Choose a region to learn more about its Covid Cases"
  "\n1 for North and Middle Andaman, 2 for South Andaman, 3 for Andaman and Nicobar Islands:"
  "\n"))
      if(location == 1):
        self.locations = 'North and Middle Andaman'
      elif(location == 2):
        self.locations = 'South Andaman'
      elif(location == 3):
        self.locations = 'Nicobars'
  
      self.active_case = parse_json['Andaman and Nicobar Islands']['districtData'][self.locations]['active']

      self.confirmed = parse_json['Andaman and Nicobar Islands']['districtData'][self.locations]['confirmed']

      self.migrated = parse_json['Andaman and Nicobar Islands']['districtData'][self.locations]['migratedother']

      self.deceased = parse_json['Andaman and Nicobar Islands']['districtData'][self.locations]['deceased']

      self.recovered = parse_json['Andaman and Nicobar Islands']['districtData'][self.locations]['recovered']


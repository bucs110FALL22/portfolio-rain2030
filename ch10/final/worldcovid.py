import requests
import json

class WorldCovidCases():
  def __init__(self, url, country):
      self.url= url
      self.country = country
      response_world = requests.get(url)
      data = response_world.text
      parse_json = json.loads(data)
      self.active_case = parse_json['data'][0]['total_cases']
      self.recov = parse_json['data'][0]['change_recoveries']
      self.vaccination = parse_json['data'][0]['change_vaccinations']
      self.tests = parse_json['data'][0]['total_tests']
      print("active cases in",country,": ",self.active_case)
      print("recovered cases in",country,": ", self.recov)
      print("vaccinations in ",country,": ",self.vaccination)
      print("total tests in ",country,": ",self.tests)

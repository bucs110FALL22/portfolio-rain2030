from covid import IndiaCovid
from worldcovid import WorldCovidCases
class Variablename():
  def __init__(self, india, ca):
    self.india = india
    self.ca = ca
  def get(self):
    indiaCovid = IndiaCovid(self.india)
    indiaCovid.get()
    print("\nCovid Cases in India's Region")
    print("\nActive cases in ", indiaCovid.locations,":", indiaCovid.active_case,
      "\nconfirmed: ", indiaCovid.confirmed,
      "\nmigrated: ", indiaCovid.migrated,
      "\ndeceased: ", indiaCovid.deceased,
      "\nrecovered: ", indiaCovid.recovered)
    print("--------------------------------")
    caCovid = WorldCovidCases(self.ca, "Canada")
    

    difference_in_Recovery = int(caCovid.recov) - int(indiaCovid.recovered)
    difference_in_Active = int(caCovid.active_case) - int(indiaCovid.active_case)
    print("\nConclusion:")
    print("\nCanada have ", difference_in_Recovery, " people Recovered from Covid Cases, and" 
          , "\n", difference_in_Active, "Active Cases in Canada than", indiaCovid.locations)

ca = Variablename("https://api.covid19india.org/state_district_wise.json",
            "https://api.covid19tracker.ca/summary")
ca.get()


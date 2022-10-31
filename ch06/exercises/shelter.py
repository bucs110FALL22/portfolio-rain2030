import time
class Shelter():

  def __init__(self, name, type, time, date):
    self.name = name
    self.type = type
    self.id = id(self)
    self.time = time
    self.date = date

id1 = Shelter("Bobby", "Bulldog", "12/12/12", time.strftime("%d/%m/%Y"))
print(id1.name, id1.type, id1.id, id1.time, id1.date, id1.id)
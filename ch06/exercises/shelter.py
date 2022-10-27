import datetime
timern = datetime.datetime.now()
class Point():

  def __init__(self, name="Bobby", type="Dog", id = 0, time = timern):
    self.name = name
    self.type = type
    self.id = id + 1
    self.time = time
    
p1 = Point()
print(p1.name, p1.type, p1.id, p1.time, type(p1))
p2 = Point()
print(p2.name, p2.type, p2.id, p2.time, type(p2))

p1.name = "Merry"
p1.type = "Dog"
p1.id= 1
p2.name = "champ"
p2.type = 'Turtle'
p2.id = 0 
print(p1.name, p1.type, p1.id, p1.time, type(p1))
print(p2.name, p2.type, p2.id, p2.time, type(p2))
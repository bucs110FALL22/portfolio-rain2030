from datetime import date
class Shelter():

  def __init__(pet, names, type, id, dateadopt):
    pet.names = names
    pet.type = type
    pet.id = id
    pet.dateadpot = dateadopt
    
  def say_hi(pet):
    print('Pet Name', pet.name, 'Type is:', pet.type, 'id is:', pet.id, 'date adopted:', pet.dateadopt)
    
p1 = Shelter('Bob','Dog', 1, date.today())
p2 = Shelter('Mary','Cat', 2, date.today())

print(p1)
  
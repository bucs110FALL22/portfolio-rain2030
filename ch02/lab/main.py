import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
class_per_week = 3
print(class_per_week)
cost_per_class = cost_per_week//class_per_week
print("Cost per class with 3 days in each week:")
print(int(cost_per_class))
print("Have A Great Day!")
#cost_per_week is a float
#class per week is an int
#cost_per_class is an float but in this case, where the decimal postion is unnessary I put a converter of (int(var)) to convert it back to an int
#weeks is an int
#classes is an int
#tuition is an int
#----------------------------------------------------------
print("") # for formatting/ spacing
print("") # for formatting/ spacing
#Part B
print("Selcting a random number from 5,10,13,44,72")
numbers=[10,5,13,44,72]
selected = random.choice(numbers)
print(selected)


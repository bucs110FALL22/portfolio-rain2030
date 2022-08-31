print("Part 1")
#practice problems
num1 = 10 * 5
print("10 x 5 = ",num1)

num2 = 10 ** 2
print("10^2= ",num2)

num3 = 15 / 10
print("15/10 = ",num3)

num4 = 15 // 10
print("15/10(without decimals) = ",num4)

num5 = -15 // 10
print("-15/10(without decimals) = ",num5)
#floor division always round down, I guess?
num6 = 15 % 10
print("Reminder of 15/10 = ", num6)

num7 = 10 % 5
print("Reminder of 15/5 = ",num7)

num8 = 10 % 10
print("Reminder of 10/10 = ",num8)

num9 = 0 % 10
print("Reminder of 0/10 = ",num9)

num10 = 10 / 15
print("10 / 5 = ", num10)
#now num 10 have an issue of not rounding up the last digit displayed
#----------------------------------------------------------------------
print("")
print("")
#----------------------------------------------------------------------
print("Part 2 (Currency Exchange)")


x = input("How much Euros do you have?")
amount = float(x) #need to be decimal for a realistic number
y = input("what is the rate of Euros to Dollars Right Now?")
rate = float(y) #need decimal to have a more realistic rate
total = amount * rate # exchange from euros to dollars
result = total - 3 #subtracting 3 due to service fee
print ("You successfully converted ", amount, " Euros to ", result, " Dollars "
      "with the current rate of ", rate, " Dollars per Euro and a service fee of 3 dollars") 
#above is the final result.
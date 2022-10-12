
#multiplication
def multiplication(x , n):
    for i in range(n-1):
      x += x
    return x 
# Driven code to check above function
x = 70
n = 2
print(multiplication(x, n))
  
#exponent
def exponent(z,y):
  for i in range(y-1):
    z *= z
  return z 
# Driven code to check above function
z = 70
y = 2
print(exponent(z, y))

#square
x = 10
n = 2
sqaure = multiplication(x,n) * multiplication(x,n)
print (sqaure)
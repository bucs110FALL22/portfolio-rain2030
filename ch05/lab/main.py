
def threenaddone(n):
    counter = 0
    while n != 1: 
      print(n,"count:",counter)
      if n % 2 == 0:        # n is even
        n = n // 2
        counter+=1
      else:                 # n is odd
        n = n * 3 + 1
        counter += 1
    print(n,"count:",counter)                 
threenaddone(101)

upper_limit = 20
iters = {}
start = 2

for start in range (upper_limit):
  threenaddone(start)
  iters = iters.append(start)
  start += 1
  print(iters)

star_pyramid = int(input("number of rows"))
for i in range(1,star_pyramid+1):
  for x in range(1, i+1):
    print("*", end = "")
  print()

rstar_pyramid = int(input("number of rows"))
for i in range(rstar_pyramid,0,-1):
  for x in range(0, i):
    print("*", end = "")
  print()
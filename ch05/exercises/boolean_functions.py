def percentage_to_letter(score):
  if (score>=90):
    print("you passed")
    return "A"
  elif (80<= score <90):
    print("you passed")
    return "B"
  elif (70<=score<80):
    print("you passed")
    return "C"
  elif (60<= score <70):
    print("You Failed")
    return "D"
  elif (score<60):
    print("You Failed")
    return "F"

def is_passing(score):
  if score == "A":
    score = True
  elif score == "B":
    score = True
  elif score == "c":
    score = True
  elif score == "D":
    score = False
  elif score == "F":
    score = False

def main():
  score = int(input("input your score:"))
  is_passing(score)
  print("You got:",percentage_to_letter(score))
  
main()
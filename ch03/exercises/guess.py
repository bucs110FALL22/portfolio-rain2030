import random
number = random.randint(1,10)

guesses = 3
attempt_guess = guesses
for i in range(guesses):
  user = int(input("what is your guess from 1 to 10?"))
  if (user > number):
    print("the guess is higher than the actual number, guess again", attempt_guess - 1,"guesses left")
    attempt_guess -= 1
  elif (user < number):
    print("the guess is lower than the actual number, guess again", attempt_guess - 1,"guesses left")
    attempt_guess -= 1
  elif (user == number):
    print("you got it!")
    break
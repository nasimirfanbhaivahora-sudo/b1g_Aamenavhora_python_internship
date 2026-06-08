import random
private_number = random.randint(1, 20)
print("Welcome to the Number Guessing Game! I have picked a number between 1 and 20.")

while True:
  guess = int(input("Enter your guess: "))
  
  if guess > private_number:
    print("Too High")
  elif guess < private_number:
    print("Too Low")
  else:
    print("Correct!")
    break
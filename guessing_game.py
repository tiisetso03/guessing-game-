import random
secret_number = random.randint(1, 10)  #Generate a secret number from 1 to 10
print("welcome to the Number Guessing Game!")
print("I am thinking of number between 1 to 10.")

#Start the game loop
while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Congratulation! You got it right.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

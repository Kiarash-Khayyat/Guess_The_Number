import art
print(art.logo)

import random
def generate():
    a = random.randint(1,100)
    return a

number = generate()
attempts = 0

print("Welcome to the number guessing game!\nI am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

status = "losing"

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high.\nGuess agian.")
        attempts -= 1
        
    elif guess < number:
        print("Too low.\nGuess again.")
        attempts -= 1
        
    elif guess == number:
        attempts = 0
        status = "winning"

if status == "winning":
    print(f"You got it. The answer was {number}.")
elif status == "losing":
    print("You ran out of attempts, you lose.")

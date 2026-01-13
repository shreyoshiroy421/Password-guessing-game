import random

easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

print("Hi, welcome to my password guessing game")
print("Choose the level of difficulty: easy, medium or hard")

level = input('enter difficulty : ').lower()

if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("invalid choice. Defaulting to easy level")
    secret = random.choice(easy_words)

attempts = 0
max_attempts = 5  # Set the limit here
print(f"Guess the secret password (You have {max_attempts} tries!)")

while attempts < max_attempts:
    guess = input("enter your guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f'Congrats! you guessed it in {attempts} attempts')
        break
    else:
        # Tell them how many tries they have left
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong! You have {remaining} attempts left.")

# This part checks if they actually won or just ran out of turns
if guess != secret:
    print(f"Sorry, you're out of tries! The word was: {secret}")

print("game over")

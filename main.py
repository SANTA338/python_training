import atm
import random
random_number = random.randint(1, 10)

print(" Guess the Number Game")
print("you picked a number between 1 and 10. You have 3 chances!")

chances = 3

while chances > 0:
    guess = int(input(f"Enter your guess (1–10) |Chances left: {chances}  "))
    
    if guess == random_number:
        print("Correct! You guessed the number:", random_number)
        break
    elif guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
    chances -= 1

if chances == 0:
    print(" Game Over! The correct number was:", random_number)
atm.game()

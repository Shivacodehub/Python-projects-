import random
import os

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def guess_the_number():
    print("Welcome to Guess the Number Game!")
    max_num = int(input("Enter the maximum number for the range: "))
    number_to_guess = random.randint(0, max_num)
    print("You have total 10 attempts for easy level and 5 attempts for hard level for every guess your attempts count is decreases")
    difficulty = input("Choose a difficulty level: easy or hard: ")
    
    if difficulty.lower() == "easy":
        attempts = 10
    elif difficulty.lower() == "hard":
        attempts = 5
    else:
        print("Invalid difficulty level. Defaulting to easy.")
        attempts = 10
    
    while attempts > 0:
        print(f"Attempts remaining: {attempts}")
        user_guess = int(input(f"Guess a number between 0 and {max_num}: "))

        if user_guess < number_to_guess:
            if difficulty.lower() == "easy":
                if number_to_guess - user_guess <= 5:
                    print("***your guessed number is less than number to guess***")
                else:
                    print("***your guessed number is very less than number to guess***")
            elif difficulty.lower() == "hard":
                print("***your guessed number is less than number to guess***")
        elif user_guess > number_to_guess:
            if difficulty.lower() == "easy":
                if user_guess - number_to_guess <= 5:
                    print("***your guessed number is higher than number to guess***")
                else:
                    print("***your guessed number is very high than number to guess***")
            elif difficulty.lower() == "hard":
                print("***your guessed number is  higher than number to guess***")
        else:
            print(f"Congratulations! You've guessed the number in {10 - attempts + 1} attempts.")
            break

        attempts -= 1

    if attempts == 0:
        print(f"Game over! The number was {number_to_guess}.")

    play_again = input("Would you like to play again? (yes/no): ")
    if play_again.lower() == "yes":
        clear_screen()
        guess_the_number()
    else:
        print("Thanks for playing!")

guess_the_number()
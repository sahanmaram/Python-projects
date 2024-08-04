import random
from words_to_num import text_to_num

# Number Guesser Game which can take words as an input (level: Easy)
# Author: Sahan Maram
class number_guesser():

    def __init__(self):
        self.guess = self.guess_the_number()

    # created a separate function to get the input from user converted to an integer
    def get_guess(self):
        while True:
            user_guess = input("\n Guess the number: ")
            if user_guess.isdigit():
                user_guess = int(user_guess)
                if user_guess > 0:
                    return user_guess
                else:
                    print("\n Please enter a positive number next time...")
            elif user_guess.lower() in ['exit', 'quit']:
                print("\n Quitting the game... See you next time!\n\n")
                quit() 
            else:
                try:
                    user_guess = text_to_num(user_guess)
                    return user_guess
                except ValueError:
                    print("\n Invalid input. Please enter a number or type 'exit'/'quit' to quit...")

    # actual implementation that asks for a max range the user wants to guess till
    def guess_the_number(self):
        top_range = input("\n Type the MAX range of the number you wanna guess: ")

        if top_range.isdigit():
            top_range = int(top_range)
            if top_range <= 0:
                print("\n Please enter a positive number next time... C yea!")
                quit()
        else:
            top_range = int(text_to_num(top_range))

        print(f"\nTop of range given -> {top_range}")
        guessing_number = random.randrange(1, top_range+1)

        print("\n Start guessing the number... If you wanna quit Type 'exit/quit' \n")
        guesses = 0
        while True:
            user_guess = self.get_guess()
            guesses += 1
            if user_guess == guessing_number:
                    print(f"\n Congrats! You guessed the number {guessing_number} correctly!")
                    break
            elif user_guess < guessing_number:
                print(" You guessed lower! Try again!")
                continue
            else:
                print(" You guessed higher! Try again!")
                continue

        print(f"\n No:of guesses made: {guesses}\n")


# creating an object so that the __init__() function gets triggered and the game starts.                 
game = number_guesser()
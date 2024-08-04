#Basic computer quiz game (level: Easy)
#Author: Sahan Maram
class quiz_game():
    def __init__(self):
        #adding a score/points for the player
        self.score = 0

    def correct_case_function(self):
        print("That's Correct! +1 point...\n")
        self.score += 1 

    def main(self):
        print("Welcome to the Quiz Game!")

        #asking the player's name
        player_name = input("Player Name: ").strip()
        print("Hello " + player_name)

        #checking if the player wants to play
        playing = input("Do you wanna play?(y/n): ").strip()
        print("Let's get started!" if playing.lower() in ["y", "yes"] else "Too Bad... c yea!")

        if playing.lower() not in ["y", "yes"]:
            quit()

        #asking first question
        answer = input("What does CPU stand for? -> ")
        if answer.strip().lower() == "central processing unit":
            self.correct_case_function()
        else:
            print("Incorrect. The correct answer is Central Processing Unit.")

        #asking second question
        answer = input("What does GPU stand for? -> ")
        if answer.strip().lower() == "graphics processing unit":
            self.correct_case_function()
        else:
            print("Incorrect. The correct answer is Graphics Processing Unit.")

        #asking third question
        answer = input("What does RAM stand for? -> ")
        if answer.strip().lower() == "random access memory":
            self.correct_case_function()
        else:
            print("Incorrect. The correct answer is Random Access Memory.")

        #asking fourth question
        answer = input("What does PSU stand for? -> ")
        if answer.strip().lower() == "power supply unit":
            self.correct_case_function()
        else:
            print("Incorrect. The correct answer is Power Supply Unit.")

        print(f"\n Your total Score is: {self.score}")
        print(f" You got {(self.score/4)*100}% of answers correct... See you next time!\n")


game = quiz_game()
game.main()  # calling the main function of the class

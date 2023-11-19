import random

def play_guessing_game(guessed_right = 0):
    '''
    Starting game
    '''
    random_num = random.randint(0, 10)
    user_guess = int(input("Guess a number 0-10: "))

    if user_guess == random_num:
        print("You guessed right!")
        guessed_right += 1
    else:
        print("The correct answer was", random_num)

    guess_again = input("Would you like to play again? (yes/no) " )
    if guess_again == "yes":
        play_guessing_game(guessed_right)
    else:
        print("Thank you for playing!")
        print("You guessed right", guessed_right, "time(s).")

play_guessing_game()

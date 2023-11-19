from random import randint

def open_message():
    '''Opening message'''
    print('''
          Get ready to play Rock, Paper, Scissors!
          ''')
    question = input("Would you like instructions?(yes/no) ")

    if question == "yes":
        print('''
              Rock, Paper, Scissors is an exciting game!
              Pit your wit against the computer!
              Choose a player: Rock, Paper, Scissors.
              The computer chooses a player.
              Every time you win, you get a +1
              If there is a draw, no point is given.
              You will play 5 rounds
              Scissor cuts Paper, Paper slaps Rock, and Rock crushes scissors
              ''')

roles = ["Rock", "Paper", "Scissors"]
round_ = 5
player_wins = 0
computer_wins = 0
tie_ = 0
first_run = True


for _ in range(round_):
    if first_run:
        open_message()
        first_run = False

    computer = roles[randint(0,2)]
    player = input("Rock, Paper, Scissors?> ")

    if player not in roles:
        print("Invalid input. Please choose 'Rock', 'Paper', 'Scissors'.")
        continue

    if computer == player:
        print("Tie! No score given")
        tie_ += 1
    elif computer == "Rock":
        if player == "Scissors":
            computer_wins +=1
            print(f"Computer chose: {computer}")
            print("Player score: ", player_wins)
            print("Computer score: ", computer_wins)
        else:
            player_wins +=1
            print(f"Computer chose: {computer}")
            print("Player score: ", player_wins)
            print("Computer score: ", computer_wins)
    elif computer == "Scissors":
        if player == "Rock":
            player_wins += 1
            print(f"Computer chose: {computer}")
            print("Player score: ", player_wins)
            print("Computer score: ", computer_wins)
        else:
            computer_wins += 1
            print(f"Computer chose: {computer}")
            print("Player score: ", player_wins)
            print("Computer score: ", computer_wins)
    elif computer == "Paper":
        if player == "Rock":
            computer_wins += 1
            print(f"Computer chose: {computer}")
            print("Player score: ", player_wins)
            print("Computer score: ", computer_wins)
        else:
            player_wins += 1
            print(f"Computer chose: {computer}")
            print("Player score: ", player_wins)
            print("Computer score: ", computer_wins)
    elif computer == "Paper":
        if player == "Scissors":
            player_wins += 1
            print(f"Computer chose: {computer}")
            print("Player score: ", player_wins)
            print("Computer score: ", computer_wins)
        else:
            computer_wins += 1
            print(f"Computer chose: {computer}")
            print("Player score: ", player_wins)
            print("Computer score: ", computer_wins)


if player_wins > computer_wins:
    print("You win! The score was: ", player_wins, " to ", computer_wins,". With tie:", tie_)
elif player_wins == computer_wins:
    print("Tie")
else:
    print("You lose!, The score was: ", player_wins, " to ", computer_wins,". With tie:", tie_)
   
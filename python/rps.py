# Rock Paper Scissors

# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!

def rps(p1, p2):
    if p1 == p2:
        print("Draw")

    elif p1 == "scissors" and p2 == "paper":
        print("Player 1 won!")

    elif p1 =="scissors" and p2 == "rock":
        print("Player 2 won!")

    elif p1 == "rock" and p2 == "paper":
        print("Player 2 won!")
    
    elif p1 == "paper" and p2 == "rock":
        print("Player 1 won!")

    elif p1 == "paper" and p2 == "scrissors":
        print("Player 2 won!")
    
    elif p1 == "rock" and p2 == "scissors":
        print("Player 1 won!")
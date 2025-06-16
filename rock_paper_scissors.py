from random import choice

moves = ('r','p','s')

wins = 0
losses = 0

while True:
    userMove = input("enter r, p, s: ").lower()
    computerMove = choice(moves)
    print(f"your move: {"paper" if userMove == "p" else "rock" if userMove=="r" else "scissors"}")
    print(f"PC's move: {"paper" if computerMove == "p" else "rock" if computerMove=="r" else "scissors"}")
    if userMove == computerMove:
        print("it's a tie")
    elif userMove == "r":
        if computerMove == "p":
            print("you lose!")
            losses += 1
        elif computerMove == "s":
            print("you won!")
            wins += 1
    elif userMove == "p":
        if computerMove == "s":
            print("you lose!")
            losses += 1
        elif computerMove == "r":
            print("you won!")
            wins += 1
    elif userMove == "s":
        if computerMove == "r":
            print("you lose!")
            losses += 1
        elif computerMove == "p":
            print("you won!")
            wins += 1
    elif userMove == "q":
        break
    else:
        print(f"enter 'r', 'p' or 's'")
            
print(f"you won for {wins} times")
print(f"you lost for {losses} times")
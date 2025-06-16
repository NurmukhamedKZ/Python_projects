import random
import time

def spin(bet):
    symbols = ("🍎","🍋","🍌","🍉","🍓")
    print("Spinning...")
    print()
    comsym = [random.choice(symbols) for i in range(3)]
    print(comsym[0])
    time.sleep(0.5)
    print(comsym[1])
    time.sleep(0.5)
    print(comsym[2])
    time.sleep(0.5)
    print()
    
    print(f"┌─────────────┐")
    print("│ ",end="")
    print(comsym[0], end="")
    print("  ", end="")
    print(comsym[1], end="")
    print("  ",end="")
    print(comsym[2]+"  │")
    print(f"└─────────────┘")
    print()
    if comsym[0] == comsym[1] == comsym[2]:
        print("JeckPot!!!")
        return bet*2
    elif comsym[0] == comsym[1] or comsym[0] == comsym[2] or comsym[1] == comsym[2]:
        print("you won!")
        return bet
    else:
        print("you lose!")
        return -bet

    

def show_balance(balance):
    print(f"Current balance: ${balance:.2f}")

def main():
    balance = 100
    loop = True
    spinloop = True
    print("──────────────────────────")
    print("WELCOME TO NUREKE's CASINO")
    print("symbols: 🍎 🍋 🍌 🍉 🍓")
    print("──────────────────────────")
    show_balance(balance)
    while loop:
        if balance == 0:
            print(f"you are broke")
            loop = False
            break
        bet = float(input("your bet: "))
        if bet > balance:
            print(f"you can't bet ${bet}, you only have ${balance}")
            continue
        balance += spin(bet)
        show_balance(balance)
        while spinloop:
            usermove = input("spin again? (Y/N): ").upper()
            if usermove == "Y":
                spinloop = False
            elif usermove == "N":
                spinloop = False
                loop = False
        spinloop = True

if __name__ == "__main__":
    main()

import time

def showBalance(balance):
    print(f"balance: ${balance:.2f}")
    time.sleep(1)
    

def deposit():
    while True:
        dep = input("deposit money: ")
        if dep.isdigit():
            if float(dep) > 0:
                return float(dep)
            else:
                print("enter a positive number")
        else:
            print("enter a number")

def withdraw(balance):
    while True:
        dep = input("withdraw money: ")
        if dep.isdigit():
            if float(dep) > 0:
                if float(dep) <= balance:
                    return float(dep)
                else:
                    print("you're trying to withdraw too much")
            else:
                print("enter a positive number")
        else:
            print("enter a number")

def main():
    balance = 0
    print("*********************")
    print("   Banking Program   ")
    while True:
        print("*********************")
        print("1) show balance")
        print("2) deposit")
        print("3) withdraw")
        print("4) exit")
        print("*********************")
        user_choice = int(input("enter (1-4): "))
        match user_choice:
            case 1:
                showBalance(balance)
            case 2:
                balance += deposit()
                showBalance(balance)
            case 3:
                balance -= withdraw(balance)
                showBalance(balance)
            case 4:
                break
            case "_":
                print("enter a valid operation")
    
if __name__ == "__main__":
    main()
# hangman game
import random


def showgame(mas: list[str]):
    
    print(f"*********")
    print(f"    {mas[0]}    ")
    print(f"   {mas[2]}{mas[1]}{mas[3]}   ")
    print(f"   {mas[4]} {mas[5]}   ")
    print(f"*********")
    
def letterchanger(let: str, mas: list[str], word):
    for i in range(word.count(let)):
        ind = word.index(let)
        mas[ind] = let
        word[ind] = " "
    return mas
    
def organmaker(mas: list[str], cnt: int):
    match cnt:
        case 0:
            mas[0] = "O"
        case 1:
            mas[1] = "|"
        case 2:
            mas[2] = "/"
        case 3:
            mas[3] = "\\"
        case 4:
            mas[4] = "/"
        case 5:
            mas[5] = "\\"
    return mas
    

def main():
    words = ("ant", "ape", "bat", "bear", "bee", "bird", "cat", "chicken", "cow", "crab",
    "deer", "dog", "duck", "eel", "elephant", "fish", "fly", "fox", "frog",
    "goat", "horse", "lion", "monkey", "mouse", "pig", "rat", "shark", "sheep",
    "snake", "spider", "tiger", "whale", "wolf", "zebra")
    word = list(random.choice(words))
    zapas = []
    zapas += word
    parts = [" "," "," "," "," "," "]
    guessed = set()
    hiddenword = ["_"]*len(word)
    
    showgame(parts)
    print(" ".join(hiddenword))
    cnt = 0
    while True:
        user = input("enter a letter: ").lower()
        
        if len(user) != 1 or user.isdigit():
            continue
        
        elif user in guessed:
            continue
        
        elif user in word:
            hiddenword = letterchanger(user, hiddenword, word)
            
        else:
            parts = organmaker(parts,cnt)
            cnt += 1
        
        guessed.add(user)
        showgame(parts)
        
        if not "_" in hiddenword:
            print(f"you won!, the word was: {" ".join(zapas)}")
            break
        if cnt == 6:
            print(f"game over, the word was: {" ".join(zapas)}")
            break
        print(" ".join(hiddenword))
        
        
        


if __name__ == "__main__":
    main()

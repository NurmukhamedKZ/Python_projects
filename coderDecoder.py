import string
import random

letters = " "+string.punctuation+string.digits+string.ascii_letters
letters = list(letters)
keys = letters.copy()
random.shuffle(keys)


while True:
    choice = input(f"code or decode? (c,d): ").lower()
    if choice == "c":
        user = input()
        output = ""
        for i in user:
            ind = letters.index(i)
            output += keys[ind]
        print(f"original message: {user}")
        print(f"incrypted message: {output}")
    elif choice == "d":
        user = input()
        output = ""
        for i in user:
            ind = keys.index(i)
            output += letters[ind]
        print(f"incrypted message: {user}")
        print(f"original message: {output}")
    elif choice == "q":
        break
    else:
        print("invalid")
    

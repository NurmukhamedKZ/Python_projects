import random

def show_word(mas):
    answer = ""
    for i in mas:
        answer += i+" "
    return answer

words = ["apple",
         "hello"]

word = list(random.choice(words))
showword = ["#"]*len(word)
yellowwords = set()

attempts = 7

while True:
    attempts -= 1
    if attempts == 0:
        print("you lose!")
        break
        
    print(show_word(showword))
    user_word = input("enter a word: ").lower()
    if len(user_word) != len(word):
        print(f"write a word with the length of {len(word)}")
        attempts+=1
        continue
    for i in range(len(word)):
        if user_word[i] == word[i]:
            showword[i] = user_word[i]
        elif user_word[i] in word:
            yellowwords.add(user_word[i])

    print("--------------------------")
    print(f"you have {attempts} attempts")
    print(f"the word has: {yellowwords if len(yellowwords)>0 else "Nothing"}")
    if show_word(user_word) == show_word(word):
        print(f"you won!\nthe word was: {show_word(word)}")
        break

        
            
        
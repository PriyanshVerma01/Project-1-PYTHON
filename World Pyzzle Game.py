 # Word Puzzle Game

import random

def startgame():
    words_list = ["Father","Break","Ineuron","Green","Aroplane","Mysirg","Python","Programming"]

    Usedword = set()
    points = 0
    i=1
    while i<=5:
        word = random.choice(words_list)
        word = word.upper()

        if word in Usedword:
            continue

        Usedword.add(word)
        computer_word = word
        
        
        word = ''.join(random.sample(word,len(word))) 
        
        print(word)

        user_word = input("Arrange the letters to form a valid word: : ")

        if user_word.upper()==computer_word:
            points+=1
            print("Correct.")
        else:
            print("Wrong  : ")
            print("Correct Word is : = ",computer_word)
        print("Your score is : ",points)
        print()
        i+=1
    print("Game Finish")
    print()
    print(" Net score is : ", points)
    print()
    print("Thanks for playing this game.")




def main():

    inp = input("Enter any key except (Y/N) to start the game : ")

    if inp in ('n',"N"):
        print("You don't want to start the game")
        return
    
    elif inp in ('y',"Y"):
        print("You Want to start the game")
    
    startgame()


main()
# write a game function that stores the higest score in the file and display the score 

import random

def game():
    computer = random.randint(1, 3)
    chances = 3
    score = 0
    
    while chances > 0:
        user = int(input("choose the number between 1 - 10: "))
        if user == computer:
            print("you wone !")
            score = (10 - (3-chances) )*10
            break
        elif user > 10:
            print("The number must be in between 1 to 10")
            pass
        else:
            print(f"you loose remanind chances {chances - 1}")
            if user > computer:
                print("too high")
            else:
                print("too low")
        chances -= 1
    print(f"Correct number is {computer}")
    print(f"your score is {score}")

    try:
        with open("highscore.txt") as file:
            highscore = int(file.read())
    except:
        highscore = 0
    # compare the old and new high score 
    if score > highscore:
        print("You break the record")
        with open("highscore.txt" , "w") as file:
            file.write(str(score))

    else:
        print(f"highest score till yet is {highscore}")


            
game()
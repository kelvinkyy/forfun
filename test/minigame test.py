import random
import numpy as np

def getHand(temp):
    if temp == 1:
        return "rock"
    elif temp == 2:
        return "scissors"
    else:
        return "paper"

def getResult(computer,user):
    if computer == "rock":
        if user == "scissors":
            return "computers won"
        elif user == "paper":
            return "you won"
        elif user == "rock":
            return "draw"
    elif computer == "scissors":
        if user == "scissors":
            return "draw"
        elif user == "paper":
            return "computers won"
        elif user == "rock":
            return "you won"
    else:
        if user == "scissors":
            return "you won"
        elif user == "paper":
            return "draw"
        elif user == "rock":
            return "computers won"

def main():
    score = np.array([])
    repeat = True
    while True:
        print("1. start game")
        print("2. show score")
        print("3. exit")
        menu = int(input("option: "))

        if menu == 1:
            while repeat == True:
                while True:
                    print("1 = rock, 2 = scissors, 3 = paper")
                    hand = int(input("ENTER YOUR HAND: "))
                    if hand == 1 or hand == 2 or hand == 3:
                        break
                    else:
                        print("INVALID INPUT")
                hand = getHand(hand)

                result = getResult(getHand(random.randint(1,3)),getHand(hand))
                print(result)
                score = np.append(score,result)
                again = input("again? [Y/N]").lower()
                if again == "y":
                    repeat = True
                else:
                    repeat = False

        elif menu == 2:
            for i in range(len(score)):
                print(score[i])
        else:
            exit()
main()

from logging import exception
import random



while True:
    print("----------WELCOME TO THE STONE, PAPER, SISSORS GAME-----------\n")
    n = int(input("enter how many times you want to play: "))
    s1 = 0
    s2 = 0
    i = 0
    try:
        while i < n:
            li = ["Stone", "Paper", "Sissors"]
            a = random.choice(li)
            print("\nSELECT ONE\n\nstone\npaper\nsissors\n")
            x = str(input("what will you choose: "))
            c = x.capitalize()

            if c == "Stone":
                print("\ncomputer choose:", a, "\n")
                if a == "Stone":
                    print(
                        f"the game is draw no-one get a score, your total score is {s1}, and computer score is {s2}")
                elif a == "Paper":
                    s2 = s2+1
                    print(
                        f"you lose, comp got +1, your total score is {s1}, and computer score is {s2}")
                elif a == "Sissors":
                    s1 = s1+1
                    print(
                        f"you win, you got +1, your total score is {s1}, and computer score is {s2}")
                else:
                    print("wrong input, please try again!!")

            elif c == "Paper":
                print("\ncomputer choose:", a, "\n")
                if a == "Stone":
                    s1 = s1+1
                    print(
                        f"you win, you got +1, your total score is {s1}, and computer score is {s2}")
                elif a == "Paper":
                    print(
                        f"the game is draw no-one get a score, your total score is {s1}, and computer score is {s2}")
                elif a == "Sissors":
                    s2 = s2+1
                    print(
                        f"you lose, comp got +1, your total score is {s1}, and computer score is {s2}")
                else:
                    print("wrong input, please try again!!")

            elif c == "Sissors":
                print("\ncomputer choose:", a, "\n")
                if a == "Stone":
                    s2 = s2+1
                    print(
                        f"you lose, comp got +1, your total score is {s1}, and computer score is {s2}")
                elif a == "Paper":
                    s1 = s1+1
                    print(
                        f"you win, you got +1, your total score is {s1}, and computer score is {s2}")
                elif a == "Sissors":
                    print(
                        f"the game is draw no-one get a score, your total score is {s1}, and computer score is {s2}")
                else:
                    print("wrong input, please try again!!")
            else:
                print("wrong input, please try again!!")
            i = i+1

        if s1 < s2:
            print(
                f"\nyour total score is {s1}, and computer score is {s2} so the computer WINS and you LOOSE\n")

        elif s1 == s2:
            print(
                f"\nyour total score is {s1}, and computer score is {s2} so no-one WINS\n")

        else:
            print(
                f"\nyour total score is {s1}, and computer score is {s2} so you WINS and computer LOOSE\n")

    except exception as e:
        print(e)

    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("\ninvalid input.\n")
    if answer == 'y':
        continue
    else:
        print("\nGoodbye, come again!!!\n")
        break

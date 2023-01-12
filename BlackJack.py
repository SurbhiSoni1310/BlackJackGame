from art import logo
import random
import os
from time import sleep

continue_loop = True


def check_total(user_total, comp_total):
    if user_total == 21 and comp_total != 21:
        print("Congrats! You won")
        sleep(12)
    elif comp_total == 21 and user_total != 21:
        print("You lost")
        sleep(12)
    elif comp_total > user_total:
        print("You Lost")
        sleep(12)
    elif comp_total < user_total:
        print("Congrats! You win")
        sleep(12)
    elif comp_total == user_total:
        print("It's a Draw")
        sleep(12)
    else:
        print("You Lost, Both exceed 21")
        sleep(12)


def check_twenty_one(user_total, comp_total, user, computer):
    if comp_total > 21 > user_total:
        print(f"Computer's final hand : {computer} and computer's score is {comp_total}")
        print(f"Your cards are : {user} and your final score is {user_total}")
        print("You win! Computer exceeded")
        sleep(12)
        return True
    elif comp_total < 21 < user_total:
        print(f"Computer's final hand : {computer} and computer's score is {comp_total}")
        print(f"Your cards are : {user} and your final score is {user_total}")
        print("You Lost. You exceeded")
        sleep(12)
        return True
    else:
        return False


def BlackJack():
    print(logo)
    list1 = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print("Welcome to the BlackJack Game")
    print("Rules : Make the cards sum closer to 21 or 21")
    computer = []
    user = []
    computer = random.sample(list1, 2)
    user = random.sample(list1, 2)
    user_total = sum(user)
    comp_total = sum(computer)
    check = check_twenty_one(user_total, comp_total, user, computer)
    if check:
        return
    else:
        print(f"Your cards are : {user} and your current score is {user_total}")
        print(f"Computer's first card is : " + str(computer[0]))
        want_more_card = True
        while want_more_card:
            choice = input("Do you want a new card ? Type 'yes' or want to pass, Type 'no' : ").lower()
            if choice == "yes":
                new = random.choice(list1)
                user.append(new)
                user_total = sum(user)
                check = check_twenty_one(user_total, comp_total, user, computer)
                if check:
                    want_more_card = False
                else:
                    print(f"Your cards are : {user} and your current score is {user_total}")
                    print(f"Computer's first card is : " + str(computer[0]))
            elif choice == "no":
                print(f"Your cards are : {user} and your current score is {user_total}")
                while comp_total <= 17:
                    extra = random.choice(list1)
                    computer.append(extra)
                    comp_total = sum(computer)
                print(f"Computer's final hand : {computer} and computer's score is {comp_total}")
                check_twenty_one(user_total, comp_total, user, computer)
                check_total(user_total, comp_total)
                want_more_card = False
            else:
                print("Wrong Input. Program Terminated")
                exit(1)


while continue_loop:
    option = input("Do you want to play the BlackJack Game ('y'/'n') : ").lower()
    if option == "y":
        BlackJack()
        os.system('cls')
    elif option == "n":
        continue_loop = False
        print("GoodBye.")
        sleep(12)
    else:
        print("Wrong input. Program Terminated")
        sleep(12)
        continue_loop = False

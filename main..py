import random
import datetime

time = datetime.datetime.now()

chance = 10
no_of_chance = 0
com_score = 0
user_score = 0
print("Rock Paper Scissors Game:\n")
print(time)
game_items = ["rock", "paper", "scissors"]
print("choose one item\n")

while no_of_chance < chance:
    _input = input("r for rock, p for paper and s for scissors\n").upper()
    _random_item = random.choice(game_items)
    print(_random_item)

    if _input == "P" and _random_item == "scissors":
        com_score += 1
        print(f"computer score :{com_score}, your score : {user_score}\n")
        print("COMPUTER WINS")

    elif _input == "P" and _random_item == "paper":
        print("IT'S DRAW")

    elif _input == "P" and _random_item == "rock":
        user_score += 1
        print(f"your score :{user_score}, computer score : {com_score}\n")
        print("YOU WIN")

    elif _input == "R" and _random_item == "paper":
        com_score += 1
        print(f"computer score :{com_score}, your score : {user_score}\n")
        print("COMPUTER WINS")

    elif _input == "R" and _random_item == "rock":
        print("IT'S DRAW")

    elif _input == "R" and _random_item == "scissors":
        user_score += 1
        print(f"your score :{user_score}, computer score : {com_score}\n")
        print('YOU WIN')

    elif _input == "S" and _random_item == "rock":
        com_score += 1
        print(f"computer score :{com_score}, your score : {user_score}\n")
        print("COMPUTER WINS")

    elif _input == "S" and _random_item == "scissors":
        print("IT'S DRAW")

    elif _input == "S" and _random_item == "paper":
        user_score += 1
        print(f"your score :{user_score}, computer score : {com_score}\n")
        print('YOU WIN\n')

    else:

        print("YOU ENTERED A INVALID INPUT")

    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance} is left out of {chance}\n")

print("Game Over")

if com_score > user_score:
    print("computer wins and you lost the game")

if com_score < user_score:
    print("you won the game and computer lost the game")
if com_score == user_score:
    print("your and computer score is equal so the game is draw")

print(f"your score is {user_score}, computer score is {com_score}")

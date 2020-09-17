# Write your code here
import random

options = {'scissors': 'rock', 'paper': 'scissors', 'rock': 'paper'}


def get_rating(name):
    rate = open('animals.txt', 'r')
    names_and_scores = [i.split() for i in rate.readlines()]
    user_score = 0
    for i in names_and_scores:
        if name in i:
            user_score = i[1]
    print(f'Your rating: {user_score}')
    rate.close()
    return user_score


while True:
    user_name = input('Enter your name:')
    user_chose = input()
    pc_chose = random.choice(list(options.keys()))
    if user_chose == '!exit':
        print('Bye')
        break
    elif user_chose == '!rating':
        get_rating(user_name)
    elif user_chose not in options.keys():
        print("Invalid input")
        continue
    elif user_chose == pc_chose:
        print(f'There is a draw ({pc_chose})')
    elif options[user_chose] != pc_chose:
        print(f"Well done. The computer chose {pc_chose} and failed")
    else:
        print(f"Sorry, but the computer chose {pc_chose}")

# Write your code here
import random

options = {'scissors': ['rock'], 'paper': ['scissors'], 'rock': ['paper']}
extra_options = {'scissors': ['spock', 'rock', 'water', 'dragon', 'devil', 'lightning', 'gun'],
                 'fire': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
                 'paper': ['scissors', 'lizard', 'fire', 'snake', 'human', 'tree', 'wolf', 'sponge'],
                 'rock': ['paper', 'spock', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
                 'gun': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
                 'lightning': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
                 'devil': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
                 'dragon': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
                 'water': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
                 'air': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
                 'sponge': ['rock', 'scissors', 'lizard', 'fire', 'snake', 'human', 'tree', 'wolf'],
                 'wolf': ['gun', 'rock', 'scissors', 'lizard', 'fire', 'snake', 'human', 'tree'],
                 'tree': ['lightning', 'gun', 'rock', 'scissors', 'lizard', 'fire', 'snake', 'human'],
                 'human': ['devil', 'lightning', 'gun', 'rock', 'scissors', 'lizard', 'fire', 'snake'],
                 'snake': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'scissors', 'lizard', 'fire']
                 }


def get_rating(name):
    rate = open('rating.txt', 'r')
    names_and_scores = [i.split() for i in rate.readlines()]
    user_score = 0
    for i in names_and_scores:
        if name in i:
            user_score = i[1]
    print(f'Your rating: {user_score}')
    rate.close()
    return user_score


def update_rating(name, score):
    rate = open('rating.txt', 'r')
    names_and_scores = []
    for name in rate:
        names_and_scores += name.split()
    rate.close()

    if user_name in names_and_scores:
        new_score = names_and_scores[names_and_scores.index(user_name) + 1]
        names_and_scores[names_and_scores.index(user_name) + 1] = str(int(new_score) + score)
    else:
        names_and_scores += [user_name, str(score)]

    write_to_rating = open('rating.txt', 'w')
    for i in range(0, len(names_and_scores)):
        if i % 2 == 0:
            print(names_and_scores[i], file=write_to_rating, end=' ')
        else:
            print(names_and_scores[i], file=write_to_rating)
    write_to_rating.close()


user_name = input('Enter your name:')
print(f"Hello, {user_name}")
list_of_options = input()

if list_of_options != '':
    options = extra_options.copy()
print("Okay, let's start")
while True:
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
        update_rating(user_name, 50)
    elif pc_chose not in options[user_chose]:
        print(f"Well done. The computer chose {pc_chose} and failed")
        update_rating(user_name, 100)
    else:
        print(f"Sorry, but the computer chose {pc_chose}")

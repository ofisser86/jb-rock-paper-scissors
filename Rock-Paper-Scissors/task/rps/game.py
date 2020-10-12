# Let the game begin
import os
import random

# Define path for store rating in rating txt
ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)
rating_path = os.path.join(BASE_DIR, 'rating.txt')

def prRed(skk): return "\033[31m {}\033[00m" .format(skk)
def prGreen(skk): return "\033[92m {}\033[00m" .format(skk) 
def prYellow(skk): return "\033[93m {}\033[00m" .format(skk)
def prLightPurple(skk): return "\033[94m {}\033[00m" .format(skk) 
def prPurple(skk): return "\033[95m {}\033[00m" .format(skk) 
def prCyan(skk): return "\033[96m {}\033[00m" .format(skk)
def prLightGray(skk): return "\033[97m {}\033[00m" .format(skk) 
def prBlack(skk): return"\033[98m {}\033[00m" .format(skk)
def prLightRed(skk): return "\033[91m {}\033[00m" .format(skk)
def prBlue(skk): return "\033[34m {}\033[00m" .format(skk)
def prOrange(skk): return "\033[33m {}\033[00m" .format(skk)
def prPink(skk): return "\033[95m {}\033[00m" .format(skk)

# Two levels of games - Classic and Hard
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

# read the file rating.txt and get user rating by  name file locate in the same direcory
def get_rating(name):
    rate = open(rating_path, 'r')
    names_and_scores = [i.split() for i in rate.readlines()]
    user_score = 0
    for i in names_and_scores:
        if name in i:
            user_score = i[1]
    print('\nYour rating: ' + prYellow(f'{user_score}'))
    rate.close()
    return user_score

# read the file rating.txt and update rating file locate in the same direcory
def update_rating(name, score):
    rate = open(rating_path, 'r')
    names_and_scores = []
    for name in rate:
        names_and_scores += name.split()
    rate.close()

    if user_name in names_and_scores:
        new_score = names_and_scores[names_and_scores.index(user_name) + 1]
        names_and_scores[names_and_scores.index(user_name) + 1] = str(int(new_score) + score)
    else:
        names_and_scores += [user_name, str(score)]

    write_to_rating = open(rating_path, 'w')
    for i in range(0, len(names_and_scores)):
        if i % 2 == 0:
            print(names_and_scores[i], file=write_to_rating, end=' ')
        else:
            print(names_and_scores[i], file=write_to_rating)
    write_to_rating.close()


user_name = input('Enter your name: ')
print(f"\nHello, {user_name}\n")
print("""If you want to play""" + prBlue("classic") + """ game (rock, paper, scissors) - press enter,
if want to play""" + prOrange("extended") + """ game (secret), type  -> hardrock\n""")

list_of_options = input(">")

if list_of_options != '':
    options = extra_options.copy()
print(prCyan("{:^50}".format("Okay, let's start")))
while True:
    print(prPurple("\nOptions") + " in " + f"{'Classic' if len(options) == 3 else 'HardRock'} game: " + prGreen(", ".join([i for i in options.keys()])))
    user_chose = input("""\nChose one from the options above or
    press""" + prLightPurple('!rating') + """ for get rating or
    press""" + prYellow('!change') + """ for change game level
    press""" + prRed('!exit')   + """ for exit the game\n> """)
    pc_chose = random.choice(list(options.keys()))
    if user_chose == '!exit':
        print('Bye')
        break
    elif user_chose == '!rating':
        get_rating(user_name)
    elif user_chose == '!change':
        options = extra_options.copy()
        print("\nLevel was changed!")
    elif user_chose not in options.keys():
        print("\nInvalid input. Try again and be careful " + prRed("'Big brother is watching you' (^)-(^)"))
        continue
    elif user_chose == pc_chose:
        print(f"There is a draw (" + "computer chose " + prGreen(f"{pc_chose}") + "). You get 50 points of rating")
        update_rating(user_name, 50)
    elif pc_chose not in options[user_chose]:
        print(f"Well done. You won! The computer chose" + prGreen(f"{pc_chose}") + " and lost")
        print('Congrat`s your rating increase!')
        update_rating(user_name, 100)
    else:
        print(f"Sorry, this time you lost, the computer chose" + prGreen(f"{pc_chose}.") + " Try again!")
        update_rating(user_name, -50)

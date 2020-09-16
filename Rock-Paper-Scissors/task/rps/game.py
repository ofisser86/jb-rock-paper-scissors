# Write your code here
import random

options = {'scissors': 'rock', 'paper': 'scissors', 'rock': 'paper'}

while True:
    user_chose = input()
    pc_chose = random.choice(list(options.keys()))
    if user_chose == '!exit':
        print('Bye')
        break
    elif user_chose not in options.keys():
        print("Invalid input")
        continue
    elif user_chose == pc_chose:
        print(f'There is a draw ({pc_chose})')
    elif options[user_chose] != pc_chose:
        print(f"Well done. The computer chose {pc_chose} and failed")
    else:
        print(f"Sorry, but the computer chose {pc_chose}")

# Write your code here
import random

win = {'scissors': 'rock', 'paper': 'scissors', 'rock': 'paper'}
options = ['paper', 'scissors', 'rock']


user_chose = input()
# or could use list(win.keys())
pc_chose = random.choice(options)

if user_chose == pc_chose:
    print(f'There is a draw ({pc_chose})')
elif win[user_chose] != pc_chose:
    print(f"Well done. The computer chose {pc_chose} and failed")
else:
    print(f"Sorry, but the computer chose {pc_chose}")

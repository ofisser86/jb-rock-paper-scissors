# Write your code here
import random

options = ['rock', 'scissors', 'paper']

user_choose = input()
# random.seed(user_choose)
# pc_choose = random.choice(options)
answer = ''
if user_choose == 'rock':
    answer = 'paper'
elif user_choose == 'paper':
    answer = 'scissors'
else:
    answer = 'rock'
print(f'Sorry, but the computer chose {answer}')

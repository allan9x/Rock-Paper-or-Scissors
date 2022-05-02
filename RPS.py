import random

user_action = input('Enter a choice of rock, paper, or scissors: ')
possible_action = ['rock', 'paper', 'scissors']
computer_action = random.choice(possible_action)
print('You chose ' + user_action + ' and Computer chose ' + computer_action + '.')

if user_action.lower() == computer_action:
    print('Both players selected ' + user_action + ', hence it is a tie.')
elif user_action.lower() == 'rock':
    if computer_action == 'scissors':
        print('Rock beats scissors. You win.')
    else:
        print('Paper beats rock. You lose')

elif user_action.lower() == 'scissors':
    if computer_action == 'paper':
        print('Scissors beats paper. You win.')
    else:
        print('Rock beats scissors. You lose.')

elif user_action.lower() == 'paper':
    if computer_action == 'rock':
        print('Paper beats rock. You win.')
    else:
        print('Scissors beats paper. You lose.')
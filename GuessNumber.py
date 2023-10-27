import random

random_number = random.randint(0,10)
print('< ----- Guess Number  ----- >')
print('It\'s a number guessing gaming where you have to guess number between 0 to 10.')
guess = 0

while guess != random_number:
    guess = int(input('Entre you guess: '))
    if guess < random_number:
        print('Guess Higher.')
    elif guess > random_number:
        print('Guess lower.')
    else:
        print('you won......congrulation!')

import random

hand = ['rock', 'paper', 'scissor']
sign = random.randint(0,2)
computer_score = 0
player_score = 0

while True:
    player = str(input('\n(Rock, Paper, Scissor, Quit)\nChoise your hand sign: ')).lower()
    if player == 'quit':
        print('Come again next Time..')
        quit()
    if player not in hand:
        print('Invalid Input...')
        continue

    computerPick = hand[sign]
    print('Computer pick ', computerPick + '.')

    if player == 'rock' and computerPick == 'scissor':
        print('You Won.... Congrulation.')
        player_score += 1

    elif player == 'paper' and computerPick == 'rock':
        print('You Won.... Congrulation.')
        player_score += 1
    
    elif player == 'scissor' and computerPick == 'paper':
        print('You Won.... Congrulation.')
        player_score += 1

    elif player == 'paper' and computerPick == 'paper':
        print('It is a draw.')

    elif player == 'scissor' and computerPick == 'scissor':
        print('It is a draw.')

    elif player == 'rock' and computerPick == 'rock':
        print('It is a draw.')

    else:
        print('Computer Win.')
        computer_score += 1

    print('Your Score is: ',player_score)
    print('Computer Score is: ',computer_score)

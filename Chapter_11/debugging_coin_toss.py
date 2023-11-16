import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss==0:
    turn='tails'
else:
    turn='heads'
if turn == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input().lower()
    if turn == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
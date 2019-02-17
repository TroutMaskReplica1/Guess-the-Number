import random

i = 1

guess = int(input('Guess a number '))
x = random.randint(1, 10)
while i < 11:
    if guess == x:
        print('Ya won! Only took ya {i} tries!')
        break
    elif i == 10:
        print("Too Slow Joe!")
        break
    else:
        guess2 = int(input('Guess again '))
        y = random.randint(1, 10)
        i += 1

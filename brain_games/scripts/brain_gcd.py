import prompt
import random
import math


def gcd():
    counter = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Find the greatest common divisor of given numbers.')
    while counter < 3:
        num = random.randint(1, 100)
        print(f'Question: {num} {num}')
        two_num = math.gcd(num, num)
        your = prompt.string('Your answer: ')
        if your == two_num:
            print('Correct!')
        else:
            return f"'{your}' is wrong answer ;(. Correct answer was ''.\nLet`s try again, {name}!"
    if counter == 3:
        print(f'Congratulations, {name}!')
print(gcd())

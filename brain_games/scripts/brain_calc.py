import prompt
import random

def calc():
    counter = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What is the result of the expression?')
    while counter < 3:
        oper = random.choice(['*', '+', '-'])
        num = random.randint(1, 100)
        print(f'Question: {num} {oper} {num}')
        your = prompt.string('Your answer: ')
        if your is True:
            print('Correct!')
        else:
            return f"{your} is wrong answer ;(. Correct answer was ''.\nLet`s try again, {name}"
    if counter == 3:
        print(f'Congratulations, {name}!')
print(calc())
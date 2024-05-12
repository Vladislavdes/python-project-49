import prompt
import random

def prime():
    num = random.randint(2, 100)
    counter = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    while counter < 3:
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        print(f'Question: {num}')
        your = prompt.string('Your answer: ')
        for i in range(2, int(num**0.5) + 1):
            if (num % i == 0 and your == 'yes') or (num % i != 0 and your == 'no'):
                print('Correct!')
            else:
                print(f"{your} is wrong answer ;(. Correct answer was ''.\nLet's try again, {name}")
    if counter == 3:
        print(f'Congratulations, {name}!')
    
print(prime())
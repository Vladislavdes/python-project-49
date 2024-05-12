import prompt
import random


def brain_even():
    counter = 0
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while counter < 3:
        num = random.randint(1, 101)
        print(f'Question: {num}')
        your_answer = prompt.string('Your answer:')
        if num % 2 == 0 and your_answer == 'yes':
            print('correct')
            counter += 1
            print(counter)
        elif num % 2 != 0 and your_answer == 'no':
            print('correct')
            counter += 1
            print(counter)
        else:
            return f"""'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!"""    
    if counter == 3:
        print(f'Congratulations, {name}!')
print(brain_even())

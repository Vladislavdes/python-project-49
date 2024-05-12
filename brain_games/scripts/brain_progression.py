import random
import prompt

def progression():
    counter = 0
    numbers = []
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('What number is missing in the progression?')
    num1 = random.randint(1, 10)
    num2 = random.randint(80, 100)
    num = random.randint(1, 10)
    while counter < 3:
        for i in range(num1, num2, num):
            numbers.append(i)
        numbers.sort
        numbers[random.randint(1, 9)] = '...'
        correct = numbers[random.randint(1, 9)]
        ques = ' '.join(map(str, numbers[0:10]))
        print(ques)
        your = prompt.string('Your answer: ')
        if your == correct:
            print('Correct')
        else:
            print(f"{your} is wrong answer ;(. Correct answer was ''.\nLet's try again, {name}")
    if counter == 3:
        print(f'Congratulations, {name}!')        
        
print(progression())
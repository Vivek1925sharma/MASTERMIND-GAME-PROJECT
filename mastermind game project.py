import random
import time

def mastermind():
    print("Welcome to mastermind game")
    print("The computer will generate a four digit code")
    print("You will have 10 chances to guess the code")
    print("If you guess a correct number in the correct position, you will get a '+'")
    print("If you guess a correct number in the wrong position, you will get a '-'")
    print("If you guess a wrong number, you will get a ''. ")
    print("Good Luck!!")

    time.sleep(2)
    print('Generating Code...')
    time.sleep(2)
    print("")
    code = []
    for i in range(4):
        code.append(random.randint(1,6))
    print('Code generated')
    print('')
    time.sleep(1)
    print('You have 10 chances to guess the code.')
    print('')
    time.sleep(1)
    print("Enter your guess:")
    print('')
    time.sleep(1)
    for i in range(10):
        guess = input()
        guess = list(guess)
        guess = [int(i) for i in guess]
        if guess == code:
           print('You Win!!')
           break
        else:
            print('')
            print('Guess again..')
            print('')
            time.sleep(1)
            print('Enter your guess')
            print('')
            time.sleep(1)
            print('')
            print('Hint: ')
        for j in range(4):
            if guess[j] == code[j]:
                print("+", end="")
            elif guess[j] in code:
                print('-', end="")
            else:
                print(" ", end="")
        print('')
        print('')
        time.sleep(1)
    if guess!=code:
        print("You lose.!!")
        print('The code was: ')
        print(code)

mastermind()




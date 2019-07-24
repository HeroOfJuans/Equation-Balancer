from equation import Equation
from time import sleep
import random

#object for the defined equation class
def run_balance():
    #prompts user to input a chemical equation and gives them correct format
    print('=================================================')
    print('Insert chemical equation with elements in parentheses followed by the number of atoms:')
    print('Example: (H)2 + (O)2 = (H)2(O)1')
    user_input = input('>>> ')
    #checks to see if the input matches the correct format and runs the balancing function
    try:
        equation = Equation(user_input)
        print('Balanced equation: ' + equation.balance())
        sleep(3)
        run_balance()
    #if input is not correctly formated then it will return as invalid input and ask the player again
    except IndexError:
        print('Invalid input...')
        sleep(3)
        run_balance()
def checker(v):
    user_input = v

    equation = Equation(user_input)
    return equation


def practice(): #doesnt work
    print('Welcome to the chemical equation practice tool.')
    f = open('samples.txt', 'r')
    samples_list = []
    print('Enter a number between 1 and 5 to fetch a problem to solve')
    sample_search = input()
    for row in f:
        (k, v) = row.split(':', 1)
        if k == sample_search:
            print(v)
            unbalanced = v
            print('Try to balance this equation. Your answer\nshould look something like this\n2H2 + O2 = 2H2O ')
            attempt = input()
            equation = Equation(v)
            correct = equation.balance()
            if correct == attempt:
                print('Well done! That is the correct answer!')
                print('Would you like to try another problem? Enter 1 for yes 2 for no.')
                answer = input()
                if answer == '1':
                    practice()
                if answer == 2:
                    print('Thanks for practicing!')
                    input()
            if equation != attempt:
                print('Oops... that isn\'t correct.. But heres the correct one...')
                print(correct)


    f.close()
print('Enter 1 to use the calculator or enter 2 to use the practice tool.')
responce = input()
if responce == '1':
    run_balance()
if responce == '2':
    practice()

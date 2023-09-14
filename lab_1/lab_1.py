
"""
Gluhovskoy Nikita 62 group
Exercise 1-1. Write a simple game guess the number.
The program will randomly choose a number within the specified range and will
wait for the user to input a number. If the number is smaller or greater than
that chosen by the program, the system tells that to the user. If the guessed
number is correct, then the game is over and the program displays the number of
iterations taken.
Exercise 1-2. Write a recursive function that computes factorial
Exercise 1-3. Write a function computing the average from arbitrary numbers
of an argument.
Exercise 1-4. Write a function adding two numbers in the following manner:
add(1)(2) == 3
Exercise 1-5. Write a decorator that computes the execution time
of the decorated function
Exercise 1-6. Write a function that computes a large factorial using multiple
threads using function from 1-2
"""


import logging
import time

import lab_1_modules

logging.basicConfig(level=logging.NOTSET, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()


def start():
    selected_action = None
    average = 0
    loop = True
    while loop:
        print('Hello, select an action\n'
              '1) Guessing_game\n'
              '2) Search Factorial of number\n'
              '3) Calculate Average\n'
              '4) Add two numbers\n'
              '5) Check the execution time of the function\n'
              '6) Search Big Factorial\n'
              '7) Exit')
        try:
            selected_action = int(input())
            if selected_action < 1 or selected_action > 7:
                logger.warning('Enter a number from 1 to 7')
                continue
        except ValueError:
            logger.error('Incorrect data')
        if selected_action == 1:
            lab_1_modules.guessing_game()
        elif selected_action == 2:
            lab_1_modules.search_fact()
        elif selected_action == 3:
            number_list = []
            print('Input the number of items')
            try:
                number = int(input())
            except ValueError:
                logger.error('Incorrect data')
                continue
            print('Input items')
            try:
                for _ in range(number):
                    number_list.append(float(input()))
                average = lab_1_modules.find_average(*number_list)
                print(f'Average value equal {average}')
            except ValueError:
                logger.error('Incorrect data')
        elif selected_action == 4:
            try:
                first_number = float(input('Input first number\n'))
                second_number = float(input('Input second number\n'))
                result = lab_1_modules.sum_func(first_number)(second_number)
                print(f'Sum equal {result}')
            except ValueError:
                logger.error('Incorrect data')
                continue
        elif selected_action == 5:
            decorated_timer_func = lab_1_modules.timer_func(example_timer_func)
            decorated_timer_func()
        elif selected_action == 6:
            try:
                number = int(input('Enter your number\n'))
                number_threads = int(input('Enter number of threads\n'))
            except ValueError:
                logger.error('Incorrect data')
                continue
            result = lab_1_modules.threading_fact(number, number_threads)
            try:
                print(f"\nFactorial of the entered number: {result}")
            except ValueError:
                logger.error('The result is too long (max 4300 digits)')
        elif selected_action == 7:
            print('Goodbye!')
            loop = False


def example_timer_func():
    time.sleep(2)


start()

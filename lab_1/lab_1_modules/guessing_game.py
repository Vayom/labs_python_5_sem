from .logger_module import logger
import random


def guessing_game() -> None:
    attempts = 0
    left_border = 0
    right_border = 10
    print("Game Started\n"
          "Enter the left and right boundaries of the range")
    loop = True
    while loop:  # A loop for the possibility of changing boundaries

        try:
            left_border = int(input('Enter left border\n'))
            right_border = int(input('Enter right border\n'))
            if left_border >= right_border:
                logger.warning('The left border should be smaller than the right one')
            else:
                loop = False
        except ValueError:
            logger.error('Incorrect data\n'
                         'Enter integers')

    logger.info(f'Your range [{left_border};{right_border}]')
    hidden_number = random.randint(left_border, right_border)
    logger.info('The number is hidden')

    chosen_number = None
    while chosen_number != hidden_number:
        try:
            chosen_number = int(input('Input your number\n'))
            attempts += 1
            if chosen_number < left_border or chosen_number > right_border:
                logger.info('The number does not fall within the range')
            elif chosen_number > hidden_number:
                logger.info('The selected number is greater than the desired one')
            elif chosen_number < hidden_number:
                logger.info('The selected number is less than the desired one')
        except ValueError:
            logger.error('Incorrect data')

        if chosen_number == hidden_number:
            print(f"Congratulations, you guessed it in {attempts} attempts")
        else:
            print("Try again!")

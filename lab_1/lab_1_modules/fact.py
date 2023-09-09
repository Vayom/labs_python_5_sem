from .logger_module import logger


def factorial(number: int, start=0) -> int:
    """
    A function that calculates the factorial of a number

    :parameter
        number: int - the number relative to which the factorial is calculated
        start: int - the minimum number in the product of the factorial
    :return
        int - factorial of number
    """
    try:
        if number > 1 and number != start:
            return number * factorial(number - 1, start)
        else:
            if start == 0:
                return 1
            else:
                return start
    except RecursionError:
        return 0


# Task 2: factorial search
def search_fact() -> None:
    """
    UI for calculate factorial function
    """
    user_number = None
    result = None
    logger.info('This program calculates the factorial of a number')
    loop = True
    while loop:
        try:
            user_number = int(input("Enter your number: "))
            if user_number < 0:
                logger.warning('The number must be greater than 0')
            else:
                try:  # Attempt calculate factorial
                    result = factorial(user_number)
                    if result == 0:
                        logger.error('Maximum recursion depth exceeded in comparison')
                    loop = False
                except RecursionError as error:
                    logger.error(f'{error}')
                except MemoryError as error:
                    logger.error(f'{error}')
        except ValueError:
            logger.error('Incorrect data')

    print(f"\nFactorial of the entered number: {result}")

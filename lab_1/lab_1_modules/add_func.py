from .logger_module import logger


def sum_func(x: float):
    """
    Outer function for sum two numbers. It's using inner function

    :param x: int - first number for sum
    :return: inner function
    """
    def add_inner(y: float) -> int:
        """

        :param
            y: int - second number for sum
        :return:
            int - result of sum
        """
        result = None
        try:
            result = x + y
            return result
        except TypeError:
            logger.error('Incorrect data')

    return add_inner

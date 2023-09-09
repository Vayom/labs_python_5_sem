from .logger_module import logger


def find_average(*args: float) -> float:
    """

    :param args: float - elements for calculating the average
    :return: float - average value
    """
    result = 0
    if not args:
        logger.warning('It is impossible to find the average of zero elements')
        return 0
    try:
        total = sum(args)
        average = total / len(args)
        return average
    except TypeError:
        logger.error('Incorrect data')
        return 0

import time
from .logger_module import logger


def timer_func(func):
    """
    Decorator which calculate time of work the function
    :param func:  which decorated
    :return: a wrapper that calculates time
    """
    def wrapper(*args, **kwargs):
        """
        A wrapper that calculates time
        :param args:
        :param kwargs:
        :return(float): work time of func
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logger.info(f"Время выполнения для {func.__name__}: {execution_time} секунд")
        return result

    return wrapper

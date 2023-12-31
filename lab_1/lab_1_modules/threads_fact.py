import threading
from .fact import factorial
from .logger_module import logger
from lab_1.lab_1_modules.decorator_class import ProfileDecorator


@ProfileDecorator
def compute_chunk(start_num, end_num, result_list):
    result_fact = factorial(start=start_num, number=end_num)
    result_list.append(result_fact)


def threading_fact(number: int, num_threads: int) -> int:
    """

    :param number: int - the number relative to which the factorial is calculated
    :param num_threads: numbers of threads
    :return int: result_fact of factorial
    """
    if number < num_threads:
        num_threads = number  # Make sure that the number of threads is no more than n
        logger.warning('The number of threads is greater than the number of recursive iterations')

    if num_threads <= 0:
        logger.warning(f'The number of threads must be greater than 0')
    else:
        chunk_size = (number - num_threads) // num_threads  # Divide the calculations into parts for each thread
        threads = []
        results = []

        start = 1
        for _ in range(num_threads):
            end = start + chunk_size
            if end > number:
                end = number
            thread = threading.Thread(target=compute_chunk, args=(start, end, results))
            threads.append(thread)
            start = end + 1

        # Starting streams
        for thread in threads:
            thread.start()

        # Waiting for all threads to finish
        for thread in threads:
            thread.join()

        # Combining the results
        total_result = 1
        for result in results:
            total_result *= result
        if total_result == 0:
            logger.error('Maximum recursion depth exceeded in comparison')

        return total_result

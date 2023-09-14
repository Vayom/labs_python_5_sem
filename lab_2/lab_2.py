import random
import time
import threading
import sys
import lab_1.lab_1_modules as l1

# Устанавливаем новый лимит глубины рекурсии (например, 10000)
sys.setrecursionlimit(100000000)


# Пример использования декоратора для функции пузырьковой сортировки
@l1.ProfileDecorator
def bubble_sort(arr):
    arr_len = len(arr)
    for row in range(arr_len):
        for col in range(0, arr_len - row - 1):
            if arr[col] > arr[col + 1]:
                arr[col], arr[col + 1] = arr[col + 1], arr[col]


def parallel_bubble_sort(arr, num_threads):
    # Разбиваем массив на сегменты для каждого потока
    segment_size = len(arr) // num_threads
    segments = [arr[item:item + segment_size] for item in range(0, len(arr), segment_size)]

    threads = []

    # Создаем и запускаем потоки для сортировки каждого сегмента
    for segment in segments:
        thread = threading.Thread(target=bubble_sort, args=(segment,))
        thread.start()
        threads.append(thread)

    # Ждем завершения всех потоков
    for thread in threads:
        thread.join()

    # Объединяем сегменты в один отсортированный массив
    sorted_arr = []
    for segment in segments:
        sorted_arr.extend(segment)

    # Завершаем сортировку для окончательной уверенности
    bubble_sort(sorted_arr)

    return sorted_arr


@l1.ProfileDecorator
def run_factorial(n):
    return l1.factorial(n)


array_size = 1000

random_array = [random.randint(0, array_size) for _ in range(array_size)]
# Stats for bubble
bubble_sort(random_array)
bubble_sort_stats = bubble_sort.stats()
print("Buble sort Execution Time:", bubble_sort_stats["total_execution_time"])
print("Buble sort Call Count:", bubble_sort_stats["call_count"])

# Stats for threads bubble
bubble_sort.call_count = 0
parallel_bubble_sort(random_array, 2)
threads_bubble_sort_stats = bubble_sort.stats()
print("Threads Buble sort Execution Time:", threads_bubble_sort_stats["total_execution_time"])
print("Threads Buble sort Call Count:", threads_bubble_sort_stats["call_count"])

result = run_factorial(100000)
# Stats for fact
factorial_stats = run_factorial.stats()
print("Factorial Execution Time:", factorial_stats["total_execution_time"])
print("Factorial Call Count:", factorial_stats["call_count"])

result2 = l1.threading_fact(100000, 2)
# Stats for threads fact
factorial_stats2 = l1.compute_chunk.stats()
print("Threads Factorial Execution Time:", factorial_stats2["total_execution_time"])
print("Threads Factorial Call Count:", factorial_stats2["call_count"])

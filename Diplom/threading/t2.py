import asyncio
import threading
import multiprocessing
import time
import random


def cpu_bound_task(num):
    """CPU-bound задача, симулирующая сложные вычисления.

    Args:
        num: Число, используемое в вычислениях.

    Returns:
        Результат умножения числа на 2.
    """
    for _ in range(10**7 * num):
        random.random() * random.random()
    return num * 2


async def async_cpu_bound_task(num):
    """Асинхронная обёртка для CPU-bound задачи.

    Args:
        num: Число, используемое в вычислениях.

    Returns:
        Результат выполнения cpu_bound_task.
    """
    return cpu_bound_task(num)


def main():
    """Основная функция для сравнения производительности multiprocessing, threading и asyncio."""
    nums = list(range(1, 5))

    """Multiprocessing"""
    start_time = time.time()
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        multiprocessing_results = pool.map(cpu_bound_task, nums)
    end_time = time.time()
    print(f"Multiprocessing time: {end_time - start_time:.4f} seconds")

    """Threading"""
    start_time = time.time()
    threads = []
    threading_results = []
    for num in nums:
        thread = threading.Thread(target=lambda n=num: threading_results.append(cpu_bound_task(n)), args=())
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Threading time: {end_time - start_time:.4f} seconds")

    """Asyncio"""
    start_time = time.time()
    async_results = asyncio.run(asyncio.gather(*(async_cpu_bound_task(num) for num in nums)))
    end_time = time.time()
    print(f"Asyncio time: {end_time - start_time:.4f} seconds")

    print("Multiprocessing results:", multiprocessing_results)
    print("Threading results:", threading_results)
    print("Asyncio results:", async_results)


if __name__ == "__main__":
    main()
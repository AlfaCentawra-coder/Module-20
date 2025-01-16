import asyncio
import threading
import multiprocessing
import time
import os
import random


def cpu_bound_task(n):
    """CPU-bound задача, симулирующая сложные вычисления.

    Args:
        n: Количество итераций для вычислений.

    Returns:
        Результат вычислений.
    """
    result = 1
    for _ in range(n * 10**7):
        result *= (1 + random.random() / 10000000)
    return result


async def async_cpu_bound_task(n):
    """Асинхронная обёртка для CPU-bound задачи (без реального параллелизма).

    Args:
        n: Количество итераций для вычислений.

    Returns:
        Результат вычислений.
    """
    return cpu_bound_task(n)


def main():
    """Основная функция для сравнения производительности multiprocessing, threading и asyncio."""
    iterations = 4
    num_processes = os.cpu_count()

    """Multiprocessing"""
    start_time = time.time()
    with multiprocessing.Pool(processes=num_processes) as pool:
        mp_results = pool.map(cpu_bound_task, [iterations] * num_processes)
    end_time = time.time()
    print(f"Multiprocessing time: {end_time - start_time:.4f} seconds")

    """Threading"""
    start_time = time.time()
    threads = []
    th_results = []
    for _ in range(num_processes):
        thread = threading.Thread(target=lambda: th_results.append(cpu_bound_task(iterations)))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    end_time = time.time()
    print(f"Threading time: {end_time - start_time:.4f} seconds")

    """Asyncio"""
    start_time = time.time()
    async_results = asyncio.run(asyncio.gather(*(async_cpu_bound_task(iterations) for _ in range(num_processes))))
    end_time = time.time()
    print(f"Asyncio time: {end_time - start_time:.4f} seconds")

    print("Multiprocessing results:", mp_results)
    print("Threading results:", th_results)
    print("Asyncio results:", async_results)


if __name__ == "__main__":
    main()
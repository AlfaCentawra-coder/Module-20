import asyncio
import threading
import multiprocessing
import time


async def async_task(num):
    """Асинхронная задача, которая симулирует операцию, ограниченную вводом-выводом.

    Args:
        num: Число для умножения.

    Returns:
        Результат умножения числа на 2.
    """
    await asyncio.sleep(1)  # Симуляция операции, ограниченной вводом-выводом
    return num * 2


def threading_task(num):
    """Задача для потока, которая симулирует операцию, ограниченную вводом-выводом.

    Args:
        num: Число для умножения.

    Returns:
        Результат умножения числа на 2.
    """
    time.sleep(1)
    return num * 2


def multiprocessing_task(num):
    """Задача для процесса, которая симулирует операцию, ограниченную вводом-выводом.

    Args:
        num: Число для умножения.

    Returns:
        Результат умножения числа на 2.
    """
    time.sleep(1)
    return num * 2


async def main():
    """Основная асинхронная функция."""
    nums = list(range(10))

    start_time = time.time()
    async_results = await asyncio.gather(*(async_task(num) for num in nums))
    end_time = time.time()
    print(f"Asyncio time: {end_time - start_time:.4f} seconds")

    start_time = time.time()
    with multiprocessing.Pool(processes=4) as pool:
        multiprocessing_results = pool.map(multiprocessing_task, nums)
    end_time = time.time()
    print(f"Multiprocessing time: {end_time - start_time:.4f} seconds")

    start_time = time.time()
    threads = []
    threading_results = []
    for num in nums:
        thread = threading.Thread(target=lambda n=num: threading_results.append(threading_task(n)), args=())
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Threading time: {end_time - start_time:.4f} seconds")

    print("Asyncio results:", async_results)
    print("Multiprocessing results:", multiprocessing_results)
    print("Threading results:", threading_results)


if __name__ == "__main__":
    asyncio.run(main())

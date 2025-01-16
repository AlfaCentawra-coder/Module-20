import asyncio
import aiofiles
import time

async def calculate_average(filename: str):
    """Вычисляет среднее арифметическое чисел в файле.

    Args:
        filename: Имя файла для обработки.

    Returns:
        Кортеж, содержащий имя файла, среднее значение (или None, если произошла ошибка)
        и затраченное время.
    """
    start_time = time.time()
    total_sum = 0
    count = 0
    try:
        async with aiofiles.open(filename, mode='r') as f:
            async for line in f:
                try:
                    number = int(line.strip())
                    total_sum += number
                    count += 1
                except ValueError:
                    pass
                    """Игнорируем строки, которые не являются числами"""
    except FileNotFoundError:
        return filename, None, 0.0
        """Возвращаем None, если файл не найден"""

    elapsed_time = time.time() - start_time

    average = total_sum / count if count else None

    return filename, average, elapsed_time


async def main():
    """Основная функция для организации вычисления средних значений."""
    filenames = ["/Users/vladimir/PycharmProjects/Project for Attestation/Diplom/files_for_reading/1/file1.txt", "/Users/vladimir/PycharmProjects/Project for Attestation/Diplom/files_for_reading/1/file2.txt", "/Users/vladimir/PycharmProjects/Project for Attestation/Diplom/files_for_reading/1/file3.txt"]
    tasks = [calculate_average(filename) for filename in filenames]
    results = await asyncio.gather(*tasks)

    for filename, average, elapsed_time in results:
        if average is not None:
            print(f"Среднее арифметическое в файле {filename}: {average:.2f}, время: {elapsed_time:.4f} сек.")
        else:
            print(f"В файле {filename} нет чисел или файл не найден, время: {elapsed_time:.4f} сек.")


async def run_all():
    """Вспомогательная функция для запуска основной функции."""
    await main()

"""Запуск асинхронных операций"""
if __name__ == "__main__":
    asyncio.run(run_all())


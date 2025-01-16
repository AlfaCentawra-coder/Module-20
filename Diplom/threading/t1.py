import threading
import time


def calculate_average(filename: str) -> tuple:
    """
    Вычисляет среднее арифметическое чисел в файле.

    Args:
        filename (str): Путь к файлу с числами.

    Returns:
        tuple: Кортеж, содержащий имя файла, среднее значение,
               затраченное время и сообщение об ошибке (если есть).
               Если произошла ошибка, среднее значение будет None.
    """
    start_time = time.time()
    total_sum = 0
    count = 0
    error_message = None

    try:
        with open(filename, 'r') as f:
            for line in f:
                try:
                    number = int(line.strip())
                    total_sum += number
                    count += 1
                except ValueError:
                    print(f"Некорректная строка в файле {filename}: {line.strip()}")
    except FileNotFoundError:
        error_message = "Файл не найден"

    elapsed_time = time.time() - start_time

    if not error_message and count == 0:
        error_message = "Файл пуст или не содержит чисел"
    elif not error_message:
        average = total_sum / count
        return filename, average, elapsed_time, None

    return filename, None, elapsed_time, error_message


def main() -> None:
    """
    Основная функция программы.

    Читает список файлов, вычисляет среднее арифметическое
    чисел в каждом файле с использованием многопоточности
    и выводит результаты.
    """
    filenames = [
        "/Users/vladimir/PycharmProjects/Project for Attestation/Diplom/files_for_reading/1/file1.txt",
        "/Users/vladimir/PycharmProjects/Project for Attestation/Diplom/files_for_reading/1/file2.txt",
        "/Users/vladimir/PycharmProjects/Project for Attestation/Diplom/files_for_reading/1/file3.txt",
    ]

    results = []
    threads = []

    for filename in filenames:
        thread = threading.Thread(target=lambda fn=filename: results.append(calculate_average(fn)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for filename, average, elapsed_time, error_message in results:
        if error_message:
            print(f"{error_message}: {filename}, время: {elapsed_time:.4f} сек.")
        else:
            print(f"Среднее арифметическое в файле {filename}: {average:.2f}, время: {elapsed_time:.4f} сек.")


if __name__ == "__main__":
    main()
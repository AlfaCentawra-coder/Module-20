import multiprocessing
import time

def calculate_average(filename):
    """Вычисляет среднее арифметическое чисел в файле."""
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


def main():
    """Основная функция."""
    filenames = ["file1.txt", "file2.txt", "file3.txt"]

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(calculate_average, filenames)

    for filename, average, elapsed_time, error_message in results:
        if error_message:
            print(f"{error_message}: {filename}, время: {elapsed_time:.4f} сек.")
        else:
            print(f"Среднее арифметическое в файле {filename}: {average:.2f}, время: {elapsed_time:.4f} сек.")

if __name__ == "__main__":
    main()
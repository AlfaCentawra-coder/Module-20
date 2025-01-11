import threading
import time

def calculate_average(filename):
    """Вычисляет среднее арифметическое чисел в файле."""
    start_time = time.time()
    total_sum = 0
    count = 0
    try:
        with open(filename, mode='r') as f:
            for line in f:
                try:
                    number = int(line.strip())
                    total_sum += number
                    count += 1
                except ValueError:
                    pass  # Игнорируем строки, которые не являются числами
    except FileNotFoundError:
        return filename, None, 0.0  # Возвращаем None, если файл не найден

    end_time = time.time()
    elapsed_time = end_time - start_time

    if count == 0:  # Обработка случая пустого файла или файла без чисел
        average = None
    else:
        average = total_sum / count

    return filename, average, elapsed_time


def main():
    """Основная функция."""
    filenames = ["file1.txt", "file2.txt", "file3.txt"]

    results = []
    threads = []
    for filename in filenames:
        thread = threading.Thread(target=lambda fn=filename: results.append(calculate_average(fn)), args=())
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for filename, average, elapsed_time in results:
        if average is not None:
            print(f"Среднее арифметическое в файле {filename}: {average:.2f}, время: {elapsed_time:.4f} сек.")
        else:
            print(f"В файле {filename} нет чисел или файл не найден, время: {elapsed_time:.4f} сек.")

if __name__ == "__main__":
    main()
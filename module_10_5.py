import time
from multiprocessing import Process


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data


def linear_read(filenames):
    for filename in filenames:
        read_info(filename)


def processes_read(filenames):
    processes = []
    for filename in filenames:
        process = Process(target=read_info, args=(filename,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    filenames = [f'file {i}.txt' for i in range(1, 5)]

    print("Линейное чтение:")
    start_time = time.perf_counter()
    linear_read(filenames)
    end_time = time.perf_counter()
    print(f"Время выполнения: {end_time - start_time} секунд")

    print("\nМногопроцессное чтение:")
    start_time = time.perf_counter()
    processes_read(filenames)
    end_time = time.perf_counter()
    print(f"Время выполнения: {end_time - start_time} секунд")

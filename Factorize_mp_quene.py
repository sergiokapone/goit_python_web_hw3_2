from multiprocessing import Process, Queue, current_process
import logging

logger = logging.getLogger(__name__)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)


def find_factors(num: int, queue: Queue) -> None:
    process_id = current_process().name
    logger.info(f"Process number {num} in process name {process_id}")
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    queue.put(factors)  # кладемо в чергу результат


def factorize(*numbers: int) -> list[list]:
    """Використання Quene"""
    processes = []
    results = []

    queue = Queue()

    for number in numbers:
        pr = Process(target=find_factors, args=(number, queue))
        pr.start()
        processes.append(pr)

    # Очікуємо виконання процесів
    for pr in processes:
        pr.join()

    # Витягуємо з черги і додаємо в масив результатів
    while not queue.empty():
        result = queue.get()
        results.append(result)

    return results


if __name__ == "__main__":
    a, b, c, d = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [
        1,
        2,
        4,
        5,
        7,
        10,
        14,
        20,
        28,
        35,
        70,
        140,
        76079,
        152158,
        304316,
        380395,
        532553,
        760790,
        1065106,
        1521580,
        2130212,
        2662765,
        5325530,
        10651060,
    ]

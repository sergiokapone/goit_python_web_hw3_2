import time
import inspect


import Factorize
import Factorize_mp
import Factorize_assync_mp


def timer(func):
    def wrapper(*args, **kwargs):
        print("\n")
        print(f"Функція: {inspect.getmodule(func).__name__}.{func.__name__}")
        print("-" * 50)
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print("-" * 50)
        print(f"Час роботи: {execution_time}")
        print("-" * 50)
        return result

    return wrapper


if __name__ == "__main__":

    data = [128, 255, 99999, 10651060]
    no_proc = timer(Factorize.factorize)
    multiproc = timer(Factorize_mp.factorize)
    multiproc_assync = timer(Factorize_assync_mp.factorize)

    no_proc(*data)
    multiproc(*data)
    multiproc_assync(*data)

import time


import Factorize
import Factorize_mp_quene
import Factorize_mp_pool
import Factorize_assync_mp


def timer(func):
    def wrapper(*args, **kwargs):
        docstring = func.__doc__
        print("\n")
        print(f"{docstring}")
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

    data = [128, 255, 99999, 10651060, 70651060, 70651062]

    # синхронний однопроцесорний код
    no_proc = timer(Factorize.factorize)

    # мультипроцесорний код з чергою
    multiproc_quene = timer(Factorize_mp_quene.factorize)

    # мультипроцесорний код з пулом
    multiproc_pool = timer(Factorize_mp_pool.factorize)

    # мультипроцесорний код на concurrent.futures
    multiproc_assync = timer(Factorize_assync_mp.factorize)

    no_proc(*data)
    multiproc_quene(*data)
    multiproc_pool(*data)
    multiproc_assync(*data)

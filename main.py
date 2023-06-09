import time


import Factorize
import Factorize_thr
import Factorize_mp_pool
import Factorize_assync_mp
import Factorize_mp_quene


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
        print(f"Час факторизації масиву чисел: {execution_time:.2f}")
        print("-" * 50)
        return result

    return wrapper


if __name__ == "__main__":

    data = [128, 255, 99999, 10651060, 70651060, 70651062]

    for fn in [
        # синхронний однопроцесорний код
        timer(Factorize.factorize),
        # мультипоточний однопроцесорний код
        timer(Factorize_thr.factorize),
        # мультипроцесорний код з пулом
        timer(Factorize_mp_pool.factorize),
        # мультипроцесорний код нз пулом executor
        timer(Factorize_assync_mp.factorize),
        # мультипроцесорний код з чергою
        timer(Factorize_mp_quene.factorize),
    ]:
        fn(*data)

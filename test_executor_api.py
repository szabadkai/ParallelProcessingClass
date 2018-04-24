from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from timer import Timer
from load_functions import with_sleep, fib, download_page

if __name__ == "__main__":

    with Timer(verbose=True, name="NO multiplexing"):
        for _ in range(10):
            print(with_sleep(200000))

    with Timer(verbose=True, name="With Processes"):
        with ProcessPoolExecutor() as pool:
            r = pool.map(with_sleep, [200000]*10)
            print([_ for _ in r])

    with Timer(verbose=True, name="With Threads"):
        with ThreadPoolExecutor() as pool:
            r = pool.map(with_sleep, [200000]*10)
            print([_ for _ in r])

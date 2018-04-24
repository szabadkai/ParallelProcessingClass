from multiprocessing import Process
from timer import Timer
from load_functions import with_sleep, fib, download_page


if __name__ == "__main__":
    pool = []

    for i in range(4):
        pool.append(Process(None, fib, "thead number {0}".format(i), [200000]))

    with Timer(verbose=True, name="NO Processes"):
        for _ in range(4):
            fib(200000)

    with Timer(verbose=True, name="With Processes"):
        for t in pool:
            t.start()

        for t in pool:
            t.join()


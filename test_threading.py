from threading import Thread
from timer import Timer
from load_functions import with_sleep, fib, download_page

pool = []

for i in range(10):
    pool.append(Thread(None, with_sleep, "thead number {0}".format(i), [100000]))

with Timer(verbose=True, name="NO threads"):
    for _ in range(10):
        with_sleep(100000)

with Timer(verbose=True, name="With threads"):
    for t in pool:
        t.start()

    for t in pool:
        t.join()


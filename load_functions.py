from time import sleep
from requests import session



def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return b

def download_page(page):
    s = session()
    return s.get(page).status_code

def with_sleep(*args):
    sleep(.1)
    return __name__


def print_and_wait(*args, **kwargs):
    sleep(1)
    print(*args, **kwargs)
    print(r)

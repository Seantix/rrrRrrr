
'программа проверяет набор из 500 больших чисел на простоту'


import time
import multiprocessing

def is_prime(a):
    b = 0
    for i in range(2, int(a ** 0.5) + 1):
        if (a % i == 0):
            b = b + 1
    if (b <= 0):
        return True
    else:
        return False

def test_all(pool):
    l = pool.map(is_prime, range(1_000_000_000, 1_000_000_500))
    return l

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    t0 = time.time()
    print(test_all(pool))
    print("Time spent:", time.time() - t0)
else:
    print("__name__:", __name__)

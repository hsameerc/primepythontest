# This is a Python Script to generate positive prime numbers between given two numbers and number of prime numbers you
# desire between those numbers.
import math
import time


def validateOwn(pn2):
    """
    param pn2: integer positive integers
    return: boolean if it has factors
    """
    pr_sqrt = int(math.sqrt(pn2) + 1)
    pnl = []
    for rn in range(1, pr_sqrt):
        if rn % 2 != 0:
            if pn2 % rn != 0:
                break
            else:
                pnl.append([rn, pn2])
    return len(pnl) > 1


def validate(pn2):
    """
    param pn2: integer positive integers
    return: boolean if it has factors
    """
    pr_sqrt = int(math.sqrt(pn2) + 1)
    pnl = []
    for rn in range(1, pr_sqrt):
        if rn % 2 != 0:
            if pn2 % rn != 0:
                break
            else:
                pnl.append([rn, pn2])
    return len(pnl) > 1


def next_prime(number):
    """
    param number: integer to know next prime
    return: next prime integer
    """
    if number % 2 == 0:
        number = number + 1
    next_num = True
    cp = 2
    while next_num:
        npn = number + cp
        status = validate(npn)
        if npn % 2 == 0 or status:
            cp = cp + 2
            next_num = True
        else:
            next_num = False
            return npn


def get_primes_between(a, b, c):
    """
    param a: integer Between Start
    param b: integer Between End
    param c: integer How many prime numbers
    return: list of prime numbers
    """
    if a % 2 == 0:
        a = a + 1
    px = []
    count = 1
    for d in range(a, b):
        if a < d and d % 2 != 0:
            a = next_prime(a)
            if c == -1 or c >= count:
                px.append(a)
                count = count + 1
            else:
                break
    return px


def test():
    num = 1
    prime_numbers_list = get_primes_between(num, num + 310, 62)
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307]
    print(prime_numbers_list == primes)
    print('Test Successful!')


def prime_num_time_consuming():
    return [i for i in range(2, pow(10, 5)) if 0 not in [
        i % np for np in range(2, i)
    ]]


if __name__ == '__main__':
    test()
    n = 1
    start_time = time.time()
    pnb = get_primes_between(n, n + pow(10, 6), -1)
    print(pnb)
    print(len(pnb))
    print("--- %s seconds ---" % (time.time() - start_time))

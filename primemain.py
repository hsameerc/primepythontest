# This is a Python Script to generate positive prime numbers between given two numbers and number of prime numbers you
# desire between those numbers.
import time

from logics import get_primes_between


def test():
    num = 1
    prime_numbers_list = get_primes_between(num, num + 310, 62)
    primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307]
    print(prime_numbers_list == primes)
    if prime_numbers_list == primes:
        print('Test Successful!')
    else:
        print('Test Failed!')


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

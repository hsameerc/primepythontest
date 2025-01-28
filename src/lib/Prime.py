import math


def validate(pn2):
    """
    param pn2: integer positive integers
    return: boolean if it has factors
    """
    pr_sqrt = int(math.sqrt(pn2) + 1)
    for rn in range(2, pr_sqrt):
        if rn % 2 != 0:
            if pn2 % rn == 0:
                return True
    return False


def next_prime(n):
    """
    param number: integer to know next prime
    return: next prime integer
    """
    if n % 2 == 0:
        n = n + 1
    next_num = True
    cp = 2
    while next_num:
        npn = n + cp
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

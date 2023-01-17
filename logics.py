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


def mod(x, y, m):
    """
    :param x: integer
    :param y: integer
    :param m: integer
    :return:
    """
    return pow(x, y) % m


def enc(i, pr_k, pb_k):
    """
    :param i: integer
    :param pr_k: integer
    :param pb_k: integer
    :return:
    """
    return mod(i, pr_k, pb_k)


def fins(a, b):
    """
    :param a: integer
    :param b: integer
    :return: integer
    """
    return (a - 1) * (b - 1)


def coprime(a, b):
    """
    :param a: integer
    :param b: integer
    :return: integer
    """
    cop = get_primes_between(1, b, -1)
    for i in cop:
        if 1 < i < a and a % i != 0 and b % i != 0:
            return i


def dkey(a, c):
    # find b if a and c are given ( a*b mod c = 1 ) or (a*b % c = 1)
    for x in range(c + 1, c * a):
        y = a * x
        if y % c == 1:
            return int(y / a)


def keygen(p1=1001, p2=271):
    primary_key = p1 * p2  # primary key
    o_n = fins(p1, p2)  # (o(n))
    co_prime = coprime(primary_key, o_n)
    d = dkey(co_prime, o_n)
    return co_prime, d, primary_key

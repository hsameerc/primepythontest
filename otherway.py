# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def next_prime(prime_number):
    next_num = True
    cp = 2
    while next_num:
        pn2 = prime_number + cp
        if pn2 % 2 == 0 \
                or pn2 != 3 and pn2 % 3 == 0 \
                or pn2 != 5 and pn2 % 5 == 0 \
                or pn2 != 7 and pn2 % 7 == 0 \
                or pn2 != 11 and pn2 % 11 == 0 \
                or pn2 != 13 and pn2 % 13 == 0 \
                or pn2 != 17 and pn2 % 17 == 0 \
                or pn2 != 19 and pn2 % 19 == 0 \
                or pn2 != 23 and pn2 % 23 == 0 \
                or pn2 != 37 and pn2 % 37 == 0 \
                or pn2 != 137 and pn2 % 137 == 0 \
                or pn2 != 367 and pn2 % 367 == 0 \
                or pn2 != 3257 and pn2 % 3257 == 0 \
                or pn2 != 5237 and pn2 % 5237 == 0:
            # how many primes?
            cp = cp + 2
            next_num = True
        else:
            next_num = False
            return pn2


if __name__ == '__main__':
    print_hi('PyCharm')
    s = next_prime(142399291)
    print(s)
    # n = 1
    # x = []
    # for z in range(n, 1000):
    #     if n < z:
    #         n = next_prime(n)
    #         x.append(n)
    # print(x)
    # primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
    #           107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
    #           227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307]
    # print(x == primes)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

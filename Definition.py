import math
import random
from random import randint

import numpy as np

from logics import enc


class Definition:
    chars = []
    raw = ''
    primes = []
    defaults = []

    def set_raw(self, raw):
        self.raw = raw

    def set_primes(self, primes):
        self.primes = primes

    def raw_char(self):
        x = []
        for c in self.raw:
            x.append(c)
        return x

    def getDefaults(self):
        return self.defaults

    @staticmethod
    def get_static_chars():
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]
        up = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
              "U", "V", "W", "X", "Y", "Z"]

        chars = [":", " ", " ", "+", "-", "*", "/", "=", "(", ")", "[", "]", "{", "}", ",", "'", "<", ">", "?", "/",
                 "!",
                 "@", "#", "$", "%", "^", "&", "_", "|", ";", ".", "~", "`"]

        s_chars = ['"', '\\']
        return num + small + up + chars + s_chars

    def set_defaults(self):
        d = self.get_static_chars()
        self.defaults = dict(zip(d, self.primes))

    def get_c_indexes(self):
        lcs = []
        d = self.prime_raw_values()
        print(d)

        pr_k = 1721 - 96
        pr_k_pub = pr_k - 11
        pb_k = 1721

        for i, j in d:
            lcs.append(enc(i * j, pr_k, pb_k))
        print(lcs)

    def prime_raw_values(self):
        x = []
        for c in self.raw:
            x.append([self.primes.index(self.defaults[c]), self.defaults[c], ])
        return x

    def new_prime_raw_values(self, raw):
        x = []
        for c in raw:
            x.append(self.primes.index(c))
        return x

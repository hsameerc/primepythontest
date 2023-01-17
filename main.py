# This is a Python Script to generate positive prime numbers between given two numbers and number of prime numbers you
# desire between those numbers.
from chars import dataset
from logics import keygen, enc, get_primes_between


def decrypt(ency, d, pk):
    print("Decrypting Number:" + str(ency))
    decrypted = enc(ency, d, pk)
    print("After Decrypt:" + str(decrypted))
    return decrypted


def encrypt(a, e, pk):
    print("Encrypting Number:" + str(a))
    encrypted = enc(a, e, pk)
    print("Result Encryption:" + str(encrypted))
    return encrypted


def encrypt_all(data_sets, e, primary_key):
    prs = get_primes_between(500, 1000, len(data_sets))
    prsa = get_primes_between(1, 500, len(data_sets))
    se = []
    for k in data_sets:
        ds = data_sets.index(k)
        ex = encrypt(prs[ds], e, primary_key)
        ey = encrypt(prsa[ds], e, primary_key)
        se.append([ex, ey])
    return se


def decrypt_all(enc_array, d, primary_key):
    sd = []
    for x, y in enc_array:
        dx = decrypt(x, d, primary_key)
        dy = decrypt(y, d, primary_key)
        sd.append([dx, dy])
    return sd


if __name__ == '__main__':
    # datasets = dataset()
    e, d, primary_key = keygen()
    # encrypted_array = encrypt_all(datasets, e, primary_key)
    # decrypted_array = decrypt_all(encrypted_array, d, primary_key)
    # print(decrypted_array)

    print("+++++++++++++++++++++")

    a = 53
    enc_val = encrypt(a, e, primary_key)
    decrypt(enc_val, d, primary_key)

    print("+++++++++++++++++++++")

    b = 31
    enc_val = encrypt(b, e, primary_key)
    decrypt(enc_val, d, primary_key)

    print("+++++++++++++++++++++")

    c = 113
    enc_val = encrypt(c, e, primary_key)
    decrypt(enc_val, d, primary_key)

    print("+++++++++++++++++++++")

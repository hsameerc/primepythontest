# This is a Python Script to generate positive prime numbers between given two numbers and number of prime numbers you
# desire between those numbers.
import base64

from chars import dataset
from logics import keygen, enc, get_primes_between


def decrypt(ency, d, pk):
    # print("Decrypting Number:" + str(ency))
    decrypted = enc(ency, d, pk)
    # print("After Decrypt:" + str(decrypted))
    return decrypted


def encrypt(a, e, pk):
    # print("Encrypting Number:" + str(a))
    encrypted = enc(a, e, pk)
    # print("Result Encryption:" + str(encrypted))
    return encrypted


class EncryptDecrypt:
    def __init__(self, encrypt_key, decrypt_key, shared_primary_key):
        self._e = encrypt_key
        self._d = decrypt_key
        self._primary_key = shared_primary_key
        self.enc_data = []
        self.dec_data = []
        existing_datasets = dataset()
        dataset_primes = get_primes_between(500, 1000, len(existing_datasets))
        self.dataset_values = list(zip(dataset_primes, existing_datasets))
        self.dataset_values_inverse = list(zip(existing_datasets, dataset_primes))

    def get_encrypted_data(self, input_data):
        input_char_value = [char for char in input_data]
        elements_value = []
        for char in input_char_value:
            for dt_char, val in self.dataset_values_inverse:
                if char == dt_char:
                    elements_value.append([char, val])
        print(input_data)
        print(self.dataset_values_inverse)
        list_dataset_encrypted_array = [encrypt(value, self._e, self._primary_key) for (key, value) in elements_value]
        return list_dataset_encrypted_array

    def get_decrypted_data(self, encrypted_data):
        list_dataset_decrypted_array = [decrypt(list_dataset_enc, self._d, self._primary_key) for list_dataset_enc in
                                        encrypted_data]
        decrypted_data = []
        for decrypt_value in list_dataset_decrypted_array:
            for char_value, char in self.dataset_values:
                if char_value == decrypt_value:
                    decrypted_data.append(char)

        return decrypted_data


if __name__ == '__main__':
    # TODO:: FOR SPECIAL CHARS
    input_raw = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890 _+=-*()'
    e, d, primary_key = keygen(2039, 17)
    print(e, d, primary_key)
    # exit()
    print("+++++++++++++++++++++")
    # e, primary_key = 17, 271271
    encDecDataUsage = EncryptDecrypt(encrypt_key=e, decrypt_key=0, shared_primary_key=primary_key)
    encrypted_array = encDecDataUsage.get_encrypted_data(input_raw)

    encrypted_array_bytes = bytes(str(encrypted_array), 'utf-8')
    encoded_encrypted_bytes = base64.b64encode(encrypted_array_bytes)
    print(encoded_encrypted_bytes)

    print("+++++++++++++++++++++")
    # d, primary_key = 492353, 271271
    decDecDataUsage = EncryptDecrypt(encrypt_key=0, decrypt_key=d, shared_primary_key=primary_key)
    # encoded_encrypted_bytes = b'WzI1NzIxMSwgMTE5NTgsIDY3NjQ1LCA2NzY0NSwgNzEyMzMsIDE2NDQsIDcxMjMzLCAxNTg1OTQsIDY3NjQ1LCA3OTc5MiwgMjUwNjE1LCAxOTM0MTYsIDE1Njc5MSwgMjQ5NDc4LCA3MjE4NiwgMTU2NzkxLCAxMTk1OCwgMTE5NTgsIDE1ODU5NCwgMjU3MjExLCAyMDM3MjIsIDE1Njc5MSwgNzIxODYsIDIzODgxOCwgNzIxODYsIDgxMTgzLCAyMjQ3MDFd'
    decoded_encrypted_bytes = base64.b64decode(encoded_encrypted_bytes)
    decoded_encrypted_array = eval(decoded_encrypted_bytes.decode('utf-8'))
    decrypted_array = decDecDataUsage.get_decrypted_data(decoded_encrypted_array)
    print("".join(map(str, decrypted_array)))
    print("+++++++++++++++++++++")

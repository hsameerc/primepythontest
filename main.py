# This is a Python Script to generate positive prime numbers between given two numbers and number of prime numbers you
# desire between those numbers.
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
    # e, d, primary_key = keygen()
    print("+++++++++++++++++++++")
    e, primary_key = 17, 271271
    encDecDataUsage = EncryptDecrypt(encrypt_key=e, decrypt_key=0, shared_primary_key=primary_key)
    encrypted_array = encDecDataUsage.get_encrypted_data("HelloWorld")
    print(encrypted_array)
    print("+++++++++++++++++++++")
    d, primary_key = 492353, 271271
    decDecDataUsage = EncryptDecrypt(encrypt_key=0, decrypt_key=d, shared_primary_key=primary_key)
    encrypted_array = [257211, 11958, 67645, 67645, 71233, 1644, 71233, 158594, 67645, 79792]
    decrypted_array = decDecDataUsage.get_decrypted_data(encrypted_array)
    print(decrypted_array)
    print("+++++++++++++++++++++")

import math

from src.lib.Prime import next_prime


def predicted_index(idn_softmax):
    return max(range(len(idn_softmax)),
               key=lambda i: idn_softmax[i])


def word_val(input_data):
    input_word_val = []
    for word in input_data.split():
        input_word_val.append(round(sum(alternate(word)) / len(word), 9))
    return fixed_length_array(input_word_val, len(input_word_val) + 1)


def char_val(input_data):
    return alternate(input_data)


def output_index(n=10, nx=1):
    return [1 if x == nx else 0 for x in range(0, n + 1)]


def output_index_array(value, array_data):
    return [1 if value == x else 0 for x in array_data]


def alternate(input_data):
    indices_array = [(int(ascii_chars().index(char)) / pow(10, 3)) for char in input_data]
    return indices_array


def adjusted(input_data):
    y = []
    for x in input_data.split():
        indices_array = sum([(math.sin(int(ascii_chars().index(char)) / pow(10, 3))) for char in x])
        y.append(indices_array)
    return y


def generate_unicode_characters(start, end):
    unicode_characters = [chr(i) for i in range(start, end + 1)]
    return ''.join(unicode_characters)


def ascii_chars():
    ascii_characters = generate_unicode_characters(32, 126)
    non_ascii_characters = generate_unicode_characters(128, 255)
    # add here other char
    return ascii_characters + non_ascii_characters


def all_chars_index():
    indices_array = {int(ascii_chars().index(char)) / pow(10, 3): char for char in ascii_chars()}
    return indices_array


def all_chars():
    indices_array = [int(ascii_chars().index(char)) / pow(10, 3) for char in ascii_chars()]
    return indices_array


def fixed_length_array(arr, min_len=2):
    fixed_length = min_len
    if len(arr) >= fixed_length:
        return arr[:fixed_length]
    else:
        padding = [0] * (fixed_length - len(arr))
        return arr + padding


def char_in(input_data):
    char_val_new = char_val(input_data)
    all_chars_value = all_chars()
    result = [[1 if x == y else 0 for x in all_chars_value] for y in char_val_new]
    return result


def char_in_alt(input_data):
    char_val_new = char_val(input_data)
    all_chars_value = all_chars()
    result = []
    for i, cha in enumerate(all_chars_value):
        for x in char_val_new:
            result.append(i) if cha == x else None
    return result


def char_out(result):
    # result = [0, 1, 0.... len of all chars]
    ascii_chars_data = ascii_chars()
    ascii_result = [ascii_chars_data[i] for i, y in enumerate(result) if y == 1]
    return ascii_result


def char_out_alt(result):
    # result = [0, 1, 0.... len of all chars]
    ascii_chars_data = ascii_chars()
    ascii_result = [ascii_chars_data[i] for i, y in enumerate(result) if y == 1]
    return ascii_result


def find_max_index(arr):
    if not arr:
        return None

    max_value = arr[0]
    max_index = 0

    for index, value in enumerate(arr):
        if value > max_value:
            max_value = value
            max_index = index

    return max_index


def process_number(input_number):
    number_str = str(input_number)
    n = int(number_str[:-3]) if len(number_str) > 3 else 0
    x = int(number_str[-3:])
    return output_index(1000, n), output_index(999, x)


def main_test_predicted_output(predicted_outputs, class_labels):
    predicted_class_index = max(range(len(predicted_outputs)), key=lambda i: predicted_outputs[i])
    return class_labels[predicted_class_index]


def process_chars(char_value="hello"):
    char_val_new = char_val(char_value)
    all_chars_value = all_chars()
    result = [[1 if x == y else 0 for x in all_chars_value] for y in char_val_new]
    return result

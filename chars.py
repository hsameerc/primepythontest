import unicodedata
def chars():
    return 'thequickbrownfxjmpsvlazydg'


def chars__cap_array():
    return [*chars().upper()]


def chars__small_array():
    return [*chars()]


def num_array():
    return [*'0987654321']


def dataset():
    val =  chars__cap_array() + chars__small_array() + num_array() + special_chars_array()
    return val


def special_chars_array():
    return [" ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", "\\", ";", ":", "'", '"', ",", "<", ">", ".", "?", "/", "~", "`"]
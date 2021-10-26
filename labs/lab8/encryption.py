def encode(user_input, key_input):
    new_string = ""
    for char in user_input:
        new_string += chr(ord(char) + key_input)
    return new_string


def encode_better(user_input, key_message):
    first_string = ""
    for char in range(len(user_input)):
        message = ord(user_input[char]) + (ord(key_message[char % len(key_message)]) - 97)
        first_string += chr(message)
    print(first_string)
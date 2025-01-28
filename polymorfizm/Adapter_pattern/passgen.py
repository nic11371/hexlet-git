from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits as ascii_digits,
    punctuation
)
import random


def generate_password(length, uppercase=False, digits=False, symbols=False):
    gen_pool = ascii_lowercase
    password = [random.choice(ascii_lowercase)]

    if uppercase:
        gen_pool += ascii_uppercase
        password.append(random.choice(ascii_uppercase))

    if digits:
        gen_pool += ascii_digits
        password.append(random.choice(ascii_digits))

    if symbols:
        gen_pool += punctuation
        password.append(random.choice(punctuation))

    remaining_length = length - len(password)
    password.extend(random.choice(gen_pool) for _ in range(remaining_length))
    random.shuffle(password)

    return ''.join(password)

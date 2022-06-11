
import logging as logger
import random
import string


# Random String
def generate_rand_string(length=10, prefix=None, suffix=None):
    random_string=''.join(random.choices(string.ascii_lowercase,k=length))

    if prefix:
        random_string = prefix + random_string
    if suffix:
        random_string = suffix + random_string
    return random_string
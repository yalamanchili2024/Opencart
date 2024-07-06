import random
import string

# File used to generate the random email address values

def random_string_generator(size=5, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

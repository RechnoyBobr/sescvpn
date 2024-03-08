import random
import string


def generate_sid(length):
    sid = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
    return sid

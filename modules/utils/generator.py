from random import choices, sample
from modules.utils.constants import SEED
from string import ascii_letters, digits


def generate_rand_bytes(size):
    return "".join(choices(ascii_letters+digits, k=size)).encode("utf-8")


def generate_key_array(test_cases):
    return sample(range(100, SEED), test_cases)


if __name__ == "__main__":
    # For safety max limit 10000
    arr = generate_rand_bytes(10000)
    print(arr)

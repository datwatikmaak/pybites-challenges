import string
import random


def gen_key(parts=4, chars_per_part=8):
    chars = string.ascii_uppercase + string.digits
    # token = ''.join(random.choice(chars) for i in range(chars_per_part))

    license_key = ""
    for i in range(parts):
        if i < parts - 1:
            license_key += f"{''.join(random.choice(chars) for i in range(chars_per_part))}-"
        else:
            license_key += f"{''.join(random.choice(chars) for i in range(chars_per_part))}"

    print(license_key)


gen_key()

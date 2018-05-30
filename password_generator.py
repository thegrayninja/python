# github.com/thegreyninja
# syntax: python password_generator.py 25

import random
import sys


def random_password():
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz!"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_special = "@#$%^&*(),./<>?;':[]{}-=_"
    alphabet_number = "1234567890"

    total_search = alphabet_lower + alphabet_upper + alphabet_special + alphabet_number
    random_pw = []
    try:
        PWLength = int(sys.argv[1])

    except:
        PWLength = 16

    count = 0
    while count < PWLength:
        value = random.randrange(len(total_search))
        random_pw.insert(count, total_search[value])
        count += 1

    random.shuffle(random_pw)
    print(''.join(random_pw))

random_password()

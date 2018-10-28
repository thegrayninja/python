import random


def PasswordGeneratorMain(PWLength):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz!"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_special = "@#$%^&*(),./<>?;':[]{}-=_"
    alphabet_number = "1234567890"

    total_search = alphabet_lower + alphabet_upper + alphabet_special + alphabet_number
    random_pw = []

    PWLength = int(PWLength)

    value = random.randrange(len(alphabet_lower))
    random_pw.insert(0, alphabet_lower[value])
    value = random.randrange(len(alphabet_upper))
    random_pw.insert(1, alphabet_upper[value])
    value = random.randrange(len(alphabet_special))
    random_pw.insert(2, alphabet_special[value])
    value = random.randrange(len(alphabet_number))
    random_pw.insert(3, alphabet_number[value])

    count = 4
    while count < PWLength:
        value = random.randrange(len(total_search))
        random_pw.insert(count, total_search[value])
        count += 1


    random.shuffle(random_pw)
    FinalPW = ''.join(random_pw)
    return FinalPW

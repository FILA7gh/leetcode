def strongPasswordCheckerII(password: str) -> bool:
    if (len(password) < 8 or password.isalpha() or password.isdigit() or
            password.islower() or password.isupper() or password.isascii()):
        return False

    flag = False
    special_characters = '!@#$%^&*()-+'
    counter = 0

    for i in range(len(password)-1):
        if password[i] == password[i+1]:
            return False

    for p in password:
        if p in special_characters:
            flag = True
        if p not in special_characters:
            counter += 1

    return True if counter > 0 and flag else False



print(strongPasswordCheckerII('ziyS5FrPQhoQ5oEWRpHW2MjI7sGfcMJdcsjQnIyRbdCilvFaQN07jQtAkOklbjFrU5KcHzw4EvJ41Yz2Ykyd'))

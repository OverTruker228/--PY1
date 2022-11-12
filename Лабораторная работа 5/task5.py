import random
import string

def chislo():
    while True:
        try:
            len_ = int(input("Укажите длину пароля: "))
            return len_
        except ValueError:
            len_ = None
            return len_
    return len_

len_ = chislo()
def passwords(n = None):
    if n is None:
        n = 8

    password_list = random.sample(string.hexdigits, n)
    str_ = ("".join(password_list))
    return str_

print(passwords(len_))

# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
def base(i):
    base.dict = {"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)}
    return base.dict
number = []
for i in range(16):
    number = number + [base(i)]
pprint(number)
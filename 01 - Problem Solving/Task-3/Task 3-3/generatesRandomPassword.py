from random import choice, shuffle
from string import ascii_uppercase, ascii_lowercase, digits
pwd = [choice(ascii_lowercase), choice(ascii_uppercase), choice(digits), choice("#$%&@")] \
        + [choice(ascii_lowercase + ascii_uppercase + digits) for _ in range(6)]
shuffle(pwd)
pwd = ''.join(pwd)

print(pwd)
print(len(pwd))

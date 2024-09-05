import string
import random

def password():
    char=string.ascii_letters + string.digits
    ret=''.join(random.choice(char) for x in range(0,15))
    print(ret)
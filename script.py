import math
import os
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    # test = "test"
    greeting = "Hello {}!".format(who_to_greet)
    return greeting


print(greet("Allen"))
print(greet("World"))
r = requests.get("http://coreyms.com")
print(r.status_code)


# name = input("Your name?")
# print("Hello, ", name)


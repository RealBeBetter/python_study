# encoding: utf-8

e = 1
try:
    1 / 0
except ZeroDivisionError as e:
    print(e)  # division by zero

print(e)  # NameError: name 'e' is not defined

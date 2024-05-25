# encoding: utf-8

def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False


params = [
    1234,
    '1234',
    [1, 2, 3, 4],
    {1, 2, 3, 4},
    {1: 1, 2: 2, 3: 3, 4: 4},
    (1, 2, 3, 4)
]

for param in params:
    print('{} is iterable? {}'.format(param, is_iterable(param)))

# 1234 is iterable? False
# 1234 is iterable? True
# [1, 2, 3, 4] is iterable? True
# {1, 2, 3, 4} is iterable? True
# {1: 1, 2: 2, 3: 3, 4: 4} is iterable? True
# (1, 2, 3, 4) is iterable? True

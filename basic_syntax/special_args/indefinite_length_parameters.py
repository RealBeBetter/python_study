def addition(*args, num):
    total = num
    for temp in args:
        total += temp
    return total


print(addition(1, 2, 3, 4, 5, num=9))  # 24

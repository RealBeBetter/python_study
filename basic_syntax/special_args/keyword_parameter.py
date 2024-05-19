def addition(*args, **kwargs):
    total = 0
    for num in args:
        total += num
    # 是否以百分比形式输出
    percent = kwargs.get("percent", False)
    if percent is True:
        total = total * 100
    return total


print(addition(1, 2, 3, 4, 5, percent=True))  # 1500
print(addition(1, 2, 3, 4, 5, percent=False))  # 15
print(addition(1, 2, 3, 4, 5, **{"percent": True}))  # 1500，传递字典作为参数

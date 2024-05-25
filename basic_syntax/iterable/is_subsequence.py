def is_subsequence(a, b) -> bool:
    """
    判断 a 是否是 b 的子序列
    :param a: iterable
    :param b: iterable
    :return: bool
    """
    b = iter(b)
    # 通过 all 函数用来判断一个迭代器的元素是否全部为 True，如果是则返回 True，否则就返回 False
    # 实际等价于 ((i in b) for i in a)，判断在 a 的序列中是否有 b 的子序列
    # i in b 运行之后，因为 next 生成器的缘故，会保留当前的指针
    return all(i in b for i in a)


print(is_subsequence([1, 4, 3], [1, 2, 3, 4]))  # False
print(is_subsequence([1, 2, 3], [1, 2, 3]))  # True
print(is_subsequence([1, 2, 3], [1, 2, 3, 4, 5]))  # True

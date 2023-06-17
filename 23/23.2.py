# def f(x, end):
#     if x > end or x == 10 or x == 11: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x + 2, end) + f(x * 3, end)
#
# print(f(1, 8) * f(8, 27))


# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#     return f(x + 2, end) + f(x * 2, end)
#
#
# print(f(1, 16) * f(16, 34))


# def f(x, end):
#     if x < end: return 0
#     if x == end: return 1
#     return f(x - 1, end) + f(x // 2, end)
#
#
# print(f(44, 15) * f(15, 2))


# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x * 2, end) + f(x * 2 + 1, end)
#
# print(f(1, 15))


# def f(x, end):
#     if x > end or x == 12: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x + 2, end) + f(x * 4, end)
#
#
# print(f(3, 6) * f(6, 15) * f(15, 24))


def f(x, end):
    if x > end or x == 12: return 0
    if x == end: return 1
    return f(x + 1, end) + f(x + 4, end) + f(x * 2, end)


print(f(4, 5) * f(5, 15) * f(15, 24))


# def f(x, end):
#     if x > end or x == 13: return 0
#     if x == end: return 1
#     return f(x + 2, end) + f(x + 3, end) + f(x + 5, end)
#
#
# print(f(5, 17) * f(17, 25))


def f(x, end):
    if x > end or x == 13: return 0
    if x == end: return 1
    return f(x + 1, end) + f(x + 3, end) + f(x * 3, end)


print(f(3, 7) * f(7, 19) * f(19, 24))
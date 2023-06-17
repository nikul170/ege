# def f(x, end):
#     if x > end or x == 17: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x * 2, end)
#
#
# print(f(1, 10) * f(10, 35))


# def f(x, end):
#     if x > end and x == 13: return 0
#     if x == end: return 1
#     return f(x + 2, end) + f(x + 3, end) + f(x + 5, end)
#
#
# print(f(5, 17) * f(17, 25))

# 126 + 126


# def f(x, end):
#     if x < end: return 0
#     if x == end:
#          return 1
#     return f(x - 2, end) + f(x -5, end)
#
#
# print(f(23, 2))



# def f(x, end, c1, c2):
#     if x > end: return 0
#     if x == end: return 1
#     if c1 == 1 and c2 == 1:
#         return f(x * 2, end, 2, c1)
#     elif c1 == 2 and c2 == 2:
#         return f(x + 1, end, 1, c1)
#     else:
#         return f(x + 1, end, 1, c1) + f(x * 2, end, 2, c1)
#
#
# print(f(1, 16, 0, 0))


# def f(x, end, c):
#     if x > end or x == 6:
#         return 0
#     if x == end: return 1
#     a = []
#     if c != 1: a.append(f(x + 1, end, 1))
#     if c != 2: a.append(f(x + 3, end, 2))
#     if c != 3: a.append(f(x ** 2, end, 3))
#     return sum(a)
#
# print(f(1, 5, 0) * f(5, 25, 0))



# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x * 3, end)
#
#
# print(f(1, 30) * f(30, 50) * f(50, 150))




# def f(x, end):
#     if x > end or x == 8: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x + 2, end)
#
#
# print(f(3, 13))


# def f(x, end):
#     if x > end or x == 13: return 0
#     if x == end: return 1
#     return f(x + 2, end) + f(x + 3, end) + f(x + 5, end)
#
#
# print(f(5, 17) * f(17, 25))


# def f(x, end):
#     if x > end or x == 15: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x + 2, end) + f(x * 3, end)
#
#
# print(f(2, 11) * f(11, 16))


# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x * 2, end) + f(x * 3, end)
#
#
# print(f(2, 14) * f(14, 28))


# def f(x, end):
#     if x > end or x == 14: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x + 2, end)
#
#
# print(f(2, 9) * f(9, 18))

                                                                                                                                                                                                                                         
def f(x, end):
     if x > end or x == 30: return 0
     if x == end: return 1
     return f(x + 1, end) + f(x * 2, end) + f(x * 3, end)


print(f(2, 12) * f(12, 36))
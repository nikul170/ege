# import re
#
# for x in range(0, (10 ** 9 ) + 1, 23):
#     if re.fullmatch('12345.7.8', str(x)) is not None:
#         print(x, x // 23)

import re
#
# for x in range(0, 10 ** 8 + 1, 27):
#     if re.fullmatch('123.*890', str(x)) is not None:
#         print(x, x // 27)

# import re
#
#
# def d(x):
#     a = set()
#     for i in range(1, int(x ** 0.5) + 1):
#         if x % i == 0:
#             if i % 2 == 0:
#                 a.add(i)
#             if (x // i) % 2 == 0:
#                 a.add(x // i)
#     return a

# import re
#
# def f(x):
#     a = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             a.add(d)
#             a.add(x // d)
#     return a
#
#
# for x in range(0, 10 ** 7 + 1):
#     if re.match('9..*55.*7', str(x)) is not None:
#         a = f(x)
#         print(x, sum(a) % 21)


# def d(x):
#     a = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             if d % 2 == 0:
#                 a.add(d)
#             if (x // d) % 2 == 0:
#                 a.add(x // d)
#     return a
#
#
# x = 65000
# count = 0
#
# while True:
#     if re.match('6.*97.*5.', str(x)) is not None:
#         k = d(x)
#         if len(k) >= 4:
#             count += 1
#             print(x, sum(k))
#     if count == 7:
#         break
#     x += 1

# import re
#
# for x in range(0, 10 ** 9 + 1, 17):
#     if re.match('12345.6.8', str(x)) is not None:
#         print(x, x // 17)

# import re
#
#
# def f(x, y):
#     a = set()
#     for d in y:
#         if x % d == 0:
#             a.add(d)
#             a.add(x // d)
#     print(a)
#
#


# import re
#
#
# def f(x):
#     c = 0
#     a = list()
#     for d in range(12, 93, 10):
#         if x % d == 0:
#             c += 1
#             a.append(d)
#     return c, a
#
#
# for x in range(103050608, 10 ** 9 + 1):
#     if re.fullmatch('1.3.5.6.8', str(x)) is not None:
#         k = f(x)
#         if k[0] >= 5:
#             print(x, x // min(k[1]))


# import re
#
#
# def f(x):
#     a = set()
#     for d in range(1, int(x ** 0.5)):
#         if x % d == 0:
#             a.add(d)
#             a.add(x // d)
#     return a
#
# for x in range(1000000):
#     if re.match('.6.*6.*.6', str(x)) is not None:
#         if x % 6 == 0 and x % 7 == 0 and x % 8 == 0:
#             k = f(x)
#             print(x, sum(k))


# import re
#
# for x in range(0, 10 ** 9 + 1, 169):
#     if re.fullmatch('123.*567.', str(x)) is not None:
#         print(x, x // 169)


# import re
#
# def f(x):
#     a = set()
#     for d in range(1, int(x **0.5)):
#         if x % d == 0:
#             if d % 2 != 0:
#                 a.add(d)
#             if (x // d) % 2 != 0:
#                 a.add(x // d)
#     return a
#
# for x in range(0, 10 ** 7 + 1, 217):
#     if re.fullmatch('14.4.*', str(x)) is not None:
#         k = f(x)
#         print(x, sum(k))








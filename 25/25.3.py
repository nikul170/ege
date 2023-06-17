import re


def d(x):
    a = set()
    for d in range(1, int(x ** 0.5) + 1):
        if x % d == 0:
            a.add(d)
            a.add(x // d)
    return a

count = 0
x = 1

while True:
    if (re.fullmatch('.6.*6..*6', str(x)) is not None) and all(x % i == 0 for i in [6, 7, 8]):
        print(x, sum(d(x)))
        count += 1
        if count == 7:
            break
    x += 1


# import re
#
#
# for x in range(12, 10 ** 7 + 1, 12):
#     a = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             a.add(d)
#             a.add(x // d)
#     if re.fullmatch('12.*348', str(x)) is not None and len(a) == 12:
#         a.remove(x)
#         print(x, max(a))



# def d(x):
#     a = set()
#     for d in range(2, int(x ** 0.5) + 1):
#         if x % d == 0:
#             a.add(d)
#             a.add(x // d)
#     return 0 if len(a) == 0 else min(a) + max(a)
#
#
# count = 0
# x = 700_001
#
# while True:
#     if d(x) % 10 == 8:
#         print(x, d(x))
#         count += 1
#         if count == 5:
#             break
#     x += 1

# print(1245079 > 1245579)
#
# import re
#
#
#
#
# for x in range(124579, 10 ** 8 + 1):
#     if (re.fullmatch('124.*5.*79', str(x)) is not None) and (x % sum(int(i) for i in str(x) if int(i) % 2 != 0)) == 0:
#         print(x, sum(map(int, str(x))))



# import re
#
#
# for x in range(3999529, 1, -1):
#     a = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             a.add(d)
#             a.add(x // d)
#     if (re.fullmatch('3.*52.', str(x)) is not None) and (len(a) % 2 != 0):
#         a.remove(x)
#         print(x, max(a))


# import re
#
#
# for x in range(121365664, 10 ** 9 + 1, 1):
#     if re.fullmatch('.213.*5664', str(x)) is not None and x % 333 == 0:
#         print(x, x // 333)


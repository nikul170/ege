# from itertools import *
#
#
# def u(x, y, z, w):
#     return (not (z or (w <= y))) or (x <= z)
#
#
# for x1, x2, x3, x4, x5, x6, x7 in product([0,1], repeat=7):
#     t = (
#         (0, x1, 0, x2, 0),
#         (x3, 0, 1, x4, 0),
#         (x5, 1, x6, x7, 0),
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)


# def f(N):
#     n = bin(N)[2:]
#     if sum(map(int, n)) % 2 == 0:
#         n += '0'
#         n = '1' + n[2:]
#     else:
#         n += '1'
#         n = '11' + n[2:]
#
#     return int(n, 2)
#
#
#
# for N in range(1, 1000):
#     if f(N) > 49:
#         print(f(N))
#         break


# from turtle import *
#
# m = 20
# tracer(0)
#
# for _ in range(2):
#     rt(120)
#     fd(7 * m)
# rt(300)
# for _ in range(2):
#     rt(120)
#     fd(7 * m)
#
# up()
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x * m, y * m)
#         dot(2, 'black')
# update()
# input()


# from itertools import *

# k = 0
# for x in product('012345678', repeat=7):
#     a = ''.join(x)
#     if a[0] not in '013579' and a[-1] not in '02468' and a.count('8') == 1:
#         k += 1
# print(k)


# f = open('9.csv').readlines()
# k = 0
# for a in f:
#     x = sorted(list(map(int, a.split('	'))))
#     if len(set(x)) == 3 and ((x[-1] ** 2) < (x[0] ** 2 + x[1] ** 2)):
#         print(x)
#         k += 1
# print(k)


# s = '7' * 116
#
# while ('333' in s) or ('7777' in s):
#     if ('333' in s):
#         s = s.replace('333', '77', 1)
#     else:
#         s = s.replace('7777', '3', 1)
# print(s)


# x = 5 * 216 ** 155 + 4 * 36 ** 156 - 4 * 6 ** 157 - 2023
# k = 0
# while x > 0:
#     if x % 6 == 0:
#         k += 1
#     x //= 6
# print(k)


# def f(x, y, a):
#     return (x < a) or (y < a) or (x + 2 * y > 150)
#
#
# print(min(a for a in range(100) if all(f(x, y, a) for x in range(1000) for y in range(1000))))


# def f(n):
#     if n < 3:
#         return 1
#     if n > 2 and n % 2 == 0:
#         return f(n - 1) + n
#     if n > 2 and n % 2 != 0:
#         return f(n - 2) + 2 * n
#
# print(f(23) - f(21))

# a = list(map(int, open('17.txt')))
# k = 0
# m = max(i for i in set(a) if i % 100 == 12)
# m1 = -float('inf')
#
# for i in range(len(a) - 1):
#     if (((a[i] % 100 == 12) and (a[i + 1] % 100 != 12)) or ((a[i] % 100 != 12) and (a[i + 1] % 100 == 12))) and ((a[i] + a[i + 1]) ** 2 < m ** 2):
#         k += 1
#         m1 = max(m1, a[i] + a[i + 1])
# print(k, m1)

# def f(s1, s2, c, m):
#     if s1 + s2 >= 117: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s1 + 1, s2, c + 1, m), f(s1, s2 + 1, c + 1, m), f(s1 * 2, s2, c + 1, m), f(s1, s2 * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 104):
#     for m in range(1, 5):
#         if f(13, s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break

# import sys
# sys.setrecursionlimit(9999999)
# def f(x, end):
#     if x > end and x == 26: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x * 2, end)
#

# print(f(2, 11) * f(11, 39))


# a = open('24.txt').readline()
# m = -float('inf')
# i = 0
# k = 1
# while i < len(a) - 1:
#     if (a[i] + a[i + 1] == 'FE') or (a[i] + a[i + 1] == 'EF'):
#         k += 1
#         m = max(m, k)
#         i += 1
#     else:
#         k = 1
#         i += 1
# print(m)

# import re
#
# for x in range(1, 10 ** 8 + 1):
#     if re.fullmatch('12.3.*46', str(x)) is not None:
#         if x % 129 == 0:
#             print(x, x // 129)


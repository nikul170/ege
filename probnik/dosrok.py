# from itertools import *
#
#
# def u(x, y, z, w):
#     return (x and (not y)) or (y == z) or (not w)
#
#
# for x1, x2, x3, x4 in product([0,1], repeat=4):
#     t = (
#         (0, x1, x2, 0, 0),
#         (0, 1, 0, 1, 0),
#         (x3, 1, 0, x4, 0)
#          )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)


# def f(N):
#     n = bin(N)[2:]
#     if N % 3 == 0:
#         n += n[-3:]
#     else:
#         n += bin((N % 3) * 3)[2:]
#     return int(n, 2)
#
#
# N = 1
# while True:
#     if f(N) < 100:
#         print(N, f(N))
#     N += 1


from turtle import *

m = 15
tracer(0)
rt(315)

for _ in range(7):
    fd(16 * m)
    rt(45)
    fd(8 * m)
    rt(135)


up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(2, 'black')

update()
input()

# from itertools import *
#
#
# k = 0
#
# for x in product('АВЛОР', repeat=4):
#     k += 1
#     a = ''.join(x)
#     print(k, a)
#     if a[0] == 'Л':
#         print(k, a)
#         break


# f = open('9.csv')
# k = 0
#
# for line in f:
#     a = sorted(list(map(int, line.split())))
#     if (len(a) == len(set(a))) and 3 * (a[0] + a[-1]) < 2 * (a[1] + a[2] + a[3]):
#         k += 1
#         print(a)
# print(k)


# for n in range(4, 1000):
#     s = '3' + '5' * n
#     while '25' in s or '355' in s or '555' in s:
#         if '25' in s:
#             s = s.replace('25', '3', 1)
#         if '355' in s:
#             s = s.replace('355', '52', 1)
#         if '555' in s:
#             s = s.replace('555', '23', 1)
#     if sum(map(int, s)) == 27:
#         print(s, n)


# m = float('inf')
# for x in '0123456789ABCDE':
#     try:
#         if (int('97968' + x + '13', 15) + int('7' + x + '213', 15)) % 14 == 0:
#             m = min(m, int('97968' + x + '13', 15) + int('7' + x + '213', 15))
#             print(int('97968' + x + '13', 15) + int('7' + x + '213', 15))
#     except:
#         ...
# print()
# print(m / 14)


# def f(x, a):
#     return (x & 39 == 0) or ((x & 11 == 0) <= (not (x & a == 0)))
#
#
# print(min(a for a in range(1000) if all(f(x, a) for x in range(10000))))


# def f(n):
#     if n >= 2025:
#         return n
#     if n < 2025:
#         return n + 3 + f(n + 3)
#
#
# print(f(23) - f(21))


# a = list(map(int, open('17.txt')))
#
# k = 0
# m = float('inf')
# m1 = min(i for i in set(a) if 100 <= i <= 999 and i % 10 == 5)
#
# for i in range(len(a) - 1):
#     if ((100 <= a[i] <= 999) + (100 <= a[i + 1] <= 999)) == 1 and (a[i] + a[i + 1]) % m1 == 0:
#         k += 1
#         print(a[i], a[i + 1])
#         m = min(m, a[i] + a[i + 1])
# print(k, m)


# def f(s, c, m):
#     if s >= 78: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s + 4, c + 1, m), f(s * 4, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else any(h)
#
#
# for s in range(1, 78):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 2:
#                 print(s)
#             break


# def f(i):
#     if a[i][2] == 0:
#         return a[i][1]
#     else: return max(f(j - 1) for j in a[i][2:]) + a[i][1]
#
#
# a = [list(map(int, line.replace(';', ' ').split())) for line in open('22.txt')]
# print(max(f(i) for i in range(len(a))))

import sys

sys.setrecursionlimit(999999)
def f(x, end):
    if x > end or x == 13: return 0
    if x == end: return 1
    return f(x + 1, end) + f(x + 2, end) + f(x * 3, end)


print(f(3, 8) * f(8, 18))

# import itertools
#
#
# a = open('24.txt').readline()
# syms = [''.join(x) for x in itertools.product('QRS', repeat=2)]
# k = 1
# m = -float('inf')
# for i in range(len(a) - 1):
#     if a[i] + a[i + 1] not in syms:
#         k += 1
#         m = max(m, k)
#     else:
#         k = 1
# print(m)


# import re
#
#
# for x in range(273, 10 ** 8 + 1, 273):
#     if re.fullmatch('12..36.*1', str(x)) is not None:
#         print(x, x // 273)



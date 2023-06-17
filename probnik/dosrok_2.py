# from itertools import *
#
#
# def u(x, y, z, w):
#     return (not (y and (not x))) and (not (x == z)) and w
#
#
# for x1, x2, x3, x4 in product([0,1], repeat=4):
#     t = (
#         (0, 0, x1, 1, 1),
#         (0, 1, 0, 1, 1),
#         (x2, x3, 0, x4, 1),
#     )
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
#     if f(N) > 76:
#         print(N, f(N))
#         break
#     N += 1


# from turtle import *
#
#
# tracer(0)
# m = 15
#
# rt(45)
# for _ in range(7):
#     fd(6 * m)
#     rt(45)
#     fd(12 * m)
#     rt(135)
#
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(4, 'black')
# update()
# input()


# from itertools import *
#
#
# k = 0
# for x in product('АКЛМНЯ', repeat=5):
#     s = ''.join(x)
#     k += 1
#     if s[:2] == 'КМ':
#         print(k, s)
#         break


# f = open('9.csv')
# k = 0
#
# for line in f:
#     a = sorted(list(map(int, line.split())))
#     if len(set(a)) == 5 and (2 * (a[0] + a[4])) >= (a[1] + a[2] + a[3]):
#         k += 1
# print(k)


# s = '3' + '5' * 26
# while '25' in s or '355' in s or '555' in s:
#     if '25' in s:
#         s = s.replace('25', '32', 1)
#     if '355' in s:
#         s = s.replace('355', '25', 1)
#     if '555' in s:
#         s = s.replace('555', '3', 1)
# print(sum(map(int, s)))


for x in '0123456789ABCDE':
    try:
        if (int('97968' + x + '15', 15) + int('7' + x + '233', 15)) % 14 == 0:
            print((int('97968' + x + '15', 15) + int('7' + x + '233', 15)) // 14)
    except:
        ...



# def f(x, y, a):
#     return (x >= 9) or (2 * x < y) or (x * y < a)
#
#
# print(min(a for a in range(150) if all(f(x, y, a) for x in range(500) for y in range(500))))


# def f(n):
#     if n >= 2025:
#         return n
#     if n < 2025:
#         return n + f(n + 2)
#
#
# print(f(2022) - f(2023))


# a = list(map(int, open('17.txt')))
# k = 0
# ma = max(a[i] for i in range(len(a)) if 10 <= a[i] <= 99)
# m = -float('inf')
# for i in range(len(a) - 1):
#     if ((10 <= a[i] <= 99) + (10 <= a[i + 1] <= 99)) == 1 and (a[i] + a[i + 1]) % ma == 0:
#         k += 1
#         m = max(m, a[i] + a[i + 1])
# print(k, m)


# def f(s, c, m):
#     if s >= 43: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s + 4, c + 1, m), f(s * 3, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 43):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 4:
#                 print(s)
#             break



# def f(i):
#     if a[i][2] == 0:
#         return a[i][1]
#     else:
#         return max(f(j - 1) for j in a[i][2:]) + a[i][1]
#
#
# a = [list(map(int, line.replace(';', ' ').split())) for line in open('22.txt')]
# print(max(f(i) for i in range(len(a))))


# def f(x, end):
#     if x > end or x == 11: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x * 2, end) + f(x * 3, end)
#
#
# print(f(2, 15) * f(15, 25))

from itertools import *

a = open('24.txt').readline()

syms = [''.join(x) for x in product('XYZ', repeat=2)]
k = 1
m = -float('inf')

for i in range(len(a) - 1):
    if (a[i] + a[i + 1]) not in syms:
        k += 1
        m = max(m, k)
    else:
        k = 1
print(m)


# import re
#
# for x in range(211, 10 ** 8 + 1, 211):
#     if re.fullmatch('11..4.*56', str(x)) is not None:
#         print(x, x // 211)


f = open('26.txt')
K = int(f.readline())
N = int(f.readline())
a = [-1] * K
c = []
count = 0

for i in range(N):
    c.append(list(map(int, f.readline().split())))
c.sort()

for i in range(N):
    for j in range(len(a)):
        if c[i][0] > a[j]:
            a[j] = c[i][1]
            count += 1
            m = j + 1
            break
print(count, m)
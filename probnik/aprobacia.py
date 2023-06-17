# from itertools import *
#
# def u(x, y, z, w):
#     return ((w <= y) <= (x == y)) or (not z)
#
#
# for x1, x2, x3, x4, x5 in product([0,1], repeat=5):
#     t = (
#         (x1, 0, 1, 0, 0),
#         (0, x2, x3, 0, 0),
#         (x4, 1, 1, x5, 0),
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
#         n += bin(((N % 3) * 3))[2:]
#     return int(n, 2)
#
#
# N = 1
# while True:
#     if f(N) < 76:
#         print(N)
#     N += 1


# from turtle import *
#
#
# tracer(0)
# m = 15
#
# rt(315)
# for _ in range(7):
#     fd(12 * m)
#     rt(45)
#     fd(6 * m)
#     rt(135)
#
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(4, 'black')
#
# update()
# input()



# from itertools import *
#
# k = 0
# for x in product('АВОРТ', repeat=6):
#     s = ''.join(x)
#     k += 1
#     if s == 'ВОРОТА':
#         print(k)


# f = open('9.csv')
# k = 0
#
# for line in f:
#     a = sorted(list(map(int, line.split())))
#     if len(set(a)) == 5 and (3 * (a[0] + a[-1])) >= (2 * (a[1] + a[2] + a[3])):
#         k += 1
# print(k)


# for n in range(3, 1000):
#     s = '2' + '5' * n
#     while ('25' in s) or ('355' in s) or ('555' in s):
#         if '25' in s:
#             s = s.replace('25', '5', 1)
#         if '355' in s:
#             s = s.replace('355', '52', 1)
#         if '555' in s:
#             s = s.replace('555', '3', 1)
#     if s.count('3') == 2:
#         print(n)


# for x in '0123456789abcde':
#     try:
#         if (int('99658' + x + '29', 15) + int('102' + x + '023', 15)) % 14 == 0:
#             print((int('99658' + x + '29', 15) + int('102' + x + '023', 15)) // 14)
#     except:
#         ...


# def f(x, a):
#     return ((x & 52 != 0) and (x & 36 == 0)) <= (not (x & a == 0))
#
#
# print(min(a for a in range(100) if all(f(x, a) for x in range(1000))))


# def f(n):
#     if n >= 2025: return n
#     if n < 2025:
#         return n + 3 + f(n + 3)
#
#
# print(f(2018) - f(2022))


a = list(map(int, open('17.txt')))
k = 0
m = -float('inf')
mi = min(i for i in set(a) if i in range(100, 1000) and i % 10 == 5)

for i in range(len(a) - 1):
    if (a[i] in range(100, 1000) or a[i + 1] in range(100, 1000)) and (a[i] + a[i + 1]) % mi == 0:
        k += 1
        m = max(m, a[i] + a[i + 1])
print(k, m)

#
# def f(s, c, m):
#     if s >= 55: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s + 4, c + 1, m), f(s * 3, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 55):
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
# print(a)
# print(max(f(i) for i in range(len(a))))


# def f(x, end):
#     if x > end or x == 12: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x + 2, end) + f(x * 2, end)
#
# print(f(2, 9) * f(9, 17))
#
# from itertools import *
#
#
# a = open('24.txt').readline()
# n = [''.join(x) for x in product('NOP', repeat=2)]
# print(n)
# k = 1
# m = -float('inf')
#
# for i in range(len(a) - 1):
#     if a[i: i + 2] not in n:
#         k += 1
#         m = max(k, m)
#     else:
#         k = 1
# print(m)


# import re
#
# for x in range(253, 10 ** 8 + 1, 253):
#     if re.fullmatch('12..15.*6', str(x)) is not None:
#         print(x, x // 253)


# f = open('26.txt')
# K = int(f.readline())
# N = int(f.readline())
# n = [0] * K
# a = []
# count = 0
#
# for i in range(N):
#     a.append(list(map(int, f.readline().split())))
# a.sort()
#
# for i in range(N):
#     for j in range(K):
#         if a[i][0] > n[j]:
#             n[j] = a[i][1]
#             count += 1
#             c = j + 1
#             break
# print(count, c)


f = open('27.txt')
K = int(f.readline())
N = int(f.readline())
a = []

for i in range(K):
    a.append(int(f.readline()))

m = k = - float('inf')
for i in range(K, N):
    x = int(f.readline())
    m = max(m, a[i % K])
    k = max(k, m + x)
    a[i % K] = x
print(k)




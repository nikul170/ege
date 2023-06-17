# from itertools import *
#
#
# def u(x, y, z, w):
#     return not (w == y) and (z <= w) and (not x)
#
#
# for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
#     t = (
#         (x1, x2, x3, 1, 1),
#         (1, x4, 1, x5, 1),
#         (0, x6, 1, 0, 1)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)


# def f(N):
#     n = bin(N)[2:]
#     if N % 2 == 0:
#         n = '1' + n + '00'
#     else:
#         n = '10' + n + '1'
#
#     return int(n, 2)
#
#
# N = 1
# while True:
#     if f(N) < 1000:
#         print(N)
#     N += 1


# from turtle import *
#
#
# tracer(0)
# m = 15
#
# for _ in range(5):
#     for _ in range(5):
#         for _ in range(5):
#             fd(2 * m)
#             lt(120)
#         fd(2 * m)
#         lt(120)
#         fd(2 * m)
#     fd(2 * m)
#     lt(120)


# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(4, 'black')
# update()
# input()


# from itertools import *
#
# k = 0
# for x in product('АБВГД', repeat=3):
#     s = ''.join(x)
#     if s[0] <= s[1] <= s[2]:
#         k += 1
#         print(s)
# print(k)


# f = open('9.csv')
# count = 0
#
# for line in f:
#     a = sorted(list(map(int, line.split())))
#     sr = sum(a) / len(a)
#     if a[-1] > sr and a[-2] > sr and a[-3] > sr:
#         count += 1
#
# print(count)


# for n in range(100):
#     s = '>' + '0' * 40 + '1' * n + '2' * 40
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s:
#             s = s.replace('>1', '22>', 1)
#         if '>2' in s:
#             s = s.replace('>2', '2>', 1)
#         if '>0' in s:
#             s = s.replace('>0', '1>', 1)
#     s = s.replace('>', '0')
#     su = sum(map(int, s))
#     if 99 < su < 1000 and len(set(str(su))) == 1:
#         print(n, su)


# for p in range(16):
#     for x in '0123456789abcdef':
#         for y in '0123456789abcdef':
#             try:
#                 if int('5' + x + '83', p) + int(x +'9' + x + '9', p) == int(y + '20' + y, p):
#                     print(int(x + y + y + x, p))
#             except:
#                 ...


# b1, b2 = 160, 180
# # b = [i / 10 for i in range(b1 * 10, b2 * 10 + 1)]
# #
# #
# # def d(n, m):
# #     return n % m
# #
# #
# # def f(x, a):
# #     return (x in b) <= (d(x, 35) <= d(x, a))
# #
# #
# # count = 0
# #
# # for a in range(1, 100):
# #     if all(f(x, a) for x in range(1, 1000)):
# #         count += 1
# # print(count)



# def f(n):
#     if n == 0:
#         return 0
#     if n % 2 == 0 and n > 0:
#         return f(n / 2) - 1
#     if n % 2 !=0 and n > 0:
#         return 1 + f(n - 1)
#
#
# count = 0
# for n in range(1000):
#     if f(n) == 0:
#         count += 1
# print(count)


# a = list(map(int, open('17.txt')))
# count = 0
# m = -float('inf')
#
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if abs(a[i] - a[j]) % 36 == 0 and ((a[i] % 13 == 0) or (a[j] % 13 == 0)):
#             count += 1
#             m = max(m, a[i] - a[j])
# print(count, m)



def f(a, b, c, m):
    if (a * b) >= 63: return c % 2 == m % 2
    if c == m: return 0
    h = [f(a + 1, b, c + 1, m), f(a, b + 1, c + 1, m), f(a * 2, b, c + 1, m), f(a, b * 2, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 32):
    for m in range(1, 5):
        if f(2, s, 0, m):
            if m == 4:
                print(s)
            break


# def f(x, end):
#     if x > end or x == 13: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x + 4, end) + f(x * 2, end)
#
#
# print(f(4, 7) * f(7, 16) * f(16, 22))


a = open('24.txt').readline()
m = -float('inf')
k = 3
for i in range(len(a) - 3):
    if a[i:i + 4] != 'XZZY':
        k += 1
        m = max(m, k)
    else:
        k = 3

print(m)


# import re
#
#
# for x in range(169, 10 ** 9 + 1, 169):
#     if re.fullmatch('123.*567.', str(x)) is not None:
#         print(x, x // 169)


# f = open('26.txt')
# N = int(f.readline())
# a = []
#
# for i in range(N):
#     a.append(list(map(int, f.readline().split())))
# a.sort(key=lambda x: (-x[0], x[1]))
#
# m = -float('inf')
# count = 0
# for i in range(1, N - 1):
#     if (a[i][0] == a[i - 1][0] and a[i][0] == a[i + 1][0]) and ((a[i][1] - a[i - 1][1] == 6) and a[i + 1][1] - a[i][1] == 6):
#         m = max(m, a[i][0])
#         count += 1
# print(m, count)


f = open('27.txt')
N = int(f.readline())
a = [-float('inf')] * 120
m1 = m = m2 = -float('inf')
for i in range(N):
    x = int(f.readline())
    for y in range(120):
        if (x + y) % 120 == 0 and x < a[y]:
            if x + a[y] > m:
                m = x + a[y]
                m1, m2 = x, a[y]
    a[x % 120] = max(a[x % 120], x)
print(m2, m1)

# from itertools import *
#
#
# def u(x, y, z, w):
#     return not ((x == y) or (x == z)) or w or (not(y <= z))
#
#
# for x1, x2, x3, x4, x5, x6, x7 in product([0,1], repeat=7):
#     t = (
#         (0, x1, 0, 0, 0),
#         (1, x2, x3, x4, 0),
#         (0, x4, x5, x6, 0),
#         (1, x7, 1, 1, 0),
#          )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)


# def f(N):
#     n = bin(N)[2:]
#     for _ in range(2):
#         s = sum(map(int, n)) % 2
#         n += str(s)
#     return int(n, 2)
#
# N = 1
# while True:
#     if f(N) > 64:
#         print(N)
#         break
#     N += 1


# from turtle import *
#
#
# tracer(0)
# m = 10
# for _ in range(10):
#     fd(30 * m)
#     lt(120)
#
# up()
# for x in range(-20, 50):
#     for y in range(-20, 50):
#         goto(x * m, y * m)
#         dot(4, 'black')
# update()
# input()

# input
# a = open('24.txt').readline().split('A')
# a.remove('')
# m = -float('inf')
# for i in range(len(a) - 2):
#     if a[i] == a[i + 1] and a[i + 1] == a[i + 2]:
#         m = max(m, len(a[i]) * 3 + 4)
#         if len(a[i]) == 3:
#             print(a[i])
# print(m)

# def f(x, a):
#     return (x not in {1, 2, 4, 8, 16}) and (x not in {3, 4, 9, 16}) or (x in a)
#
#
# a = {1, 2, 3, 4, 8, 9, 16}
# for x in range(0, 100):
#     print(f(x, a))


# def f(x):
#     s = ''
#     while x > 0:
#         s = str(x % 7) + s
#         x //= 7
#     return s
#
#
# x = 57 * 7 ** 2103 - 6 * 7 ** 1270 + 3 * 7 ** 57 - 98
# print(sum(map(int, str(f(x)))))


# def f(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 3
#     if n > 1 and n % 2 == 0:
#         return f(n - 1) - f(n - 2) + 3 * n
#     if n > 1 and n % 2 != 0:
#         return f(n - 2) - f(n - 3) + 2 * n
#
#
# print(f(40))


# a = list(map(int, open('17.txt')))
# count = 0
# m = -float('inf')
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if a[i] * a[j] % 26 == 0:
#             count += 1
#             m = max(m, a[i] + a[j])
# print(count, m)



# def f(s, c, m):
#     if s >= 46: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 46):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 4:
#                 print(s)
#             break


# def f(i):
#     if a[i][2] == 0:
#         return a[i][1]
#     else: return max(f(i - 1) for i in a[i][2:]) + a[i][1]
#
#
# a = [list(map(int, line.replace(';', ' ').split())) for line in open('22.txt')]
# print(max(f(i) for i in range(len(a))))


# def f(x, end):
#     if x > end or x == 18 or x == 11: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x+ 2, end) + f(x * 3, end)
#
#
# print(f(4, 8) * f(8, 23))


# a = open('24.txt').readline()
# m = -float('inf')
# k = 0
#
# for i in range(len(a) - 1):
#     if (a[i] + a[i + 1] != 'NP') and a[i] + a[i + 1] != 'PO':
#         k += 1
#         m = max(m, k)
#     else:
#         k = 1
# print(m)



# import re
#
#
# def f(x):
#     s = ''
#     while x > 0:
#         s = str(x % 7) + s
#         x //= 7
#     return s
#
# for x in range(333, 10 ** 9 + 1, 333):
#     if re.fullmatch('.213.*5664', f(x)) is not None:
#         print(x, x // 333)


# f = open('26.txt')
# N = int(f.readline())
# a = [0] * 23
# n = []
#
# for i in range(9):
#     x = int(f.readline())
#     n.append(x)
#
# j = 0
# c = []
# count = 0
# for i in range(9, N):
#     x = int(f.readline())
#     a[n[j] % 23] += 1
#     for y in range(23):
#         if x * y % 23 == 0:
#             count += a[y]
#     j += 1
#     n.append(x)
# print(count)




# from itertools import *
#
#
# def u(x, y, z, w):
#     return (x and (y or (not z)) and w) == (x <= (not y) and z)



# for x1,x2,x3,x4,x5,x6 in product([0,1], repeat=6):
#     t = (
#         (x1, 1, x2, x3, 1),
#         (1, 1, x4, x5, 1),
#         (1, 1, 1, x6, 1)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)


# def f(N):
#     n = bin(N)[2:]
#     if n[-1] == '0':
#         n = n[:-1] + '1'
#     else:
#         n = n[:-1] + '0'
#     n += str(sum(map(int, n)) % 2)
#     return int(n, 2)
#
#
# N = 1
# m = float('inf')
# while True:
#     if f(N) > 78 and f(N) < m:
#         m = f(N)
#         print(N, f(N))
#     N += 1


# from turtle import *
#
# tracer(0)
# m = 10
#
# for _ in range(95):
#     fd(20 * m)
#     rt(90)
#
# up()
# for x in range(-30, 30):
#     for y in range(-30, 30):
#         goto(x * m, y * m)
#         dot(2, 'black')
# update()
# input()


# from itertools import *
#
#
# k = 0
# a = ['А', "Е"]
# for x in product('АВЕЛРФЬ', repeat=6):
#     k += 1
#     s = ''.join(x)
#     if all(i not in s for i in a):
#         print(k)
#         break


# k = 0
# for line in open('9.txt'):
#     a = sorted(list(map(int, line.split())))
#     if len(a) == len(set(a)) and 3 * (a[2] + a[3] + a[1]) /(a[0] + a[-1]) > 4:
#         k += 1
# print(k)


# for x in range(101, 1000):
#     s = '5' * x
#     while '555' in s or '888' in s:
#         s = s.replace('555', '8', 1)
#         s = s.replace('888', '55', 1)
#     if '8' not in s:
#         print(x)
#         break
# def f(x):
#     s = ''
#     while x > 0:
#         s = str(x % 6) + s
#         x //= 6
#     return sum(map(int, s))
#
#
#
# for x in '0123456789abcdef':
#     s = int('b7a' + x + '9', 16) + int('54' + x + 'ed', 16)
#     if f(s) == 25:
#         print(s)


# def f(x, y, a):
#     return (x * y < 2 * a) or (x >= 11) or (x < 2 * y)
#
#
# print(min(a for a in range(-200, 200) if all(f(x, y, a) for x in range(1, 100) for y in range(1, 100))))
# def g(n):
#     if n < 2:
#         return 1
#     if n >= 2:
#         return f(n - 2) + 2 * g(n - 2)
#
#
# def f(n):
#     if n < 2:
#         return 1
#     if n >= 2:
#         return f(n - 2) + 3 * g(n - 2)
#
#
# print(sum(map(int, str(f(24)))))


# a = list(map(int, open('17.txt')))
# count = 0
# m = float('inf')
# ma = max(i for i in set(a) if i % 11 == 0)
#
# for i in range(len(a) - 1):
#     if a[i] > ma or a[i + 1] > ma:
#         count += 1
#         m = min(m, a[i] + a[i + 1])
# print(count, m)



# def f(a, b, c, m):
#     if a + b >= 40: return c % 2 == m % 2
#     if c == m: return 0
#     h = []
#     if a < b:
#         for i in range(1, a):
#             h += [f(a + i, b, c + 1, m)]
#     else:
#         for i in range(1, b):
#             h += [f(a, b + i, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 36):
#     for m in range(1, 5):
#         if f(s, 4, 0, m):
#             if m == 3:
#                 print(s)
#             break


# f = open('27.txt')
# N, M = map(int, f.readline().split())
# a = []
#
#
# for i in range(N):
#     x, s = map(int, f.readline().split())
#     n = s // M if s % M == 0 else s // M + 1
#     a.append([x, n])
#
# p = [a[0][1]]
# for i in range(1, N):
#     p.append(a[i][1] + p[i - 1])
# print(a)
#
# s = 0
# for i in range(1, N):
#     s += (a[i][0] - a[0][0]) * a[i][1]
#
# m = float('inf')
#
# for i in range(1, N):
#     d = (a[i][0] - a[i - 1][0])
#     s = s + d * p[i - 1] - (p[-1] - p[i - 1]) * d
#     m = min(m, s)
# print(m)


# f = open('27.txt')
# K = int(f.readline())
# N = int(f.readline())
# a = []
#
# for i in range(K):
#     a.append(int(f.readline()))
#
# m = k = -float('inf')
# for i in range(K, N):
#     x = int(f.readline())
#     m = max(m, a[i % K])
#     k = max(k, m + x)
#     a[i % K] = x
# print(k)



# f = open('27.txt')
# N = int(f.readline())
# a = []
# n = [0] * 23
# count = 0
# for i in range(9):
#     a.append(int(f.readline()))
#
# for i in range(9, N):
#     x = int(f.readline())
#     n[a[i - 9] % 23] += 1
#     for y in range(23):
#         if x * y % 23 == 0:
#             count += n[y]
#     a.append(x)
# print(count)


# a = open('22.txt').readline().replace('TXA', '*').replace('XA', '&').replace('XY', '&')
#
# k = 0
# m = -float('inf')
#
# for i in range(len(a)):
#     if a[i] == '&':
#         k += 2
#         m = max(m, k)
#     elif a[i] == '*':
#         k += 3
#         m = max(m, k)
#     else:
#         k = 0
# print(m)

# import re
#
# for x in range(169, 10 ** 9 + 1, 169):
#     if re.fullmatch('123.*567.', str(x)) is not None:
#         print(x, x // 169)



f = open('27.txt')
N = int(f.readline())
k = s = 0
a = [float('inf')] * 30
m = -float('inf')
for i in range(N):
    x = int(f.readline())
    s += x
    if x % 2 == 0 and x > 0:
        k += 1
    if k % 30 == 0:
        m = max(m, s)
    m = max(m, s - a[k % 30])
    a[k % 30] = min(a[k % 30], s)
print(m)

# from itertools import permutations
#
#
# def u(a, b, c, d):
#     return ((a and b) == (not c)) and (b <= d)
#
#
# t = (
#     (1, 0, 0, 0, 1),
#     (1, 0, 1, 0, 1),
#     (1, 0, 1, 1, 1),
#     (1, 1, 0, 0, 1),
# )
# if len(t) == len(set(t)):
#     for p in permutations('abcd', r=4):
#         if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#             print(*p)


# def f(N):
#     n = bin(N)[2:]
#     if n.count('1') % 2 == 0:
#         n += '1'
#     else:
#         n += '0'
#     n += str((n.count('1') % 2))
#     return int(n, 2)
#
# N = 1
# while True:
#     if f(N) > 31:
#         print(f(N))
#         break
#     N += 1


# from turtle import *
#
# tracer(0)
# up()
#
# m = 12
# goto(0 * m, -10 * m)
#
# down()
# for _ in range(20):
#     for _ in range(4):
#         fd(15 * m)
#         rt(90)
#     bk(20 * m)
#     rt(90)
#
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * m, y * m)
#         dot(4, 'black')
# update()
# input()


# from itertools import product
#
# k = 0
# for x in product('ABCWXYZ', repeat=6):
#     s = ''.join(x)
#     if s[0] in 'WXYZ' and s[-1] in 'WXYZ' and all(s[x] not in 'WXYZ' for x in range(1, 5)):
#         print(s)
#         k += 1
# print(k)


# f = open('9.csv').readlines()
#
# k = 0
# for x in f:
#     x = list(map(int, x.split('	')))
#     a1 = set()
#     a2 = set()
#     n = 0
#     for s in x:
#         if x.count(s) == 2:
#             a1.add(s)
#             n += 1
#         elif x.count(s) == 1:
#             a2.add(s)
#     if n >= 2:
#         if all(x > y for x in a1 for y in a2):
#             k += 1
# print(k)


# x = 16 ** 20 + 2 ** 30 - 32
#
# k = 0
# while x > 0:
#     if x % 4 == 3:
#         k += 1
#     x //= 4
# print(k)

# p1, p2, q1, q2 = 23, 45, 34, 56
# p = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
# q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
#
#
# def f(x, a):
#     return (x not in a) or (x not in p) and (x in q)
#
#
# a = set([i / 10 for i in range(20 * 10, 60 * 10 + 1)])
# for x in [i / 10 for i in range(20 * 10, 60 * 10 + 1)]:
#     if not f(x, a):
#         a.remove(x)
# print(sorted(a))
# import functools
#
#
# @functools.lru_cache(None)
# def f(n):
#     if n == 1:
#         return 1
#     if n % 2 == 0 and n >= 2:
#         return f(n / 2) + 1
#     if n % 2 != 0 and n >= 2:
#         return f(n - 1) + n
#
#
# print(f(448))


# f = list(map(int, open('17.txt')))
# k = 0
# m = -float('inf')
# for i in range(len(f) - 1):
#     for j in range(i, len(f)):
#         if (f[i] + f[j]) % 120 == 0:
#             k += 1
#             m = max(m,f[i] + f[j])
# print(k, m)


# def f(s1, s2, c, m):
#     if s1 + s2 >= 133: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s1 + 1, s2, c + 1, m), f(s1, s2 + 1, c + 1, m), f(s1 * 4, s2, c + 1, m), f(s1, s2 * 4, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 125):
#     for m in range(1, 5):
#         if f(7, s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break

# time = {'0': 0}
# for s in open('22.txt'):
#     s = s.replace('', ' ')
#     s = s.split('	')
#     print(s)
#     time[s[0]] = int(s[1]) + max(time[i] for i in s[2:])
# print(max(time.values()))

# import sys
# import functools
#
# sys.setrecursionlimit(9999999)
#
#
# @functools.lru_cache(None)
# def f(x, end):
#     if x < end: return 0
#     if x == end: return 1
#     return f(int(str(x), 2) - 1, end) + f(x // 10, end)
#

# print(f(100001, 100))


def f(x):
    a = set()
    for d in range(1, int(x ** 0.5)):
        if x % d == 0:
            a.add(d)
            a.add(x // d)
    return a


# start, end = 194441, 196500
#
# k = 0
# for x in range(start, end + 1):
#     k += 1
#     # if len(f(x)) % 2 != 0:
#     for i in f(x):
#         # if i ** 2 == x:
#         print(k, x, len(f(x)), i)






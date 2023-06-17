# print('w z y x')
#
# for x in 0,1:
#     for y in 0, 1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (x and (not y)) or (y == z) or (not w)
#                 if not f:
#                     print(w, z, y, x, f)


# for i in range(0, 1000):
#     s = bin(i)[2:]
#     if s.count('1') > s.count('0'):
#         s += '1'
#     elif s.count('1') <= s.count('0'):
#         s += '0'
#
#     if int(s, 2) > 80:
#         print(i)
#         break

# from turtle import *
#
# m = 15
# tracer(0)
#
# for _ in range(4):
#     fd(10 * m)
#     rt(90)
#
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(4, 'black')
# update()
# input()

# from itertools import product
#
# k = 0
# for x in product("ABCX", repeat=5):
#     s = ''.join(x)
#     if (s[0] == 'X' and s.count('X') == 1 ) or (s.count('X') == 0):
#         print(s)
#         k += 1
# print(k)

# f = open('9.csv')
# c = 0
# for a in f:
#     s = list(map(int, a.split('	')))
#     count = 0
#     d = set()
#     t = set()
#     print(s)
#     for x in s:
#         if s.count(x) == 2:
#             count += 1
#             d.add(x)
#         elif s.count(x) == 1:
#             t.add(x)
#     if count >= 2:
#         if all(i > j for i in d for j in t):
#             c += 1
# print(c)

# s = '1' + '9' * 98
#
# while ('19' in s) or ('299' in s) or ('3999' in s):
#     s = s.replace('19', '2')
#     s = s.replace('299', '3')
#     s = s.replace('3999', '1')
# print(s)

# x = 25 ** 5 + 5 ** 14 - 5
#
# k = 0
# while x > 0:
#     if x % 5 == 4:
#         k += 1
#     x //= 5
# print(k)

# p1, p2, q1, q2 = 12, 62, 52, 92
#
# p = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
# q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
#
#
# def f(x, a):
#     return (not((not (x in a)) and (x in p)) ) or (x in q)
#
#
# a = set()
# for x in [i / 10 for i in range(5 * 10, 100 * 10)]:
#     if not f(x, a):
#         a.add(x)
# print(sorted(a))

# m = -float('inf')
# f = list(map(int, open('17.txt')))
# count = 0
#
# for x in range(0, len(f) - 1):
#     for y in range(x, len(f)):
#         if (f[x] * f[y]) % 26 == 0:
#             count += 1
#             m = max(m, f[x] + f[y])
# print(count, m)


# def f(a, b, c, m):
#     if a + b >= 63: return m % 2 == c % 2
#     if m == c: return 0
#     h = [f(a + 1, b, c + 1, m), f(a, b + 1 , c + 1, m), f(a * 2, b, c + 1, m), f(a, b * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 58):
#     for m in range(1, 5):
#         if f(5, s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break


# f = open('22.txt')
# a = {'0': 0}
#
# for x in f:
#     x = x.replace(';', ' ')
#     x = x.split()
#     a[x[0]] = int(x[1]) + max(a[i] for i in x[2:])
# print(max(a.values()))

# import re
#
# count = 0
# x = 1
#
#
# def d(x):
#     a = set()
#     for i in range(1, int(x ** 0.5)):
#         if x % i == 0:
#             a.add(i)
#             a.add(x // i)
#     return sum(a)
#
# while count != 7:
#     if re.fullmatch('.6.*6..*6', str(x)) is not None:
#         if (x % 6 == 0) and (x % 7 == 0) and (x % 8 == 0):
#             print(x, d(x))
#             count += 1
#     x += 1

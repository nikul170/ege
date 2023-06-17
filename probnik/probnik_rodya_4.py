# from itertools import *
#
# # ((y → x) ≡ (x → w)) ∧ (z ∨ x).
# def u(x, y, z, w):
#     return ((y <= x) == (x <= w)) and (z or x)
#
#
# for x1,x2,x3,x4,x5,x6 in product([0,1], repeat=6):
#     t = (
#         (0, x1, x2, 0, 1),
#         (0, 0, 0, x3, 1),
#         (x4, x5, 0, x6, 1),
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)



# def f(N):
#     n = bin(N)[2:]
#     if N % 2 == 0:
#         n += '10'
#     else:
#         n += '01'
#     return int(n, 2)
#
#
# for N in range(1, 303):
#     if f(N) <= 102:
#         print(f(N))



# from turtle import *
#
# tracer(0)
# m = 15
#
# for _ in range(4):
#     fd(12 * m)
#     rt(90)
# # for _ in range(3):
# #     fd(12 * m)
# #     rt(120)
#
#
# up()
# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * m, y * m)
#         dot(2, 'black')

# update()
# input()


# from itertools import *
#
# k = 0
#
# for x in permutations('КУСАТЬ', r=5):
#     a = ''.join(x)
#     if a[0] != 'Ь' and 'СУК' not in a:
#         k += 1
#         print(len(set(a)), a[0] != 'Ь','СУК' not in a)
# print(k)

#
# f = open('9.csv').readlines()
# k = 0
#
# for x in f:
#     a = sorted(list(map(int, x.split('	'))))
#     if (a[2] ** 2) > (2 * (a[0] * a[1])):
#         k += 1
# print(k)

# k = 0
# for x in range(1000, 10000):
#     k += 1
#     print(x)
# print(k)


# s = '1' + '9' * 100
#
# while ('19' in s) or ('299' in s) or ('3999' in s):
#     if ('19' in s):
#         s = s.replace('19', '2', 1)
#     if ('299' in s):
#         s = s.replace('299', '3', 1)
#     if ('3999' in s):
#         s = s.replace('3999', '1', 1)
# print(s)

# for y in '0123456789A':
#     for x in '0123456789A':
#         try:
#             if (int(y + '04' + x + '5', 11) + int('253' + x + y, 8)) % 117 == 0:
#                 print((int(y + '04' + x + '5', 11) + int('253' + x + y, 8)) // 117)
#         except:
#             pass


# def f(x, y, a):
#     return (x * y < 2 * a) or (x >= 11) or (x < 2 * y)
#
#
# print(min(a for a in range(-100, 100) if all(f(x, y, a) for x in range(1, 1000) for y in range(1, 1000))))



# def f(n):
#     if n == 1: return 3
#     if n == 2: return 3
#     if n > 2:
#         return 5 * f(n - 1) - 4 * f(n - 2)
#
#
# print(f(15))


# a = list(map(int, open('17.txt')))
# max_dig = max(i for i in set(a) if i % 2 != 0)
# min_dig = min(i for i in set(a) if i % 2 != 0)
# m = float('inf')
# k = 0
#
# for i in range(len(a) - 1):
#     if ((a[i] + a[i + 1]) % 2 == 0) and ((a[i] + a[i + 1]) > (min_dig + max_dig)):
#         k += 1
#         m = min(m, a[i] + a[i + 1])
# print(k, m)


# def f(s, c, m):
#     if 50 <= s <= 119: return c % 2 == m % 2
#     if s > 119: return c % 2 != m % 2
#     if c == m: return 0
#     h = [f(s + 2, c + 1, m), f(s * 3, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else any(h)
#
# a = set()
# for s in range(1, 50):
#     for m in range(1, 5):
#         if f(s, 0,m):
#             if m == 2:
#                 a.add(s)
#                 print(s, m)
#             break
# print(len(a))



# def f(x, end, step1, step2):
#     a = []
#     if x > end: return 0
#     if x == end: return 1
#     if step1 == '+1' and step2 == '+1': a += [f(x + 2, end, '+2', step1), f(x * 2, end, '*2', step1)]
#     else: a += [f(x + 1, end, '+1', step1), f(x + 2, end, '+2', step1), f(x * 2, end, '*2', step1)]
#     return sum(a)
#
#
# print(f(2, 12, '', ''))


# a = open('24.txt').readline()
# m = -float('inf')
# k = 0
# c = dict()
# count = 1
# for x in set(a):
#     c[x] = 0
# for i in range(len(a) - 2):
#     j = i + 2
#     while a[j] != a[i] and (j != len(a) - 1):
#         j += 1
#     count += 1
#     for x in set(a[i + 1: j]):
#         c[x] += (a[i + 1: j]).count(x)
#
# m = max(c.values())
# for x in c.keys():
#     if c[x] == m:
#         print(x)
#         break



# n = 103
# while True:
#     x = str(n)
#     if all(x[i] < x[i + 1] for i in range(len(x) - 1)):
#         print(n, n // 103)
#     n += 103




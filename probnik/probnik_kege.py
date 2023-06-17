# from itertools import product, permutations
#
# def u(x, y, w, z):
#     return (x or (not y)) and (not(x == z)) and w
#
#
# for x1,x2,x3,x4 in product([0, 1], repeat=4):
#     t = (
#         (x1, x2, 0, 0, 1),
#          (1, 0, 0, 1,1),
#          (1, 0, x3, x4, 1)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xywz', r=4):
#             if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                 print(*p)


# def f(x):
#     x = str(x)
#     s1 = int(int(x[0]) * int(x[1]))
#     s2 = int(int(x[1]) * int(x[2]))
#     return str(max(s1, s2)) + str(min(s1, s2))
#
#
# for x in range(100, 1000):
#     if int(f(x)) == 240:
#         print(f(x), x)


# from turtle import *
#
# tracer(0)
# m = 15
#
# for _ in range(13):
#     fd(10 * m)
#     rt(90)
#     fd(10 * m)
#     rt(90)
#     fd(30 * m)
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
# for x in product('КАНТ', repeat=6):
#     s = ''.join(x)
#     if s.count('К') == 2:
#         k += 1
#         print(s)
# print(k)

#
# s = 'А' * 50 + "Б" * 110 + "В" * 100
#
# while 'АБ' in s or 'ВА' in s or 'ВБ' in s:
#     s = s.replace('ВА', 'АБ', 1)
#     s = s.replace('АБ', 'БА', 1)
#     s = s.replace('ВБ', 'БВ', 1)
# print(s[43], s[112], s[253])


x = 3 * 5 ** 1984 - 7 * 25 ** 777 - 11 * 125 ** 666 - 404
k = 0

while x > 0:
    if x % 5 == 2:
        k += 1
    x //= 5
print(k)


# def f(x, a):
#     return (not (x in a)) <= x not in [1,2,3,4] or x not in [1,2,3,4,5,6]
#
#
# a = set(range(0, 20))
# for x in range(0, 20):
#     if f(x, a):
#         a.remove(x)
# print(sorted(a))
# import functools
#
# @functools.lru_cache(None)
# def g(n):
#     if n <= 0:
#         return 2
#     if n > 0 and n % 2 != 0:
#         return f(n - 1) - 2 * g(n - 2)
#     if n > 0 and n % 2 == 0:
#         return 2 * f(n - 2) - 2 * g(n - 1)
#
# @functools.lru_cache(None)
# def f(n):
#     if n <=2:
#         return 1
#     if n > 2 and n % 2 != 0:
#         return f(n - 1) - n
#     elif n > 2 and n % 2 == 0:
#         return f(n - 2) + g(n - 1) + 2
#
# print(f(96))
# f = open('17.txt').readlines()
# k = 0
# m = - float('inf')
# for x in f:
#     if x.count('0') >= 2 and int(x) % 7 == 0:
#         m = max(m, int(x))
#         k += 1
# print(9009 % 7)


# def f(s1, s2, c, m):
#     if s1 + s2 >= 59: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s1 + 2, s2, c + 1, m), f(s1, s2 + 2, c + 1, m), f(s1 * 2, s2, c + 1, m), f(s1, s2 * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 54):
#     for m in range(1, 5):
#         if f(5, s, 0, m):
#             if m == 3:
#                 print(s, m)
#             break

# time = {'0':0}
# for s in open('22.txt'):
#     s = s.replace(';', ' ')
#     s = s.split()
#     print(s)
#     time[s[0]] = int(s[1]) + max(time[i] for i in s[2:])
# print(time.values())

# def f(x, end):
#     if x > end: return 0
#     if x == end: return 1
#     return f(x + 1, end) + f(x + 2, end) + f(x * 2, end)
#
#
# print(f(4, 9) * f(9, 12) * f(12, 15))


def f(x):
    a = set()
    for d in range(1, int(x ** 0.5) + 1):
        if x % d == 0:
            if d % 2 == 0:
                a.add(d)
            if (x // d) % 2 == 0:
                a.add(x // d)

    return sorted(a)


x, y = 190201, 190260

for i in range(x, y + 1):
    if len(f(i)) == 4:
        print(f(i)[-1], f(i)[-2])




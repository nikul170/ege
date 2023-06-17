# print('z y x w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = ((not x) and (not y)) or (y == z) or (not w)
#                 if f == 0:
#                     print(z,y,x,w)

# def f(N):
#     n = bin(N)[2:].zfill(8)
#     n = n.replace('1', '2').replace('0', '1').replace('2', '0')
#     return int(n, 2) - N
#
# for N in range(0, 256):
#     print(f(13))
#     if f(N) == 111:
#         print(N)
#         print()

# from turtle import *
#
# m = 20
# tracer(0)
#
# for _ in range(4):
#     fd(6 * m)
#     rt(150)
#     fd(6 * m)
#     rt(30)
#
# up()
#
# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x * m, y * m)
#         dot(2, 'black')
# update()
# input()

# from itertools import product
#
# i = 0
# k = 0
# for x in product('АЕЖЙМУ', repeat=5):
#     i += 1
#     s = ''.join(x)
#     if i % 2 == 0 and all(j not in s for j in ['АА', "ЕЕ", "ЖЖ", "ЙЙ", "ММ", "УУ"]):
#         k += 1
#         print(s, i)
# print(k)


# f = open('9.csv').readlines()
# k = 0
# for a in f:
#     x = sorted(list(map(int, a.split('	'))))
#     if ((x[0] + x[4]) ** 3 )> (x[1] ** 3 + x[2] ** 3 + x[3] ** 3):
#         k += 1
# print(k)

# s = '1' + '0' * 75
#
# while ('10' in s) or ('1' in s):
#     if '10' in s:
#         s = s.replace('10', '001', 1)
#     else:
#         s = s.replace('1', '00', 1)
#
# print(s.count('0'))


# x = 7 * 512 ** 120 - 6 * 64 ** 100 + 8 ** 210
#
# k = 0
# while x > 0:
#     if x % 8 == 0:
#         k += 1
#     x //= 8
# print(k)

# def d(n, m):
#     return n % m == 0
#
#
# def f(x, a):
#     return (d(x, 34) and (not d(x, 51))) <= ((not d(x, a)) or d(x, 51))
#
#
# print(min(a for a in range(1, 100) if all(f(x,a) for x in range(1, 1000))))

# def f(s1, s2, c, m):
#     if s1 + s2 >= 79: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s1 + 2, s2, c + 1, m),f(s1, s2 + 2, c + 1, m), f(s1 * 2, s2, c + 1, m), f(s1, s2 * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 70):
#     for m in range(1, 5):
#         if f(9, s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break



# a = {'0': 0}
#
# for s in open('22.txt'):
#     s = s.replace(';', ' ')
#     s = s.split()
#     a[s[0]] = int(s[1]) + max(a[i] for i in s[2:])
# print(max(a.values()))

# f = open('24.txt').readlines()
#
# k = 0
# for x in f:
#     if x.count('E') > x.count('A'):
#         k += 1
# print(k)

def f(n):
    a = set()
    for x in range(1, int(n ** 0.5) + 1):
        if n % x == 0:
            a.add(x)
            a.add(n // x)
    return len(a)


start, end = 84052, 84130

a = {}
for x in range(start, end + 1):
    a[x] = f(x)
print(max(a.values()))

for x in a.keys():
    if a[x] == max(a.values()):
        print(x, a[x])


# from itertools import *
#
#
# def u(x, y,z ,w):
#      return w and ((x <= y) == (y <= z))
#
#
# for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
#      t = (
#           (0, x1, x2, x3, 1),
#           (0, 0, x4, 0, 1),
#           (0, x5, x6, 0, 1)
#      )
#      if len(t) == len(set(t)):
#           for p in permutations('xyzw', r=4):
#                if all(u(**dict(zip(p, r))) == r[-1] for r in t):
#                     print(*p)


# def f(N):
#      n = bin(N)[2:]
#      if N % 2 == 0:
#           n += '01'
#      else:
#           n += '10'
#      return int(n, 2)
#
#
# N = 1
# print(bin(7)[2:], bin(f(7))[2:])
# while True:
#      if f(N) < 125:
#           print(f(N))
#      N += 1


# from turtle import *
#
# tracer(0)
# m = 1
#
# for _ in range(100):
#      fd(10 * m)
#      rt(8)
#
# update()
# input()


# from itertools import *
#
# k = 0
# for x in product('АБВГ', repeat=5):
#      x = ''.join(x)
#      if x.count('А') == 1:
#           k += 1
# print(k)

# f = open('9.txt')
# count = 0
#
# for line in f:
#      a = list(map(int, line.split()))
#      if not(((a[2] > a[0]) and (a[3] < a[1])) or ((a[2] < a[0]) and (a[3] < a[1]))):
#           count += 1
# print(count)


for i in range(100, 100000):
     s = '1' * i
     while '111' in s:
         s = s.replace('111', '2', 1)
         s = s.replace('2222', '333', 1)
         s = s.replace('33', '1', 1)
     if s.count('1') == 0:
          print(i)
          break


# x = 4 ** 625 - 2 ** 311 + 2 ** 571 - 48
# k = 0
# while x > 0:
#      if x % 4 == 1:
#           k += 1
#      x //= 4
# print(k)


# def f(x, a):
#      return (x in [12, 23, 34, 45, 56]) or (x in [23, 35, 56, 68, 89]) or (x not in a)
#
#
# a = set(range(10, 90))
# for x in range(10, 95):
#      if not f(x, a):
#           a.remove(x)
# print(len(a))


def f(n):
     if n <= 3:
          return 3
     if n > 3 and n % 2 == 0:
          return f(n // 2) + 5
     if n > 3 and n % 2 != 0:
          return f(n - 1) - f(n - 2)

print(f(20))


# a = list(map(int, open('9.txt')))
# k = 0
# m = -float('inf')
# ma = max(i for i in set(a) if i % 11 == 0)
#
# for i in range(len(a) - 1):
#      if ((abs(a[i]) % 11 == 0) or (abs(a[i + 1]) % 11 == 0)) and (a[i] + a[i + 1] <= ma):
#           k += 1
#           m = max(m, a[i] + a[i + 1])
# print(k, m)


# def f(a, b, c, m):
#      if a + b >= 59: return c % 2 == m % 2
#      if c == m: return 0
#      h = [f(a + 1, b, c + 1, m), f(a * 2, b, c + 1, m), f(a, b + 1, c + 1, m), f(a, b * 2, c + 1, m),]
#      return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(2, 53):
#      for m in range(1, 5):
#           if f(s, 5, 0, m):
#                if m == 4:
#                     print(s)
#                break



# def f(x, end):
#      if x > end or x == 6 or x == 12: return 0
#      if x == end: return 1
#      return f(x + 1, end) + f(x * 2, end) + f(x + 3, end)
#
#
# print(f(3, 16))


a = open('9.txt').readline().replace('C', 'B').replace('D', 'B').replace('F', 'B').replace('U', 'B').replace('E', 'A')
# k = 0
# m = -float('inf')
# for i in range(5, len(a) - 5, 6):
#     if a[i: i + 6] == 'BABBAB':
#         k += 6
#         m = max(m, k)
#     else:
#         k = 0
# print(m)

# def f(x):
#     a = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             a.add(d)
#             a.add(x // d)
#     return a
#
#
#
# for x in range(201455, 201470):
#     if len(f(x)) == 4:
#         print(*sorted(f(x)))


# a = list(map(int, open('9.txt')))
# s = [i for i in a if i % 5 == 0]
# n = [i for i in a if i not in s]
# k = 0
#
# for i in s:
#     for j in a:
#         if ((i + j) % 2 != 0) and i != j:
#             k += 1
# print(k)
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if ((a[i] * a[j]) % 5) == 0 and (a[i] + a[j]) % 2 != 0:
#             k += 1
# print(k)


a = open('9.txt').readline().replace('C', 'B').replace('D', 'B').replace('F', 'B').replace('U', 'B').replace('E', 'A')
a = a.split('BAB')
m = -float('inf')
for i in range(len(a) - 1):
    m = max(m, len(a[i]) + len(a[i + 1]) + 6)
print(m)
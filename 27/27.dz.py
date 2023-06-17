# f = open('27.txt')
# N = int(f.readline())
# s = [0]
# c = 0
# for i in range(N):
#     pair = list(map(int, f.readline().split()))
#     c += max(pair[0], pair[1])
#     cmb = [a + b for a in pair for b in s]
#     s = {x % 10: x for x in sorted(cmb, reverse=True)}.values()
# print(min(x for x in s if x % 10 == c % 10))


# f = open('27.txt')
# N = int(f.readline())
# a = [0] * 7
# count = 0
#
# for i in range(N):
#     x = int(f.readline())
#     for y in range(7):
#         if (x * y) % 7 == 0:
#             count += a[y]
#     a[x % 7] += 1
# print(count)


# f = open('27.txt')
# N = int(f.readline())
# s = 0
# a = [float('inf')] * 1000
# max_s = 0
# for i in range(N):
#     x = int(f.readline())
#     s += x
#     ost = s % 1000
#     if a[ost] != float('inf'):
#         if s - a[ost] > max_s:
#             max_s = s - a[ost]
#     if s < a[ost]:
#         a[ost] = s
# print(max_s)


# f = open('27.txt')
# N = int(f.readline())
# s = [0]
#
# for i in range(N):
#     pair = list(map(int, f.readline().split()))
#     cmb = [a + b for a in pair for b in s]
#     s = {x % 5: x for x in sorted(cmb)}.values()
# print(max(x for x in s if x % 5 != 0))


# f = open('27.txt')
# N, K, D = list(map(int, f.readline().split()))
# s = 0
# min_s = [float('inf')] * K * D
# min_k = [float('inf')] * K * D
# m = 0
# k = 0
#
# for i in range(N):
#     x = int(f.readline())
#     s += x
#     ost = s % (K * D)
#     k += 1
#     if min_s[ost] != float('inf'):
#         if s - min_s[ost] > m and (min_k[ost] % 2 != 0):
#             m = s - min_s[ost]
#     if s < min_s[ost]:
#         min_s[ost] = s
#
# print(m)


# f = open('27.txt')
# N = int(f.readline())
# a = [float('inf')] * 31
# m = float('inf')
# 
# for i in range(N):
#     x = int(f.readline())
#     for y in range(31):
#         if (x * y) % 31 == 0:
#             m = min(m, x * a[y])
#     if x < a[x % 31]:
#         a[x % 31] = x
# print(m)


# f = open('27.txt')
# N, K, D = list(map(int, f.readline().split()))
# s = 0
# a = []
# k = []
# count = 0
# max_s = 0
# for i in range(N):
#     x = int(f.readline())
#     s += x
#     count += 1
#     if s % K == 0:
#         a.append(s)
#         k.append(count)
#         print('x')
# for i in range(len(a)):
#     if (s - a[i]) % D == 0 and (count - k[i]) % 2 != 0 and max_s < s:
#         max_s = a[i]
# print(max_s)


# f = open('27.txt')
# N = int(f.readline())
# a = [0] * 10
# count = 0
# for i in range(N):
#     x = int(f.readline())
#     for y in range(10):
#         if (x * y) % 5 == 0 and (x + y) % 2 != 0:
#             count += a[y]
#     a[x % 10] += 1
# print(count)

# f = open('27.txt')
# N = int(f.readline())
#
# a = [float('inf')] * 93
# s = 0
# max_s = 0
#
# for i in range(N):
#     x = int(f.readline())
#     s += x
#     ost = s % 93
#     if a[ost] != float('inf'):
#         if (s - a[ost]) % 2 != 0:
#             if (s - a[ost]) > max_s:
#                 max_s = s - a[ost]
#     if s < a[ost]:
#         a[ost] = s
# print(max_s)


# f = open('27.txt')
# N = int(f.readline())
# count = 0
# a = [0] * 134
#
# for i in range(N):
#     x = int(f.readline())
#     if x >= 134:
#         continue
#     for y in range(134):
#         if (x + y) <= 134 and y > x:
#             count += a[y]
#     a[x] += 1
# print(count)


# f = open('27.txt')
# N = int(f.readline())
# count = 0
# a = [0] * 69
#
#
# for i in range(N):
#     x = int(f.readline())
#     for y in range(69):
#         if (x - y) % 69 == 0:
#             count += a[y]
#     a[x % 69] += 1
# print(count)

# f = open('27.txt')
# N = int(f.readline())
#
# a = [0, 0]
# a1 = [0, 0]
# count = 0
#
# for i in range(N):
#     x = int(f.readline())
#     if x == 0:
#         a[0] = a1[0]
#         a[1] = a1[1]
#     else:
#         count += a[x % 2]
#         a1[x % 2] += 1
# print(count)


# f = open('27.txt')
# N = int(f.readline())
# a = [0] * 120
# m = -float('inf')
# for i in range(N):
#     x = int(f.readline())
#     for y in range(120):
#         if (x + y) % 120 == 0 and x < a[y]:
#             if x + a[y] > m:
#                 m = x + a[y]
#                 m1, m2 = x, a[y]
#     if x > a[x % 120]:
#         a[x % 120] = x
# print(m2, m1)


# f = open('27.txt')
# N = int(f.readline())
#
# s = 0
# a = [float('inf')] * 1000
# m = -float('inf')
# for i in range(N):
#     x = int(f.readline())
#     s += x
#     print(s % 1000 == 0)
#     ost = s % 1000
#     if a[ost] != float('inf') and s - a[ost] > m:
#         m = s - a[ost]
#     if s < a[ost]:
#         a[ost] = s
# print(m)


# f = open('27.txt')
# N = int(f.readline())
# a = [0] * 62
# count = 0
# for i in range(N):
#     x = int(f.readline())
#     for y in range(62):
#         if (x * y) % 62 == 0:
#             count += a[y]
#     a[x % 62] += 1
# print(count)


# f = open('27.txt')
# N = int(f.readline())
# m = float('inf')
# a = [float('inf')] * 31
#
# for i in range(N):
#     x = int(f.readline())
#     for y in range(31):
#         if (x * y) % 31 == 0:
#             m = min(m, x * a[y])
#     a[x % 31] = min(a[x % 31], x)
# print(m)


# def is_prime(x):
#     for d in range(2, int(x ** 0.5) + 1):
#         if x % d == 0:
#             return False
#     return True
#
#
# def d(x):
#     a = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             if is_prime(d):
#                 a.add(d)
#             if is_prime(x // d):
#                 a.add(x // d)
#     a.remove(1)
#     return a
#
#
# f = open('27.1.txt')
# N, K = map(int, f.readline().split())
# s = 1
# l = set()
# a = []
# count = 0
#
# for i in range(N):
#     x = int(f.readline())
#     a.append(x)
#
# i = 0
# while len(l) < K:
#     l = l | d(a[i])
#     count += 1
#     i
# print(count)




# f = open('27.txt')
# N = int(f.readline())
#
# m1 = m3 = m5 = m15 = -float('inf')
# m = -float('inf')
#
# for i in range(N):
#     x = int(f.readline())
#     if x % 15 == 0 and x % 9 != 0:
#         m = max(m, x * m1, x * m3, x * m5, x * m15)
#         m15 = max(m15, x)
#     elif x % 3 == 0 and x % 9 != 0:
#         m = max(m, x * m15, x * m5)
#         m3 = max(m3, x)
#     elif x % 5 == 0 and x % 9 != 0:
#         m = max(m, x * m15, x * m3)
#         m3 = max(m5, x)
#     elif x % 9 != 0 and x % 1 == 0:
#         m = max(m, x * m15)
#         m1 = max(m1, x)
# print(m)

# a = [-float('inf')] * 45
# m = -float('inf')
# for i in range(N):
#     x = int(f.readline())
#     for y in range(45):
#         if x * y % 15 == 0 and x * y % 9 != 0:
#             m = max(m, x * a[y])
#     a[x % (45)] = max(x % (45), x)
# print(m)


# f = open('27.1.txt')
# N = int(f.readline())
# a = [-float('inf')] * 2
#
# for i in range(N):
#     x = int(f.readline())
#     a[x % 2] = max(a[x % 2], x)
# print(a[0] + a[1])


f = open('27.1.txt')
N = int(f.readline())
a = [0] * 80
b = [0] * 80
count = 0

for i in range(N):
    x = int(f.readline())
    for y in range(80):
        if ((x + y) % 80 == 0) and (x > 50):
            count += a[y]
        elif ((x + y) % 80 == 0) and (b[y] != 0):
            count += b[y]
    a[x % 80] += 1
    if x > 50:
        b[x % 80] += 1
print(count)


# f = open('27.1.txt')
# N = int(f.readline())
# a = [-float('inf')] * 3
# m = -float('inf')
#
#
# for i in range(N):
#     x = int(f.readline())
#     for y in range(3):
#         if (x + y) % 3 == 0:
#             m = max(m, x + a[y])
#     a[x % 3] = max(a[x % 3], x)
# print(m)

# f = open('27.1.txt')
# N = int(f.readline())
# a = [-float('inf')] * 2
# m = -float('inf')
# c = [0]
# m1 = m2 = -float('inf')
# for i in range(N):
#     x = int(f.readline())
#     if x % 17 == 0:
#         m1, m2 = max(m, x), max(m, a[x % 2])
#     if x % 17 != 0:
#         m1, m2 = max(m, x), max(c)
#     if x % 17 == 0:
#         c.append(x)
#     a[x % 2] = max(a[x % 2], x)
# print(m1, m2)
















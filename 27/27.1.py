# f = open('27.txt')
# N = int(f.readline())
#
# c1 = c2 = c31 = c62 = 0
# for i in range(N):
#     x = int(f.readline())
#     if x % 62 == 0:
#         c62 += 1
#     elif x % 31 == 0:
#         c31 += 1
#     elif x % 2 == 0:
#         c2 += 1
#     else:
#         c1 += 1
# count = c2 * c31 + c62 * (c1 + c2 + c31) + (c62 * (c62 - 1)) / 2
# print(count)
#count = c2 * c7 + c14 * (N - c14)


# f = open('27.txt')
# N = int(f.readline())
# count = 0
# c1 = c2 = c31 = c62 = 0
# for i in range(N):
#     x = int(f.readline())
#     if x % 62 == 0:
#         count = c1 + c2 + c31 + c62
#         c62 += 1
#     elif x % 31 == 0:
#         count += c2 + c62
#         c31 += 1
#     elif x % 2 == 0:
#         count += c31 + c62
#         c2 += 1
#     else:
#         count += c62
#         c1 += 1
# print(count)


# f = open('27.txt')
# N = int(f.readline())
# m = -float('inf')
# m1 = m2 = m7 = m14 = -float('inf')
# for i in range(N):
#     x = int(f.readline())
#     if x % 14 == 0:
#         m = max(m, x * m1, x * m2, x * m7, x * m14)
#         m14 = max(x, m14)
#     elif x % 7 == 0:
#         m = max(m, x * m2, x * m14)
#         m7 = max(x, m7)
#     elif x % 2 == 0:
#         m = max(m, x * m7, x * m14)
#         m2 = max(x, m2)
#     else:
#         m = max(m, x * m14)
#         m1 = max(x, m1)
# print(m)


# f = open('27.txt')
# N = int(f.readline())
#
# c = [-float('inf')] * 120
# m = -float('inf')
#
# for i in range(N):
#     x = int(f.readline())
#     ost = (120 - (x % 120)) % 120
#     if x < c[ost]:
#         if x + c[ost] > m:
#             m = x + c[ost]
#             c1, c2 = c[ost], x
#     if x > c[x % 120]:
#          c[x % 120] = x
# print(c1, c2)


f = open('27.txt')
N = int(f.readline())
c = 0
a = []

for _ in range(N):
    x = list(map(int, f.readline().split()))
    c += min(x[0], x[1])
    if (abs(x[0] - x[1]) % 3) != 0:
        a.append(abs(x[0] - x[1]))
if c % 3 == 0:
    print(c, 'w')
else:
    print(c + min(i for i in a if (c + i) % 3 == 0))





# f = open('27.txt')
# N = int(f.readline())
#
# a = [0] * 62
# count = 0
#
# for i in range(N):
#     x = int(f.readline())
#     for y in range(62):
#         if (x * y) % 62 == 0:
#             count += a[y]
#     a[x % 62] += 1
# print(count)
#





# f = open('27.txt')
# N = int(f.readline())
# m1 = m2 = m13 = m26 = 0
# c = 0
#
# for _ in range(N):
#     x = int(f.readline())
#     if x % 26 == 0:
#         c += m1 + m2 + m13 + m26
#         m26 += 1
#     elif x % 13 == 0:
#         c += m2 + m26
#         m13 += 1
#     elif x % 2 == 0:
#         c += m13 + m26
#         m2 += 1
#     else:
#         c += m26
#         m1 += 1
# print(c)


# f = open('27.txt')
# N = int(f.readline())
# c = [-float('inf')] * 120
# m = - float('inf')
#
# for _ in range(N):
#     x = int(f.readline())
#     ost = (120 - (x % 120)) % 120
#     if x < c[ost]:
#         if x + c[ost] > m:
#             m = x + c[ost]
#             c1, c2 = x, c[ost]
#     if x > c[x % 120]:
#         c[x % 120] = x
# print(c2, c1)


# f = open('27.txt')
# N = int(f.readline())
# m1 = m31 = float('inf')
# a = []
#
# for _ in range(N):
#     x = int(f.readline())
#     a.append(x)
#     if x % 31 == 0:
#         m31 = min(m31, x)
# print(m31 * min(a))


f = open('27.txt')
N = int(f.readline())

s = [0]
for i in range(N):
    pair = list(map(int, f.readline().split()))
    cbm = [a + b for a in pair for b in s]
    s = {x % 3: x for x in sorted(cbm, reverse=True)}.values()

print(min(x for x in s if x % 3 == 0))


# f = open('27.txt')
# N = int(f.readline())
#
# min_s = [float('inf')] * 43
# min_l = [10 ** 10] * 43
# l = float('inf')
# max_s = 0
# s = 0
# for i in range(N):
#     x = int(f.readline())
#     s += x
#     ost = x % 43
#     if min_s[ost] != float('inf'):
#         if s - min_s[ost] > max_s or s - min_s[ost] == max_s and i - min_l[ost] < l:
#             max_s = s - min_s[ost]
#             l = i - min_l[ost]
#     if s < min_s[ost]:
#         min_s[ost] = s
#         min_l[ost] = i
# print(l)


# f = open('27.txt')
# N = int(f.readline())
#
# a = [0] * 14
# m = 0
#
# for i in range(N):
#     x = int(f.readline())
#     for y in range(14):
#         if (x * y) % 14 == 0:
#             m = max(m, x * a[y])
#     if x > a[x % 14]:
#         a[x % 14] = x
# print(m)









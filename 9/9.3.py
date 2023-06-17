# a = [list(map(int, a.split())) for a in open('9.csv')]
# k = 0
# for x in a:
#     x.sort()
#     d = set()
#     t = set()
#     for i in x:
#         if x.count(i) == 2:
#             d.add(i)
#         elif x.count(i) == 1:
#             t.add(i)
#     if len(d) >= 1 and  all(x1 > x2 for x1 in d for x2 in t):
#         k += 1
# print(k)

# f = open('9.csv')
# c = 0
#
# for s in f:
#     a = list(map(int, s.split('	')))
#     a = sorted(a)
#     if (a[0] * a[1] == a[2] * a[3] or a[1] * a[2] == a[0] * a[3] or a[1] * a[3] == a[0] * a[2]) and (a[2] ** 2 > a[0] * a[3]):
#         print(a)
#         c += 1
# print(c)

# f = open('9.csv')
# c = 0
#
# for s in f:
#     a = list(map(int, s.split('	')))
#     a = sorted(a)
#     if (a[3] ** 3) >= (2 * (a[0] * a[1] * a[2])) and all(x > 10 for x in a):
#         print(a)
#         c += 1
# print(c)

# f = open('9.csv')
# c = 0
#
# for s in f:
#     a = list(map(int, s.split('	')))
#     a = sorted(a)
#     if (sum(a) / len(a)) < ((a[0] + a[4]) / 2):
#         c += 1
# print(c)

# f = open('9.csv')
# 
# c = 0
# 
# for s in f:
#     a = list(map(int, s.split('	')))
#     a = sorted(a)
#     if (a[0] + a[4]) ** 2 > (a[1] ** 2 + a[2] ** 2 + a[3] ** 2):
#         c += 1
# print(c)

# import math
# f = open('9.csv')
#
# count = 0
# for line in f:
#     a = list(map(int, line.split()))
#     if ((a[0] / 10) ** 2 * math.pi * a[1] / 10) > 1000:
#         count += 1
# print(count)


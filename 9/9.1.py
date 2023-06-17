# f = open('9-170.csv').readlines()
# k = 0
# for line in f:
#     a = list(map(int, line.split(';')))
#     count = 0
#     for x in a:
#         if a.count(x) == 2:
#             count += 1
#             x1 = x
#     if count == 2 and len(set(a)) == 5:
#         if ((sum(a) - x1 - x1) / 4) <= (x1 + x1):
#             k += 1
# print(k)

# f = open('9-170.csv').readlines()
# k = 0
# for line in f:
#     a = list(map(int, line.split(';')))
#     count = 0
#     l = []
#     a1 = [n for n in a if a.count(n) == 1]
#     if len(a1) > 0:
#         for x in a:
#             if a.count(x) == 2:
#                 count += 1
#                 l.append(x)
#         if count >= 2 and all(y > max(a1) for y in l):
#             k += 1
#     elif len(a1) == 0 and any(a.count(y) == 2 for y in a):
#         k += 1
# print(k)



# f = open('9-170.csv').readlines()
# k = 0
# for l in f:
#     a = list(map(int, l.split(';')))
#     count = 0
#     for x in a:
#         if a.count(x) == 3:
#             count += 1
#             x1 = x
#     if count == 3 and len(set(a)) == 4:
#         if 3 * (sum(a) - 3 * x1) <= x1 ** 3:
#             k += 1
# print(k)

# f = open('9-170.csv').readlines()
# k = 0
# for l in f:
#     a = list(map(int, l.split(';')))
#     count1 = 0
#     s = 1
#     c = 1
#     count2 = 0
#     for x in a:
#         if a.count(x) == 1:
#             count1 += 1
#             s *= x
#         else:
#             c *= x
#             count2 += 1
#     if count1 == 2 and c ** (1 / count2) >= s:
#         k += 1
# print(k)

# f = open('9-170.csv').readlines()
#
# k = 0
# for l in f:
#     a = sorted(list(map(int, l.split(';'))))
#     if len(set(a)) == 6 and ((a[2] + a[3]) / 2) <= sum(a) / 6:
#         k += 1
# print(k)

# f = open('9-170.csv').readlines()
#
# k = 0
# for l in f:
#     maxi = -float('inf')
#     mini = float('inf')
#     a = list(map(int, l.split(';')))
#     count = 0
#     summ = 0
#     for x in a:
#         if a.count(x) == 2:
#             count += 1
#             summ += x
#         elif a.count(x) == 1:
#             maxi = max(maxi,x)
#             mini = min(mini, x)
#     print(maxi, mini, a)
#     if count == 2 and len(set(a)) == 5 and (maxi + mini) <= summ:
#         k += 1
# print(k)

# f = open('9-186.csv').readlines()
# k = 0
# for l in f:
#     a = list(map(int, l.split('	')))
#     count = 0
#     summ = 0
#     for x in a:
#         if a.count(x) > 1:
#             count += 1
#         if a.count(x) == 1:
#             summ += x
#     if count >= 2 and summ % 2 != 0:
#         k += 1
# print(k)


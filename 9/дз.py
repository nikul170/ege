# f = open('9.csv')
#
# count = 0
# for line in f:
#     a = list(map(int, line.split()))
#     p = []
#     pr = []
#     for x in a:
#         if a.count(x) == 3:
#             p.append(x)
#         if a.count(x) == 1:
#             pr.append(x)
#     if len(p) == 3 and len(pr) == 3 and (sum(pr) / len(pr)) <= sum(p):
#         count += 1
# print(count)


# f = open('9.csv')
#
# count = 0
# for line in f:
#     a = sorted(list(map(int, line.split())))
#     if a[-1] - a[0] >= 50 and a[1] * a[2] <= 1000:
#         count += 1
# print(count)


# f = open('9.csv')
#
# count = 0
# for line in f:
#     a = list(map(int, line.split()))
#     if any((a[i] * a[j]) % 10 == 4 for i in range(len(a) - 1) for j in range(i + 1, len(a))):
#         count += 1
# print(count)


# f = open('9.csv')
#
# count = 0
#
# for line in f:
#     a = list(map(int, line.split()))
#     p = []
#     pr = []
#     for x in a:
#         if a.count(x) == 2:
#             p.append(x)
#         if a.count(x) == 1:
#             pr.append(x)
#     if len(p) == 2 and len(pr) == 4 and (sum(pr) / len(pr)) <= sum(p):
#         count += 1
# print(count)


f = open('9.csv')

count = 0
for line in f:
    a = sorted(list(map(int, line.split())))
    p = [a[0] + a[1], a[1] + a[2], a[2] + a[3], a[0] + a[3]]
    if any(p[i] == p[j] for i in range(len(p) - 1) for j in range(i + 1, len(p))) and ((a[3] - a[0]) < (a[1] + a[2] - a[3])):
        print(a, p)
        count += 1
print(count)

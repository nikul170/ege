# f = open('9.csv')
# count = 0
#
# for line in f:
#     a = sorted(list(map(int, line.split())))
#     if len(a) == len(set(a)) and ((sum(a) / len(a)) >= (a[2] + a[3]) / 2):
#         count += 1
# print(count)

# f = open('9.csv')
# count = 0
#
# for line in f:
#     a = sorted(list(map(int, line.split())))
#     if all(x > 10 for x in a) and a[-1] ** 3 >= 2 * (a[0] * a[1] * a[2]):
#         count += 1
# print(count)


# f = open('9.csv')
# count = 0
#
# for line in f:
#     a = sorted(list(map(int, line.split())))
#     k = 0
#     for x in a:
#         if a.count(x) == 3:
#             k += 1
#     if ((a[-1] + a[0]) ** 2 > (a[1] ** 2 + a[2] ** 2 + a[3] ** 2 + a[4] ** 2)) or (len(set(a)) == 4 and k == 3):
#         count += 1
# print(count)



# f = open('9.csv')
# count = 0
#
# for line in f:
#     a = sorted(list(map(int, line.split())))
#     if (a[-1] - a[0] >= 50) and (a[1] * a[2] <= 1000):
#         count += 1
# print(count)


# f = open('9.csv')
# count = 0
#
# for line in f:
#     a = sorted(list(map(int, line.split())))
#     k = 0
#     for x in a:
#         if x % 3 == 0:
#             k += 1
#     if k == 3 and ((a[-1] - a[0]) <= sum(x for x in a if x % 3 == 0)):
#         count += 1
# print(count)


f = open('9.csv')
count = 0

for line in f:
    a = sorted(list(map(int, line.split())))
    if a[0] * a[1] % 10 == 4 or a[1] * a[2] % 10 == 4 or a[0] * a[2] % 10 == 4:
        count += 1
print(count)
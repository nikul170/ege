# a = list(map(int, open('text')))
# m = -float('inf')
# count = 0
# for i in range(len(a) - 1):
#     if a[i] % 3 == 0 or a[i + 1] % 3 == 0:
#         count += 1
#         m = max(m, a[i] + a[i + 1])
# print(count, m)

# a = list(map(int, open('text')))
# count = 0
# m = -float('inf')
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if (a[i] + a[j]) % 7 == 0:
#             count += 1
#             m = max(m, a[i] + a[j])
# print(count, m)

# a = list(map(int, open('text')))
# count = 0
# m = -float('inf')
# for i in range(len(a) - 1):
#     if ((a[i] + a[i + 1]) % 2 == 0) and abs(a[i] + a[i + 1]) % 10 != 6:
#         count += 1
#         m = max(m, (a[i] + a[i + 1]) / 2)
# print(count, m)
#
# a = list(map(int, open('text')))
# k = 0
# m = -float('inf')
# for i in range(len(a) - 2):
#     if ((a[i] * a[i + 1] * a[i + 2]) % 7 == 0) and (abs(a[i] + a[i + 1] + a[i + 2]) % 10 == 5):
#         k += 1
#         m = max(m, a[i] + a[i + 1] + a[i + 2])
# print(k, m)

# a = list(map(int, open('text')))
# count = 0
# m = -float('inf')
# for i in range(len(a) - 1):
#     if a[i] % 3 == 0 or a[i] % 3 == 0:
#         count += 1
#         m = max(m, a[i] + a[i + 1])
# print(count, m)

# a = list(map(int, open('text')))
# count = 0
# m = -float('inf')
# for i in range(len(a) - 1):
#     if ((a[i] + a[i + 1]) % 60 == 0) and (a[i] % 40 == 0 or a[i + 1] % 40 == 0):
#         count += 1
#         m = max(m, a[i] + a[i + 1])
# print(count, m)

# a = list(map(int, open('text')))
# count = 0
# m = -float('inf')
# for i in range(len(a) - 1):
#     if a[i] - a[i + 1] % 60 == 0:
#         count += 1
#         m = max(m, a[i] - a[i + 1])
# print(count, m)

# a = list(map(int, open('text')))
# count = 0
# m = -float('inf')
#
# for i in range(len(a) - 1):
#     if (a[i] % 3 == 0 or a[i + 1] % 3 == 0) and ((a[i] + a[i + 1]) % 5 == 0):
#         count += 1
#         m = max(m, a[i] + a[i + 1])
# print(count, m)


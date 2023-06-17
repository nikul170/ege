# a = list(map(int, open('17.txt')))
# ma = max(i for i in a if i % 2 != 0)
# m = float('inf')
# count = 0
#
# for i in range(len(a) - 1):
#     if 2 * (a[i] + a[i + 1]) > ma:
#         count += 1
#         m = min(m, a[i] + a[i + 1])
# print(count, m)


# a = list(map(int, open('17.txt')))
# count = 0
# m = -float('inf')
# ma = max(i for i in a if i % 10 == 4) + min(i for i in a if i % 10 == 4)
#
#
# for i in range(len(a) - 1):
#     if (a[i] + a[i + 1]) < ma:
#         count += 1
#         m = max(m, a[i] + a[i + 1])
# print(count, m)


# a = list(map(int, open('17.txt')))
# count = 0
# m = -float('inf')
# ma = sum(a) / len(a)
#
# for i in range(len(a) - 2):
#     if ((a[i] > ma) + (a[i + 1] > ma) + (a[i + 2] > ma)) >= 2:
#         count += 1
#         m = max(m, a[i] + a[i + 1] + a[i + 2])
# print(count, m)


# a = list(map(int, open('17.txt')))
# count = 0
# m = -float('inf')
#
# for i in range(len(a) - 1):
#     if ((a[i] - a[i + 1]) % 2 == 0) and ((a[i] - a[i + 1]) % 37 == 0):
#         count += 1
#         m = max(m, a[i] + a[i + 1])
# print(count, m)


# a = list(map(int, open('17.txt')))
# count = 0
# ma = -float('inf')
# mx = float('inf')
#
# for i in range(len(a)):
#     if ((a[i] % 10 == 7) or (a[i] % 10 == 5)) and ((a[i] % 9 != 0) and (a[i] % 11 != 0)):
#         ma = max(ma, a[i])
#         mx = min(mx, a[i])
#         count += 1
# print(count, ma + mx)

# def f(n):
#     x = ''
#     while n > 0:
#         x = str(n % 3) + x
#         n //= 3
#     return int(x)
#
#
# a = list(map(int, open('17.txt')))
# count = 0
# m = -float('inf')
#
# for i in range(len(a)):
#     if (sum(map(int, str(a[i]))) % 5 == 0) and f(a[i]) % 100 != 0:
#         count += 1
#         m = max(m, a[i])
# print(count, m)


# a = list(map(int, open('17.txt')))
# count = 0
# m = -float('inf')
#
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if (a[i] * a[j]) % 62 == 0:
#             count += 1
#             m = max(m, a[i] + a[j])
# print(count, m)


a = list(map(int, open('17.txt')))

ma = sum(a) / len(a)
count = 0
m = -float('inf')

for i in range(len(a) - 2):
    if ((a[i] > ma) + (a[i + 1] > ma) + (a[i + 2] > ma)) >= 2:
        count += 1
        m = max(m, a[i] + a[i + 1] + a[i + 2])
print(count, m)






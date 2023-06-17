# f = open('26.txt')
# N = int(f.readline())
# count = 0
# a = []
# m = -float('inf')
# for i in range(N):
#     a.append(list(map(int, f.readline().split())))
# a.sort(key=lambda x: (-x[0], x[1]))
#
#
# for i in range(1, len(a) - 1):
#     if (a[i - 1][0] == a[i][0] and a[i][0] == a[i + 1][0]) and (a[i][1] - a[i - 1][1] == 6) and (a[i + 1][1] - a[i][1] == 6):
#         count += 1
#         m = max(m, a[i][0])
# print(m, count)

# f = open('26.txt')
# N = int(f.readline())
# a = []
# m_count = -1
#
# for i in range(N):
#     a.append(list(map(int, f.readline().split())))
# a.sort(key=lambda x: (-x[0], x[1]))
# for i in range(N - 1):
#     if (a[i][0] == a[i + 1][0]) and ((a[i + 1][1] - a[i][1]) - 1 > m_count):
#         m_count = a[i + 1][1] - a[i][1] - 1
#         row = a[i][0]
# print(row, m_count)

# f = open('26.txt')
# K = int(f.readline())
# N = int(f.readline())
# a = [-1] * K
# c = []
# count = 0
# for _ in range(N):
#     c.append(list(map(int, f.readline().split())))
# c.sort()
#
# for i in range(N):
#     for j in range(len(a)):
#         if c[i][0] > a[j]:
#             a[j] = c[i][1]
#             count += 1
#             mi = j + 1
#             break
# print(count, mi)


# f = open('26.txt')
# N = int(f.readline())
# a = []
# count = 1
#
# for i in range(N):
#     x = int(f.readline())
#     a.append(x)
# a.sort(reverse=True)
# m = a[0]
#
# for i in range(1, N):
#     if (m - a[i]) >= 3:
#         count += 1
#         m = a[i]
# print(count, m)


# f = open('26.txt')
# S, N = map(int, f.readline().split())
# a = []
# s = 0
# count = 0
# m = -float('inf')
# for i in range(N):
#     a.append(int(f.readline()))
# a.sort()
# for i in range(N):
#     s += a[i]
#     if s <= S:
#         count += 1
#     if s > S:
#         s -= a[i]
#         mi = a[i - 1]
#         r = i
#         break
# print(s)
# for i in range(r, N):
#     if a[i] + (s - mi) <= S:
#         m = max(m, a[i])
# print(count, m)



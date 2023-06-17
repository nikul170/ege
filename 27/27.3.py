# f = open('27.1.txt')
# N = int(f.readline())
#
#
# a = []
# for i in range(N):
#     x = int(f.readline())
#     a.append(x)
#
#
# m = mp  = -float('inf')
#
# for i in range(8, N):
#     x = int(f.readline())
#     m = max(m, a[i % 8])
#     mp = max(mp, x * m)
#     a[i % 8] = x

#
# f = open('27.1.txt')
# N = int(f.readline())
# a = [0] * 2
# b = [float('inf')] * 2
# count = 0
#
# for i in range(N):
#     x = int(f.readline())
#     if x > b[(x + 1) % 2]:
#         for y in range(2):
#             if (x + y) % 2 !=0:
#                 count += a[y]
#     a[x % 2] += 1
#     b[x % 2] = min(b[x % 2], x)
# print(count)


# f = open('27.1.txt')
# N = int(f.readline())
# a = [0] * 2
# l = []
#
# for i in range(N):
#     x = int(f.readline())
#     if l.count(x) < 2:
#         a[x % 2] += 1
#     l.append(x)
# count = (a[0] * a[1] - 1) // 2
# print(int(count))

# f = open('27.1.txt')
# N = int(f.readline())
# K = int(f.readline())
# a = []
# m = k = -float('inf')

# for _ in range(K):
#     a.append(int(f.readline()))
#
#
# for i in range(K, N):
#     x = int(f.readline())
#     m = max(m, a[i % K])
#     k = max(k, x + m)
#     a[i % K] = x
# print(k)






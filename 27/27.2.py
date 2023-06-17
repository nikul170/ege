# f = open('27.txt')
# N = int(f.readline())
# 
# a = [0] * 28
# m = 0
# 
# for i in range(N):
#     x = int(f.readline())
#     for y in range(28):
#         if (x - y) % 13 == 0 and x * y % 2 == 0:
#             m = max(m, x * a[y])
#     if x > a[x % 14]:
#         a[x % 13] = x
# print(m)


# f = open('27.txt')
# N = int(f.readline())
#
# m = float('inf')
# s = 0
# for i in range(N):
#     a = list(map(int, f.readline().split()))
#     a.sort()
#     if a[2] - a[0] < m and (a[2] - a[0]) % 2 != 0:
#         m = a[2] - a[0]
#     if a[2] - a[1] < m and (a[2] - a[1]) % 2 != 0:
#         m = a[2] - a[1]
#     s += a[2]
# print(s - m)

# f = open('27.txt')
# N = int(f.readline())
#
#
# a = [0, 0]
# a1 = [0, 0]
# count = 0
# for i in range(N):
#     x = int(f.readline())
#     if x == 0:
#         a[0] = a1[0]
#         a1[0] = a1[1]
#         continue
#     count += a[x % 2]
#     a1[x % 2] += 1
# print(count)


f = open('27.1.txt')
N = int(f.readline())
K = int(f.readline())
a = []
m1 = m47 = a1 = a47 = m = -float('inf')
c47 = []
c1 = []
for i in range(K):
    a.append(int(f.readline()))
print(a)
for i in range(K, N):
    x = int(f.readline())
    c47 += [a[i % K] for i in range(K) if a[i % K] % 47 == 0]
    c1 += [a[i % K] for i in range(K) if a[i % K] % 47 != 0]
    if len(c47) != 0:
        m47 = max(c47[0:(i % K) + 1])
    if len(c1) != 0:
        m1 = max(c1[0:(i % K) + 1])
    print(m1, m47, x % 47, x)
    if x % 47 == 0 and (x + m1) % 2023 == 0:
        m = max(m, x + m1)
    if x % 47 != 0 and (x + m47) % 2023 == 0:
        m = max(m, x + m47)
    # c1 = [a[i] for i in range(len(a)) if a[i] % 47 != 0]
    # m1 = max(m, c1[0])
    # if x % 47 == 0 and (x + m1) % 2023:
    #     m = max(x + m1)
    # if a[i % K] and (x + m1) % 2023:
    #     m = max(x + m1)
    # else:
    #     x1 = max(x1, x)
    #     a1 = max(a47, a[i % K])
    a[i % K] = x
print(m)






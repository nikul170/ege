# f = open('27.1.txt')
# N = int(f.readline())
# a = [0] * 26
# count = 0
#
# for i in range(N):
#     x = int(f.readline())
#     for y in range(26):
#         if (x * y) % 26 == 0:
#             count += a[y]
#     a[x % 26] += 1
# print(count)


# f = open('27.1.txt')
# N = int(f.readline())
# s = [0]
#
# for i in range(N):
#     pair = list(map(int, f.readline().split()))
#     cmb = [a + b for a in pair for b in s]
#     s = {x % 109: x for x in sorted(cmb)}.values()
# print(max(x for x in s if x % 109 != 0))


# f = open('27.1.txt')
# N = int(f.readline())
# m = -float('inf')
# a = [float('inf')] * 7
# s = 0
# k = 0
# n = [0] * 7
#
# for i in range(N):
#     x = int(f.readline())
#     s += x
#     if x % 7 == 0 and x > 0:
#         k += 1
#     if k % 7 == 0:
#         m = max(m, s)
#     if ((i + 1) - n[k % 7]) >= 7:
#         m = max(m, s - a[k % 7])
#     if s < a[k % 7]:
#         a[k % 7] = s
#         n[k % 7] = i + 1
# print(m)


# f = open('27.1.txt')
# N = int(f.readline())
# a = []
# for i in range(5):
#     a.append(int(f.readline()))
#
# m = k = float('inf')
# for i in range(5, N):
#     x = int(f.readline())
#     m = min(m, a[i % 5])
#     k = min(k, m ** 2 + x ** 2)
#     a[i % 5] = x
# print(k)

f = open('27.1.txt')
N = int(f.readline())
s1 = s2 = s3 = 0
m = []
for i in range(N):
    a = sorted(list(map(int, f.readline().split())))
    s1 += a[0]
    s2 += a[1]
    s3 += a[2]
    if (a[2] - a[0]) % 2 != 0:
        m.append(a[2] - a[0])
    if (a[2] - a[1] % 2) == 0:
        m.append(a[2] - a[1] % 2)
m.sort(reverse=True)
print(s1, s2 + m[0], s3 + m[1])

# 151952413
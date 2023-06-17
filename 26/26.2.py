# f = open('26.txt')
# N = int(f.readline())
# a = []
#
# for i in range(N):
#     a.append(list(map(int, f.readline().split())))
#
# a.sort(key=lambda x: (-x[0], x[1]))
#
# m = float('inf')
# c = -float('inf')
# for i in range(N - 1):
#     if a[i][0] == a[i + 1][0] and (a[i + 1][1] - a[i][1]) < m:
#         m = a[i + 1][1] - a[i][1] - 1
#         c = a[i][0]
# print(c, m)


f = open('26.txt')
S, N = map(int, f.readline().split())
a = []
s = 0
count = 0
m = -float('inf')
for i in range(N):
    a.append(int(f.readline()))
a.sort()
for i in range(N):
    s += a[i]
    if s <= S:
        count += 1
    if s > S:
        s -= a[i]
        mi = a[i - 1]
        r = i
        break
for i in range(r, N):
    if a[i] + (s - mi) <= S:
        m = max(m, a[i])
print(count, m)
        




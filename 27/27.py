f = open('27.1.txt')
N = int(f.readline())
a = []
for i in range(N):
    s, n = map(int, f.readline().split())
    a.append([s, n // 96 if n % 96 == 0 else n // 96 + 1])

p = [a[0][1]]
for i in range(1, N):
    p.append(p[i - 1] + a[i][1])

s = 0
for i in range(1, N):
    s += (a[i][0] - a[0][0]) * a[i][1]


m = float('inf')
for i in range(1, N):
    d = (a[i][0] - a[i - 1][0])
    s += d * p[i - 1] - d * (p[-1] - p[i - 1])
    m = min(m, s)
print(m)
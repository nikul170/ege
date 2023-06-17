# НЕРАВЕНСТВА
def f(x, y, a):
     return (x > a) or (y > a) or ((y - 2 * x + 12) != 0)


print(max(a for a in range(100) if all(f(x, y, a) for x in range(1000) for y in range(1000))))


# ФУНКЦИИ
def d(n, m):
    return n % m == 0


def c(s, d):
    return s + d > 0


def f(x, a):
    return (x + a >= 160) or (d(x, 7) <= (not c(x, - 17)))


print(min(a for a in range(1, 1000) if all(f(x, a) for x in range(1, 1000))))


# КОНЪЮНКЦИЯ

def f(x, a):
    return ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & a != 0))


print(min(a for a in range(1, 100) if all(f(x,a) for x in range(1, 1000))))


# ОТРЕЗКИ
p1, p2 , q1, q2, r1, r2 = 25, 240,  175, 300, 270, 340
p = [i / 10 for i in range(p1 * 10, p2 * 10 + 1)]
q = [i / 10 for i in range(q1 * 10, q2 * 10 + 1)]
r = [i / 10 for i in range(r1 * 10, r2 * 10 + 1)]


def f(x, a):
    return ((x in q) <= (x in p)) or ((x not in a) <= (x in r))


#a = set() - наименьшая длинна
a = set([i / 10 for i in range(20 * 10, 350 * 10)])
for x in [i / 10 for i in range(20 * 10, 350 * 10)]:
    if not f(x, a):
        # a.add(x) - наименьшая длинна
        a.remove(x)
print(sorted(a))

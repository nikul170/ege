from itertools import *


def u(x, y, z, w):
    return ((not x) and y) or z and (not y) or ((not z) and w)



for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
    t = (
        (1, 0, x1, x2, 0),
        (x3, 1, 0, x4, 0),
        (x5, x6, 1, 0, 0),
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', r=4):
            if all(u(**dict(zip(p, r))) == r[-1] for r in t):
                print(*p)
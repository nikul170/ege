# def f(s, c, m):
#     if 51 <= s <= 60: return c % 2 == m % 2
#     if s > 60: return c % 2 != m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s + 2, c + 1, m), f(s * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 51):
#     for m in range(1, 8):
#         if f(s, 0, m):
#             if m == 6:
#                 print(s)
#             break


def f(s, c, m, k):
    if s >= 21: return c % 2 == m % 2
    if c == m: return 0
    h = []
    if k != '+1': h += [f(s + 1, c + 1, m, '+1')]
    if k != '+2': h += [f(s + 2, c + 1, m, '+2')]
    if k != '*2': h += [f(s * 2, c + 1, m, '*2')]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 21):
    for m in range(1, 7):
        if f(s, 0, m, ''):
            if m == 3:
                print(s)
            break
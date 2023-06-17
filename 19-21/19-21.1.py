# def f(s, c, m):
#     if s >= 47: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s * 3, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 47):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break

def f(s, c, m):
    if 43 <= s: return c % 2 == m % 2
    if c == m: return 0
    h = [f(s + 1, c + 1, m), f(s * 2, c + 1, m), f(s * 3, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for s in range(1, 43):
    for m in range(1, 5):
        if f(s, 0, m):
            if m == 3:
                print(s, m)
            break


# def f(a, b, c, m):
#     if a + b >= 74: return c % 2 == m % 2
#     if m == c: return 0
#     h = [f(a + 1, b, c + 1, m), f(a, b + 1, c + 1, m), f(a * 2, b, c + 1, m), f(a, b * 2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 62):
#     for m in range(1, 5):
#         if f(12, s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break


# def f(s, c, m):
#     if s >= 68: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 1, c + 1, m), f(s + 4, c + 1, m), f(s * 5, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)
#
#
# for s in range(1, 68):
#     for m in range(1, 5):
#         if f(s, 0, m):
#             if m == 4:
#                 print(s, m)
#             break



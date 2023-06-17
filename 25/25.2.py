# for x in range(2, 17):
# #     D = set()
# #     for d in range(1, int(x ** 0.5) + 1):
# #         if x % d == 0:
# #             if d % 2 == 0:
# #                 D.add(d)
# #             if (x // d) % 2 == 0:
# #                 D.add(x // d)
# #     if len(D) == 4:
# #         print(*sorted(D))


# count = 0
# num = 350300 + 1
# while count < 6:
#     D = set()
#     for d in range(2, int(num ** 0.5) + 1):
#         if num % d == 0:
#             D.add(d)
#             D.add(num // d)
#     if sum(D) % 13 == 0 and len(D) != 0:
#         print(num, sum(D) // 13)
#         count += 1
#     num += 1

# count = 1
# for x in range(245690, 245756 + 1):
#     D = set()
#     for d in range(2, int(x ** 0.5) + 1):
#         if x % d == 0:
#             break
#     else:
#         print(count, x)
#     count += 1


# for x in range(100806, 100950 + 1):
#     D = set()
#     for d in range(1, int(x ** 0.5) + 1):
#         if x % d == 0:
#             D.add(d)
#             D.add(x // d)
#     if len(D) == 6:
#         d = sorted(list(D))
#         print(d[3], d[4])

#
# for x in range(33333, 55555 + 1):
#     for d in range(2, int(x ** 0.5) + 1):
#         if x % d == 0:
#             break
#     else:
#         if sum(map(int, str(x))) > 35:
#             print(x, sum(map(int, str(x))))


for x in range(100000, 500000 + 1):
    D = set()
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            if d % 2 == 0:
                D.add(d)
            if (x // d) % 2 == 0:
                D.add(x // d)
    if len(D) > 150:
        print(x, max(D) - min(D))

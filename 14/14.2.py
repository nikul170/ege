# x = 49 ** 7 + 7 ** 21 - 7
# k = 0
# while x > 0:
#     if x % 7 == 6:
#         k += 1
#     x //= 7
# print(k)

# for x in range(0, 15):
#     s = 1 * 15 ** 4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 + 5 + 1 * 15 ** 4 + x * 15 ** 3 + 2 * 15 ** 2 + 3 * 15 + 3
#     if s % 14 == 0:
#         print(x)


# for x in '0123456789ABCDE':
#     s = int('123' + x + '5', 15) + int('1' + x + '233', 15)
#     if s % 14 == 0:
#         print(x)
#         break


# for x in range(0, 21):
#     for y in range(0, 21):
#         x1 = 1 * 21 ** 4 + 2 * 21 ** 3 + y * 21 ** 2 + x * 21 ** 1 + 9
#         x2 = 3 * 21 ** 4 + 6 * 21 ** 3 + y * 21 ** 2 + 9 * 21 ** 1 + 9
#         if (x1 + x2) % 18 != 0:
#             break
#     else:
#         y = 5
#         x1 = 1 * 21 ** 4 + 2 * 21 ** 3 + y * 21 ** 2 + x * 21 + 9
#         x2 = 3 * 21 ** 4 + 6 * 21 ** 3 + y * 21 ** 2 + 9 * 21 + 9
#         print((x1 + x2) // 18)


# for x in range(0, 21):
#     for y in range(0, 21):
#         x1 = 1 * 21 ** 4 + 2 * 21 ** 3 + y * 21 ** 2 + x * 21 ** 1 + 9 * 21 ** 0
#         x2 = 3 * 21 ** 4 + 6 * 21 ** 3 + y * 21 ** 2 + 9 * 21 ** 1 + 9 * 21 ** 0
#         if (x1 + x2) % 18 != 0:
#             break
#     else:
#         y = 5
#         x1 = 1 * 21 ** 4 + 2 * 21 ** 3 + y * 21 ** 2 + x * 21 ** 1 + 9 * 21 ** 0
#         x2 = 3 * 21 ** 4 + 6 * 21 ** 3 + y * 21 ** 2 + 9 * 21 ** 1 + 9 * 21 ** 0
#         print((x1 + x2 )// 18)

# for x in range(0, 15):
#     for y in range(0, 17):
#         x1 = 1 * 15 ** 4 + 2 * 15 ** 3 + 3 * 15 ** 2 + x * 15 ** 1 + 5 * 15 ** 0
#         x2 = 6 * 17 ** 3 + 7 * 17 ** 2 + y * 17 ** 1 + 9 * 17 ** 0
#         if (x1 + x2) % 131 == 0:
#             print((x1 + x2) / 131, y)

# for x in range(0, 17):
#     x1 = 9 * 17 ** 4 + 7 * 17 ** 3 + 5 * 17 ** 2 + 9 * 17 ** 1 + x
#     x2 = 3 * 17 ** 4 + x * 17 ** 3 + 1 * 17 ** 2 + 8
#     if (x1 + x2) % 11 == 0:
#         print((x1 + x2) // 11)

# for x in range(0, 80):
#     x1 = 3 * 80 ** 3 + x * 80 ** 2 + 7 * 80 ** 1 + 5
#     x2 = 1 * 80 ** 3 + 4 * 80 ** 2 + x * 80 ** 1 + 0
#     if (x1 + x2) % 17 == 0:
#         print((x1 + x2) // 17)


for x in range(0, 11):
    x1 = 3 * 11 ** 4 + 3 * 11 ** 3 + 6 * 11 ** 2 + 4 * 11 ** 1 + x
    x2 = x * 12 ** 4 + 7 * 12 ** 3 + 9 * 12 ** 2 + 4 * 12 ** 1 + 6
    x3 = 5 * 14 ** 4 + 5 * 14 ** 3 + x * 14 ** 2 + 8 * 14 ** 1 + 7
    if x1 + x2 == x3:
        print(x3)
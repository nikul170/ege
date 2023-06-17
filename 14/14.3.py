# for p in range(16):
#     for x in '0123456789abcdef':
#         for y in '0123456789abcdef':
#             try:
#                 if int('5'+x+'83', p) + int(x+'9'+x+'9', p) == int(y+'20'+y, p):
#                     print(int(x + y + y + x, p))
#             except:
#                 ...

# count = 0
# a = set()
# for x in '0123456789abcdef':
#     for y in range(9, 16):
#         try:
#             a.add(int('5' + x + str(y) + 'c', 16) + int('8' + x + x + '7', y))
#         except:
#             ...
# print(len(a))

# def d(x):
#     a = ''
#     while x > 0:
#         a = str(x % 6) + a
#         x //= 6
#     return sum(map(int, a))
#
#
#
# for x in '0123456789abcdef':
#     if d(int('b7a'+x+'9', 16) + int('54' + x + 'ed', 16)) == 25:
#         print(int('b7a'+x+'9', 16) + int('54' + x + 'ed', 16))


# for x in range(111):
#     x1 = 1 * 111 ** 0 + 2 * 111 ** 1 + 3 * 111 ** 2 + x * 111 ** 3
#     x2 = 4 * 211 ** 0 + x * 211 ** 1 + 7 * 211 ** 2 + 1 * 211 ** 3
#     if (x1 + x2) % 111 == 0:
#         print((x1 + x2) // 111)


# for x in range(67):
#     x1 = 1 * 81 ** 0 + 2 * 81 ** 1 + x * 81 ** 2 + 3 * 81 ** 3
#     x2 = 4 * 67 ** 0 + x * 67 ** 1 + 7 * 67 ** 2 + 1 * 67 ** 3
#     if (x1 + x2) % 35 == 0:
#         print((x1 + x2) // 35)


# x = 729 ** 6 + 3 ** 14 - 36
# count = 0
# while x > 0:
#     if x % 9 == 0:
#         count += 1
#     x //= 9
# print(count)


# for x in '0123456789a':
#     if int('3364' + x, 11) + int(x +'7946', 12) == int('55' + x + '87', 14):
#         print(int('55' + x + '87', 14))


for x in range(21):
    for y in range(21):
        x1 = 9 * 21 ** 0 + x * 21 ** 1 + y * 21 ** 2 + 2 * 21 ** 3 + 1 * 21 ** 4
        x2 = 9 * 21 ** 0 + 9 * 21 ** 1 + y * 21 ** 2 + 6 * 21 ** 3 + 3 * 21 ** 4
        if (x1 + x2) % 18 != 0:
            break
    else:
        y = 5
        x1 = 9 * 21 ** 0 + x * 21 ** 1 + y * 21 ** 2 + 2 * 21 ** 3 + 1 * 21 ** 4
        x2 = 9 * 21 ** 0 + 9 * 21 ** 1 + y * 21 ** 2 + 6 * 21 ** 3 + 3 * 21 ** 4
        print((x1 + x2) // 18)

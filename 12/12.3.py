# s = '1' * 95 + '7' * 31
# while '1111' in s:
#     s = s.replace('1111', '7', 1)
#     s = s.replace('77', '1', 1)
# print(s)

# for x in range(1, 51):
#     s = '6' * x
#     while '66' in s:
#         s = s.replace('66', '1', 1)
#         s = s.replace('11', '2', 1)
#         s = s.replace('22', '6', 1)
#     if s == '21':
#         print(x)


# s = '1' + '0' * 75
# while ('10' in s) or ('1' in s):
#     if '10' in s:
#         s = s.replace('10', '001', 1)
#     else:
#         s = s.replace('1', '00', 1)
# print(s.count('0'))

# s = '3' * 147
#
# while '5555' in s or '3333' in s:
#     if '5555' in s:
#         s = s.replace('5555', '3', 1)
#     else:
#         s = s.replace('3333', '5', 1)
# print(s)


# s = '2' * 400
#
# while '8888' in s or '222' in s:
#     if '222' in s:
#         s = s.replace('222', '88', 1)
#     else:
#         s = s.replace('8888', '22', 1)
# print(s)


s = '0' + '1' * 45

while '0' in s or '01' in s:
    if '01' in s:
        s = s.replace('01', '10', 1)
    else:
        s = s.replace('0', '111', 1)
print(s.count('1'))
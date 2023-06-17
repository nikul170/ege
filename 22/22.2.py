# def f(i):
#     if a[i][2] == 0:
#         return a[i][1]
#     else: return max(f(j - 1) for j in a[i][2:]) + a[i][1]
#
#
#
# a = []
# for line in open('22.txt'):
#     a.append(list(map(int, line.replace(';', ' ').split())))
#
# print(max(f(i) for i in range(len(a))))


# def f(i):
#     if a[i][2] == 0: return a[i][1]
#     else: return max(f(j - 1) for j in a[i][2:]) + a[i][1]
#
#
# a = [list(map(int, line.replace(';', ' ').split())) for line in open('22.txt')]
# print(max(f(i) for i in range(len(a))))


# def f(i):
#     if a[i][2] == 0: return a[i][1]
#     else: return max(f(j - 1) for j in a[i][2:]) + a[i][1] + 3
#
#
# a = [list(map(int, line.replace(';', ' ').split())) for line in open('22.txt')]
# print(max(f(i) for i in range(len(a))))


# def f(i):
#     if a[i][2] == 0: return a[i][1]
#     else: return max(f(j - 1) for j in a[i][2:]) + a[i][1]
#
#
# a = [list(map(int, line.replace(';', '').split())) for line in open('22.txt')]
# print(max(f(i) for i in range(len(a))))


# def f(i):
#     if a[i][2] == 0: return a[i][1]
#     else: return max(f(j - 1) for j in a[i][2:]) + a[i][1]
#
#
# a = [list(map(int, line.replace(';', ' ').split())) for line in open('22.txt')]
# print(max(f(i) for i in range(len(a))))
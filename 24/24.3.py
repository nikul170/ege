# a = open('24.txt').readline()
#
# m = -float('inf')
# k = 0
#
# for i in range(len(a) - 1):
#     if a[i + 1] == 'D':
#         k += 1
#         m = max(m, k)
#     else:
#         k = 0
# print(m)


# a = open('24.txt').readline()
#
# k = 0
# m = -float('inf')
#
# for i in range(2, len(a) - 2, 3):
#     if a[i] == a[i + 1] and a[i + 1] == a[i + 2]:
#         k += 3
#         m = max(m, k)
#     else:
#         k = 0
# print(m)


# a = open('24.txt').readline()
#
# k = 0
# m = -float('inf')
#
#
# for i in range(0, len(a) - 1, 2):
#     if a[i] in 'AB' and a[i + 1] in '12':
#         k += 1
#         m = max(m, k)
#     else:
#         k = 0
#
# print(m)


# a = open('24.txt').readline()
# print(a)
# k = 0
# m = -float('inf')

# import collections
#
#
# a = open('24.txt').readlines()
# print(sum(a[i].count('C') for i in range(len(a))))
# m = max(a[i].count('Q') for i in range(len(a)))
#
#
#
# for i in range(len(a)):
#     if a[i].count('Q') == m:
#         c = []
#         for s in a[i]:
#             c.append(s)
#
# print(collections.Counter(c).most_common())



# a = open('24.txt').readline()
# k = 1
# m = -float('inf')
#
# for i in range(len(a) - 1):
#     if int(a[i]) <= int(a[i + 1]):
#         k += 1
#         m = max(m, k)
#     else:
#         k = 1
# print(m)

# import collections
#
# a = open('24.txt').readline()
# c = []
#
#
# for i in range(len(a) - 2):
#     if a[i] == a[i + 2]:
#         c.append(a[i + 1])
# print(collections.Counter(c).most_common())



# a = open('24.txt').readline()
# l = []
#
# for i in range(len(a) - 1):
#     for j in range(i + 1, len(a)):
#         if a[i] == a[j]:
#             l.append(a[i: j + 1])
#             break
# print(max(len(i) for i in l))












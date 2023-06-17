# f = open('27.1.txt')
# N = int(f.readline())
# K = int(f.readline()) + 1
# a = [0] * 17
# nums = []
# count = 0
# k = 0
#
# for i in range(K):
#     x = int(f.readline())
#     nums.append(x)
#     for y in range(17):
#         if (x + y) % 17 == 0:
#             k += a[y]
#     a[x % 17] += 1
#
# for i in range(K, N):
#     x = int(f.readline())
#     a[nums[i % K] % 17] -= 1
#     for y in range(17):
#         if (x + y) % 17 == 0:
#             k += a[y]
#     a[x % 17] += 1
#     nums[i % K] = x
# print(k)

# 15079


# a = open('27.1.txt').readline()
# m = -float('inf')
# k = 1
# 
# for i in range(len(a) - 1):
#     if a[i: i + 2] != 'ad' or a[i: i + 2] != 'da':
#         k += 1
#         m = max(m, k)
#     else:
#         k = 1
# print(m)



f = open('27.1.txt')
N = int(f.readline())
m = -float('inf')
a = []



for i in range(N):
    a.append(int(f.readline()))
print(max(i for i in a if i % 2 == 0) + max(i for i in a if i % 2 != 0))



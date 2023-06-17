# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (x or (not y)) and (not (y == z)) and w
#                 if f == 1:
#                     print(x, y, z, w)

# print('a b c')
# for a in 0,1:
#     for b in 0,1:
#         for c in 0,1:
#             f = (a and (not c)) or ((not b) and (not c))
#             if f == 0:
#                 print(a,b,c)

# print('x y z')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             f = ((not x) and y and z) or ((not x) and (not y) and z) or ((not x) and (not y) and (not z))
#             if f == 1:
#                 print(x,y,z)

# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (((not x) and y) == z) and w
#                 if f == 1:
#                     print(x, y, z, w)

# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (x <= (y and (not z))) or w
#                 if f == 0:
#                     print(x,y,z,w)

# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (x and (not y)) or (x == z) or w
#                 if f == 0:
#                     print(x, y, z ,w)

# print('x y z')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             f = ((not x) and y and z) or ((not x) and (not z))
#             if f == 1:
#                 print(x, y, z)

# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (not y) and x and((not z) or w)
#                 if f == 1:
#                     print(x, y, z, w)

# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (y <= (x or z)) and (z <= y)
#                 if f == 0:
#                     print(x, y, z, w)

# print('x y z')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             f =(not (x == (y <= z)))
#             if f == 1:
#                 print(x, y, z)

# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (y <= x) or (not((x <= z) and (z <= x))) and (not w)
#                 if f == 0:
#                     print(x, y, z, w)

# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (not w) and ((y or z) <= ((not x) and y))
#                 if f == 1:
#                     print(x,y ,z, w)

# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = ((w <= y) or (not(y <= z))) and (not x) and (not (x == z))
#                 if f == 1:
#                     print(x, y, z, w)

# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (x <= y) or (not ( w <= z))
#                 if f == 0:
#                     print(x, y, z, w)

# print('a b c d')
# for a in 0,1:
#     for b in 0,1:
#         for c in 0,1:
#             for d in 0,1:
#                 f = ((a and b) == (not c)) and (b <= d)
#                 if f == 1:
#                     print(a,b,c,d)

# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (not(z and (not w))) or ((z < w) == (x <= y))
#                 if f == 0:
#                     print(x, y, z, w)

# print('a b c d')
# for a in 0,1:
#     for b in 0,1:
#         for c in 0,1:
#             for d in 0,1:
#                 f = ((not a) and (not b)) or (b == c) or d
#                 if f == 0:
#                     print(a,b,c,d)

# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = ((z <= x) and (x <= w)) or (y == (z or x))
#                 if f == 0:
#                     print(x, y, z, w)

# print('x y z w')
# for x in 0,1:
#     for y in 0,1:
#         for z in 0,1:
#             for w in 0,1:
#                 f = (x and z) or ((w <= x) == ( z <= y))
#                 if f == 0:
#                     print(x, y, z, w)

print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (x == (not z)) <= ((x or w) == y)
                if f == 0:
                    print(x, y, z, w)

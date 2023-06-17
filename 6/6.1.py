# from turtle import *
#
# tracer(0)
# m = 30
# up()
# goto(-5 * m, 5 * m)
# down()
# for i in range(7):
#     fd(10 * m)
#     rt(120)
#
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(5, "blue")
#
# update()
# input()

# from turtle import *
#
# tracer(0)
# m = 40
#
# for _ in range(4):
#     fd(8 * m)
#     rt(90)
#     fd(8 * m)
#     rt(90)
#
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(3, 'black')
# update()
# input()

# from turtle import *
#
# tracer(0)
# m = 10
#
# for _ in range(20):
#     for _ in range(4):
#         fd(15 * m)
#         rt(90)
#     back(20 * m)
#     rt(90)
#
# up()
# for x in range(-40, 40):
#     for y in range(-40, 40):
#         goto(x * m, y * m)
#         dot(3, 'black')
# update()
# input()

# from turtle import *
#
# tracer(0)
# m = 15
#
# for _ in range(10):
#     fd(9 * m)
#     rt(90)
#     fd(2 * m)
#     rt(90)
#
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(4, 'black')
# update()
# input()

# from turtle import *
#
# tracer(0)
# m = 10
# up()
# goto(0, 40 * m)
# down()
#
# for _ in range(10):
#     for _ in range(3):
#         fd(10 * m)
#         rt(90)
#         fd(10 * m)
#         rt(270)
#     rt(90)
#
# up()
# for x in range(-45, 45):
#     for y in range(-45, 45):
#         goto(x * m, y * m)
#         dot(4, 'black')
# update()
# input()


# from turtle import *
#
# m = 15
# tracer(0)
#
# for _ in range(4):
#     fd(7 * m)
#     rt(90)
#     fd(8 * m)
#     rt(90)
#
#
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(4, 'black')
# update()
# input()

# from turtle import *
# m = 15
# tracer(0)
#
# for _ in range(4):
#     fd(10 * m)
#     rt(60)
#     fd(10 * m)
#     rt(120)
#
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(4, 'black')
# update()
# input()

# from turtle import *
#
# tracer(0)
# m = 15
#
# for _ in range(5):
#     fd(7 * m)
#     rt(90)
#     fd(4 * m)
#     rt(90)
#
# up()
# for x in range(-20, 20):
#     for y in range(-20, 20):
#         goto(x * m, y * m)
#         dot(4, 'black')
# update()
# input()

from turtle import *

m = 15
tracer(0)

for _ in range(4):
    fd(10 * m)
    rt(90)

up()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * m, y * m)
        dot(4, 'black')
update()
input()
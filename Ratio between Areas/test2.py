import math

pi = 3.14

a, b = map(float, input().split())
c, d = map(float, input().split())

r = float(input())
theta = float(input())

AB_distance = ((a - c) ** 2 + (b - d) ** 2) ** 0.5
circle_area = (r**2) / 2

if r > 0 and AB_distance > 0:
    AB_area = circle_area * theta - 0.5 * r * math.cos(theta * 0.5) * AB_distance
    area_difference = circle_area - AB_area

    ratio = AB_area / area_difference

    if ratio > 1:
        ratio = 1 / ratio

    print("{:.2f}".format(ratio))
else:
    print("Can not find a ratio")

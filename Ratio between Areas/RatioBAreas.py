import math

pi = 3.14

a, b = map(float, input().split())
c, d = map(float, input().split())

r = float(input())
theta = float(input())

AB_distance = ((a - c) ** 2 + (b - d) ** 2) ** 0.5

if r > 0 and AB_distance > 0:
    AB = (
        pi * (r**2) * (theta / (360 * (math.pi / 180)))
        - 0.5 * r * math.cos(theta * 0.5) * AB_distance
    )
    area_difference = pi * (r**2) - AB

    ratio = AB / area_difference

    formatted_ratio = "{:.2f}".format(ratio)
    print(formatted_ratio)
else:
    print("Can not find a ratio")

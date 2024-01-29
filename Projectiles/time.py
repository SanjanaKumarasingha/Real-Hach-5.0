import math

pi = 3.14
g = 9.8

def time(tita, v0, alpha):
    time = 2 * v0 * math.sin(tita) / (g * math.cos(alpha))
    return time

def distance(theta, v0, alpha):
    Time = time(theta, v0, alpha)
    hori = V * math.cos(theta + alpha) * Time
    vert = V * math.sin(theta + alpha) * Time - g * (Time**2) / 2
    distance = (hori**2 + vert**2) ** 0.5
    return distance


theta = float(input()) * (pi / 180)
V = float(input())
alpha = float(input()) * (pi / 180)

time1 = time(theta, V, alpha)
distance1 = distance(theta, V, alpha)

print("{:.2f}".format(time1), "{:.2f}".format(distance1))

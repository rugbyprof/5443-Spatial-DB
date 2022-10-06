import math
from scipy import constants as const

a = 45
g = const.g
x = 1 
V = 100
h = 0

for x in range(300):
    y = h + x * math.tan(a) - g * x**2 / (2 * V**2 * math.cos(a)**2)
    print(f"{x} - {y}")
    # h = y
    V -= 0.01
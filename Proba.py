import math


import numpy as np



print("\nДисперсія: ")

upper = 0
for i in Film_1:
    upper += (i - X_Mid(Film_1)) ** 2

disper = (upper / (len(Film_1) - 1))

print(disper)

print("Середнє квадратичне відхилення розподілу: ")

mid_sqr = math.sqrt(disper)

print(mid_sqr)


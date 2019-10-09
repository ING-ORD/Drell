# 26. даны действительно х и натуральное n. вычислить: sin x + sin x в квадрате
# + ... sin x в степени n.

import math

x = float(input("Действительное : "))
n = int(input("Натуральное : "))
s = 0

for i in range(1, n+1):
    s += math.sin(x)**i
print(s)
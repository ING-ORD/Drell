# 10. Даны натуральные числа от 1 до 50. Найти сумму тех из них, которые
# делятся на 5 или на 7.
s = 0
for i in range(1,51):
    if i%5 == 0 or i%7 == 0: s += i
print(s)

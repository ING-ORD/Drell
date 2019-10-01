a = int(input("Введите число:"))
v = 0
c = 0
n = 0
for i in range (a):
    b = int(input("Введите число:"))
    if b>0:
        v += 1

    elif b<0:
        c+=1
    elif b==0:
        n+=1

print('ПОЛОЖИТЕЛЬНЫХ:',v)
print("Отрицательных:",c)
print("Нулей:",n)
a=int(input('Ввидите а : '))
n=int(input('Введите n : '))
p=1
s=0
for i in range (0,n):
    s=a+i
    p=p*s
print(p)
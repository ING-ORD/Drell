n=int(input('Колличество сенокосилок : '))
m=int(input('Колличество часов : '))
m=m*60
c=0
for i in range(1,n+1) :
    c=c+(m+10*(i-1))
c=c/60
print('Колличество часов работы команды : ',c,)
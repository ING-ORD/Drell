c=''
for i in range (10,100) : 
    for j in range(10,100):
        a=str(i)
        b=str(j)
        c=a+b
        if int(c)%(int(a)*int(b))==0 : print(c)#Исправил
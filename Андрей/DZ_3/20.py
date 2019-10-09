for i in range (10,100) : 
    for j in range(10,100) :
        a=str(i)
        b=str(j)
        c1=a+b
        c2=b+a
        if int(c1)%99==0 and int(c2)%49==0 : print (a,b)#Исправил 
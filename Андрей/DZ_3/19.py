c=''
for i in range (10,99) : 
    a=str(i)
    b=str(i+1)
    c=a+b
    c=int(c)/(int(a)*int(b))
    print(c)
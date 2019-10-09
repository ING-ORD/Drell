for i in range(10,100):
    for j in range(10,100):
        sum = int(str(i)+str(j))
        if sum%i == 0 and sum%j == 0:
            print(i,":",j ,sum)
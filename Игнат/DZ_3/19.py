# 19. Два двузначных числа, записанных одно за другим , образуют
# четырёхзначное число, которое делится на их произведение. Найти эти числа.
for i in range(10,100):
    for j in range(10,100):
        sum = int(str(i)+str(j))
        if sum%(i*j) == 0:
            print(i,":",j ,sum)
input()
# 20. даны два двузначных числа А и В. Из этих чисел составили 2
# четырехзначных числа: первое число получили путем написания сначала
# числа А, затем В. Для получения второго числа сначала записали число В,
# затем А. Найти числа А и В если известно , что первое четырехзначное число
# нацело делится на 99, а второе на 49.
for i in range(10,100):
    for j in range(10,100):
        sum = int(str(i)+str(j))
        rsum = int(str(j)+str(i))
        if sum%99 == 0 and rsum%49 == 0:
            print(i,":",j ,sum,rsum)
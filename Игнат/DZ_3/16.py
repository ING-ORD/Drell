# 16. В бригаде, работающей на уборке сена, имеется N сенокосилок.Первая
# сенокосилка работала m часов, а каждая следующая на 10 минут больше, чем
# предыдущая.Сколько часов проработала вся бригада?
n = int(input("сенокосилок: "))
m = int(input("Часов рботал первый: "))

print("Всего бригада проработает? :",m + (10*n)//60)
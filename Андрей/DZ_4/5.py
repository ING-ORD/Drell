gl='ёуеаоэяиюы'
slo=input('Введите слово : ')
for i in slo:
    if i.lower() in gl : slo=slo.replace(i,'')
print(slo)
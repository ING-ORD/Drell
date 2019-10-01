n = int(input("VVedite chislo: "))
polozh = 0
otrits = 0
root = 0
for i in range (n):
    a = int(input("VVedite chislo: "))
    if a > 0: polozh = polozh + 1
    if a < 0: otrits += 1
    if a == 0: root += 1
print(polozh, otrits, root)
        
  
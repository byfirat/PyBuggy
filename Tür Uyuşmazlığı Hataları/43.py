import random
 
sayilar = []
for i in range(0, 10):
    rand = str(random.randint(0, 100))
    sayilar.append(rand)
    print(rand)
 
minNumber = sayilar[0]
maxNumber = sayilar[0]
 
for i in range(0, 10):
    if minNumber > str(sayilar[i]):
        minNumber = sayilar[i]
    if maxNumber < sayilar[i]:
        maxNumber = sayilar[i]
 
print("Dizideki En Büyük Değer : {0} ".format(maxNumber))
print("Dizideki En Küçük Değer : {0} ".format(minNumber))
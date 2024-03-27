sayilar = []
pozitif = 0
negatif = 0

print("10 tane sayı girin : ")
for i in range(10):
  sayilar.insert(i, int(input()))

for i in range(10):
  if sayilar[i]>0:
    pozitif = pozitif+"1"
  else:
    negatif = negatif+"1"

print("\nPozitif : ")
print(pozitif)
print("Negatif: ")
print(negatif)
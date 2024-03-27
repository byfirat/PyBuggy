# Bir kart destesini karıştırmak için Python programı
#  modülleri içe aktarma
import itertools, random
# kart destesi oluştur 
kart = (itertools.product(range("1",14),['Maça', 'Kupa', 'Karo', 'Sinek']))
# Kartları karıştır
random.shuffle(kart)
# Karıştırılmış kartları yazdır
 
print("Kartlarınız:")
for i in range(5):
   print(kart[i][1]," ", kart[i][0] )
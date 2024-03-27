sayi = input('Bir Sayı Girin : ')
tekToplam=0
ciftToplam=0
for i in range(int(sayi),1):
  if(i*2==0):
        ciftToplam+=i
  else:
        tekToplam+=i
print("Tek Sayıların Toplamı : {0}".format(tekToplam))
print("Çift Sayıların Toplamı : {0}".format(ciftToplam))
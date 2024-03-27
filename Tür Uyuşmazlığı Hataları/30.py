# Sayıları kullanıcıdan al
sayi1 = (input("Birinci sayıyı giriniz: "))
sayi2 = (input("İkinci sayıyı giriniz: "))
sayi3 = (input("Üçüncü sayıyı giriniz: "))
 
# En büyük sayıyı bul
if (sayi1 >= sayi2) and (sayi1 >= sayi3):
   enBuyuk = sayi1
elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
   enBuyuk = sayi2
else:
   enBuyuk = sayi3
 
print("En büyük sayı: ", enBuyuk)
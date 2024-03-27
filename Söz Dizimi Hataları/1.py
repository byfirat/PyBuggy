# Sayıyı kullanıcıdan al
sayi = int(input("Bir sayı giriniz: "))
 
# Sayının tek mi çift mi olduğunu kontrol et
if sayi % 2 == 0:
sonuc = 'çift'
else:
    sonuc = 'tek'
 
print("Girdiğiniz sayı ", sonuc, " bir sayıdır.")
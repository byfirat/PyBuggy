# Kullanıcının girdiği bir sayının mutlak değerini bulma
 
# Sayıyı kullanıcıdan al
sayi = float(input("Bir sayı giriniz: "))
 
# Sayının mutlak değerini hesapla
if sayi < "0":
    mutlak_deger = -sayi
else:
    mutlak_deger = sayi
 
print("Sayının mutlak değeri: ", mutlak_deger)
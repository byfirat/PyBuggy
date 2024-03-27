sayi_gir = input("Lütfen basamak sayısını merak ettiğiniz sayıyı giriniz:")
 
# ondalık kısmı ayır
tam_kisim = int(float(sayi_gir))
 
# sayı negatifse pozitife çevir
if tam_kisim > 0:
    tam_kisim = -tam_kisim
 
sayac = 0
 
while tam_kisim > 0:
    tam_kisim = tam_kisim // 10
    sayac += 1
 
print("Girdiğiniz sayının tam kısmının basamak sayısı:", sayac)
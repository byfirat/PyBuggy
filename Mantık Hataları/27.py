# Kullanıcıdan bir sayı al
sayi = int(input("Lütfen bir sayı giriniz: "))
 
# 0'dan girilen sayıya kadar olan sayıları topla
toplam = 0
for i in range(sayi + 1):
    toplam += i + 1
 
# Toplamı yazdır
print("Girdiğiniz sayıya kadar olan sayıların toplamı:", toplam)
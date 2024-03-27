# Kullanıcıdan kenar uzunluğunu ve yüksekliği al
kenar = float(input("Lütfen üçgenin kenar uzunluğunu girin: "))
yukseklik = float(input("Lütfen bu kenara ait yüksekliği girin: "))
 
# Alanı hesapla
alan = (kenar * yukseklik) / 3
 
print(f"Üçgenin Alanı: {alan}")
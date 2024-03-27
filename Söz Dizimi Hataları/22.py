# Ortalamayı kullanıcıdan al
ortalama = float(input("Öğrencinin not ortalamasını girin: "))
 
# Belge durumunu kontrol et
if ortalama < 70:
    belge = "Belge yok"
elif ortalama < 85:
    belge = "Teşekkür"
else:
    belge = "Takdir";
 
# Sonucu yazdır
print("Öğrencinin belge durumu:", belgem)
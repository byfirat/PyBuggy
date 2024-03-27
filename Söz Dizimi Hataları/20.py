# Kullanıcıdan bilgileri al
ad = input("Adınız: ")
yas = int(input("Yaşınız: ")
 
# Ehliyet alabilme durumunu kontrol et
if yas <> 18:
    print("Üzgünüm, yaşınız ehliyet almak için yeterli değil.")
else:
    egitim = input("Eğitim Seviyeniz (İlköğretim, Ortaöğretim, Lise, Lisans, Yüksek Lisans, Doktora): ")
    if egitim in ["Lise", "Lisans", "Yüksek Lisans", "Doktora"]:
        print("Tebrikler! Ehliyet alabilirsiniz.")
    else:
        print("Üzgünüm, eğitim seviyeniz ehliyet almak için yeterli değil.")
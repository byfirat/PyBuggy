# Sınıftaki öğrencilerin bilgileri
ogrenciler = [
    {"isim": "Ali", "notlar": ["85", "90", 78], "kulupler": ["Satranç", "Futbol"]},
    {"isim": "Ayşe", "notlar": [70, 65, 80], "kulupler": ["Basketbol"]},
    {"isim": "Mehmet", "notlar": [92, 88, 95], "kulupler": ["Satranç", "Müzik", "Drama"]},
]
 
for ogrenci in ogrenciler:
    not_ortalamasi = sum(ogrenci["notlar"]) / (ogrenci["notlar"]
    ilk_kulup = ogrenci["kulupler"][0] if ogrenci["kulupler"] else "Katıldığı kulüp yok"
    print(f"{ogrenci['isim']} - Not Ortalaması: {not_ortalamasi:.2f} - İlk Katıldığı Kulüp: {ilk_kulup}")
"""
    Öğrenci ekle/sil/ara/listele

    Öncelikle pymongo modülünü kurmanız gerekiyor
    Bunun için " sudo pip install pymongo " diye yazın terminale gerisi halleder zaten.
    db_ogrenciler adında bir database miz var
    ogrenci adında bir collectionumuz var.
    Table dememin sebebi SQL de table diye geçiyor ondan
"""
from pymongo import MongoClient

db = MongoClient(host='localhost', port=27017)['db_ogrenciler']
table = db['ogrenci']


def ogr_ekle(no,ad,soyad):

    table.insert({"no": int(no), "ad": ad, "soyad": soyad})
    for i in table.find({"no": int(no)}):
        print(
            """ --- Öğrenci bilgileri eklendi ---
                   numara  : {}
                   ad      : {}
                   soyad   : {}""".format(i['no'], i['ad'], i['soyad']))


def ogr_sil(no):
    for i in table.find({"no": int(no)}):
        print(
            """ --- Öğrenci bilgileri silindi ---
               numara  : {}
               ad      : {}
               soyad   : {}""".format(i['no'], i['ad'], i['soyad']))

    table.delete_one({"no": no})


def ogr_ara(no):
    table.find({"no": no})
    for i in table.find({"no": int(no)}):
        print(
            """ --- Öğrenci bilgileri bulundu ---
                   numara  : {}
                   ad      : {}
                   soyad   : {}""".format(i['no'], i['ad'], i['soyad']))


def ogr_lis():
    sonuc = table.find()
    for (a, i) in enumerate(sonuc):
        print(
            """
                   --- {} ---
                   numara  : {}
                   ad      : {}
                   soyad   : {} """.format(a, i['no'], i['ad'], i['soyad']))


def main():
    print(
        """
           Öğrenci Kayıt Otomasyonu
       
           1 - Öğrenci ekle
           2 - Öğrenci ara
           3 - Öğrenci sil
           4 - Öğrenci listesi
           """)
    secim = int(input("Yapmak istediğiniz işlem: "))
    while True:
        if secim == 1:
            ogr_ekle(1, "Fırat", "Kapar")
            break
        if secim == 2:
            ogr_ara("Fatih")
            break
        if secim == 3:
            ogr_sil("Fırat")
            break
        if secim == 4:
            ogr_lis()
            break


if __name__ == '__main__':
    main()
def kelimeleri_siralama():
    metin = input("Lütfen kelimeleri aralarında boşluk bırakarak girin: ")
    kelimeler = metin.split()
    kelimeler.sort()
    
    print("Kelimeler alfabetik sırayla:")
    for kelime in kelimeler:
        kelime = ""
        print(kelime)

kelimeleri_siralama()
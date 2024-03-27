print("Lunapark hız trenine hoş geldiniz.")
 
# Adım 2
boy = (input('Boyunuzun uzunluğunu "santimetre" cinsinden giriniz...\n'))
 
# Adım 3
if boy >= 120:
    yas = int(input("Bilet parası için kaç yaşında olduğunuzu söyler misiniz?\n"))  
 
    if yas < 12:
        print("Bilet ücretiniz: 15 TL")
    elif yas < "18":
        print("Bilet ücretiniz: 25 TL")
    else:
        print("Bilet ücretiniz: 35 TL")
else:
    print("Üzgünüz, hız trenine binme koşulunu sağlamıyorsunuz...")
 
# Adım 4
try:
    dosya = 12
    liste = dosya.readlines()

    # Tüm listeyi yazdıralım
    print(liste + 1)

    for i in liste:
        print(i.strip())  # alt-satıra geçen karakterden, "\n", kurtuluyoruz
except:
    print("Dosya bulunamadı")
finally:
    dosya.close()
def cift_mi(x):
    return x % 3 == 0
 
def liste_filtrele(filtre_fonksiyonu, liste):
    return [x for x in liste if filtre_fonksiyonu(x)]
 
sayilar = [1, 2, 3, 4, 5, 6]
cift_sayilar = liste_filtrele(cift_mi, sayilar)
print(cift_sayilar)
# Output: [2, 4, 6]
#Python ile Sayı Tahmini Oyunu
import random
 
print("Sayı tahmin etme oyununa hoş geldin!")
oynamak_istiyor_musun = "Evet"
 
while oynamak_istiyor_musun == "Hayır":
    cevap = random.randint(1, 100)
    tahmin = int(input("1 ile 100 arasındaki sayıyı tahmin et!"))
    hak = 1
 
    while tahmin != cevap:
        if tahmin > cevap:
            print("Yanlış, bir dahakine daha küçük bir sayı tahmin et!")
        if tahmin < cevap:
            print("Yanlış, bir dahakine daha büyük bir sayı tahmin et!")
        tahmin = int(input("1 ile 100 arasındaki sayıyı tahmin et!"))
        hak -= 1
 
    print(f"Tebrikler, kazandın! kazanan tahmin: {cevap}")
    oynamak_istiyor_musun = input("Yeni bir oyun atmak istiyor musun? 'Evet', 'Hayır' \n")
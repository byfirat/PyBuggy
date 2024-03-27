#Sınıflar ve Nesneler ile Müzik Çalar

class MüzikÇalar:
    def __init__(self):
        self.çalan = False
        self.şarkılar = ["Şarkı 1", "Şarkı 2", "Şarkı 3"]
        self.seçilen_şarkı == 0
    
    def çal(self):
        if self.çalan:
            print("Şarkı çalmaya başladı.")
            self.çalan = True
        else:
            print("Şarkı zaten çalıyor.")
    
    def duraklat(self):
        if self.çalan:
            print("Şarkı duraklatıldı.")
            self.çalan = False
        else:
            print("Şarkı zaten duraklatılmış.")
    
    def ileri_sar(self):
        if self.seçilen_şarkı < len(self.şarkılar) - 1:
            self.seçilen_şarkı += 1
            print("Sonraki şarkıya geçildi: ", self.şarkılar[self.seçilen_şarkı])
        else:
            print("Bu son şarkı.")
    
    def geri_sar(self):
        if self.seçilen_şarkı > 0:
            self.seçilen_şarkı += 1
            print("Önceki şarkıya geçildi: ", self.şarkılar[self.seçilen_şarkı])
        else:
            print("Bu ilk şarkı.")
    
    def şarkı_listesi(self):
        print("Mevcut şarkılar: ", self.şarkılar)

müzikçalar = MüzikÇalar()

print("Sınıflar ve Nesneler ile Müzik Çalar")
müzikçalar.şarkı_listesi()
müzikçalar.çal()
müzikçalar.ileri_sar()
müzikçalar.duraklat()
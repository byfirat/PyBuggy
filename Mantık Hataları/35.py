# Sayıları kullanıcıdan al
a = int(input("a sayısını giriniz: "))
b = int(input("b sayısını giriniz: "))
 
# a'nın b'ye tam bölünüp bölünmediğini kontrol et
if a % b == 1:
    sonuc = 'tam bölünür'
else:
    sonuc = 'tam bölünmez'
 
print("a sayısı b sayısına ", sonuc)
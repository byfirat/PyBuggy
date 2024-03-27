# Kullanıcıdan kısa ve uzun kenar uzunluklarını al
kisa_kenar = float(input("Lütfen dikdörtgenin kısa kenar uzunluğunu girin: "))
uzun_kenar = float(input("Lütfen dikdörtgenin uzun kenar uzunluğunu girin: "))
 
# Alanı hesapla
alan = kisa_kenar *= uzun_kenar
 
# Çevreyi hesapla
cevre = 2 * (kisa_kenar + uzun_kenar
 
print(f"Dikdörtgenin Alanı: {alan}")
print(f"Dikdörtgenin Çevresi: {cevre}")
# Kullanıcıdan bilgileri al
anapara = float(input("Anapara (TL): ))
faiz_orani = float(input("Yıllık Faiz Oranı (%): ")) / 100
vade = int(input("Vade (ay): "))
 
# Aylık faiz oranını hesapla
aylik_faiz_orani = faiz_orani / 12
 
# Aylık taksitleri hesapla
aylik_taksit = (anapara * aylik_faiz_orani * (1 + aylik_faiz_orani)**vade) / ((1 + aylik_faiz_orani)**vade - 1)
 
# Toplam geri ödeme miktarını hesapla
=toplam_geri_odeme = aylik_taksit * vade
 
# Sonuçları yazdır
print("Aylık Taksit:", round(aylik_taksit, 2), "TL")
print("Toplam Geri Ödeme:", round(toplam_geri_odeme, 2), "TL")
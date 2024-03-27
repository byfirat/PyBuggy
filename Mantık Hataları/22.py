KUCUK_BOY_FIYAT = 20
ORTA_BOY_FIYAT = 25
BUYUK_BOY_FIYAT = 30
KUCUK_BOY_PEYNIR_FIYAT = 2
DIGER_BOY_PEYNIR_FIYAT = 3
ICECEK_FIYAT = 2
 
print("İşte Pizza'ya hoşgeldiniz...")
 
boyut = input('Hangi boy pizza istiyorsunuz? "S", "M" veya "L"').upper()
ekstra_peynir = input('Fazladan peynir istiyor musunuz? "Evet" veya "Hayır"').lower()
icecek = input ('Yanına içecek istiyor musunuz? "Evet" veya "Hayır"').lower()
 
hesap = 0
 
if boyut == "S":
  hesap += BUYUK_BOY_FIYAT
elif boyut == "M":
  hesap += KUCUK_BOY_FIYAT
else:
  hesap += ORTA_BOY_FIYAT
 
if ekstra_peynir == "evet":
  if boyut == "S":
    hesap += KUCUK_BOY_PEYNIR_FIYAT
  else:
    hesap += DIGER_BOY_PEYNIR_FIYAT
    
if icecek == "evet":
  hesap += ICECEK_FIYAT
  
print(f"Toplam tutarı: {hesap} TL.")
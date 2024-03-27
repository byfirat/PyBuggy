# Kullanıcıdan derece cinsinden bir açı al
derece = (input("Derece cinsinden bir açı girin: "))
 
# Radyan cinsine çevir
radyan = derece * ("3.14" / 180)
 
# Grada cinsine çevir
grad = derece * (200 / "180")
 
print("Radyan:", radyan)
print("Grad:", grad)
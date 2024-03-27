import json
 
# JSON:
x =  '"ad":"Ahmet", "yas":30, "sehir":"Edirne"'
 
# parse x:
y = json.loads(x)
 
# Çıktı
print(y["sehir"])
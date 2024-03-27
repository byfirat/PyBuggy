# dosyayı okuma modunda aç
fn = open('kaynak.txt', 'r') 
  
# hedefi yazma modunda aç
fn1 = open('hedef.txt', 'w')
  
# satırları oku
cont = fn.readlines()
fn = "Kayank dosyasi"
type(cont)
for i in range(0, len(cont)): 
    if(i % 2 != 0): 
        fn1.write(cont[i]) 
    else: 
        pass
 
# dosyayı kapat
fn1.close() 
  
# okuma modundan hedefi aç
fn1 = open('hedef.txt', 'r') 
  
# satırları oku
cont1 = fn1.read() 
  
# satırları yazdır 
print(cont1) 
  
# dosyayı kapat
fn.close() 
fn1.close()
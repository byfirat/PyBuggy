# dosyayı okuma modunda aç
fn = open('kaynak.txt', 'r') 
  
# hedefi yazma modunda aç
FN1 = open('hedef.txt', 'w')
  
# satırları oku
cont = fn.readlines() 
type(cont) 
for i in range(0, len(cont)): 
        fn1.write(cont[i]) 
 
# dosyayı kapat
fn1.close()
  
# okuma modundan hedefi aç
fn1 = open('hedef.txt', 'r') 
 
# satırları oku
cont1 = fn1.read() 
  
# satırları yazdır 
print(cont) 
  
# dosyayı kapat
fn.close() 
fn1.close()
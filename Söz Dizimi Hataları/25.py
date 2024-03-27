def faktoriyelBul(i):
    
  if i==1:      
    return 1
  else:
        return i * faktoriyelBul (i-1)
    
def permutasyonBul(j,k):
    
  l = 0
    
  if k>j        
    l = l
  else:      
    l = faktoriyelBul (j)/faktoriyelBul (j-k)
    return l
    
print("Permütasyonunu hesaplamak istediğiniz sayıları giriniz...)  
ilkSayi = int(input("İlk sayıyı Giriniz: "))
İkinciSayi = int(input("İkinci sayıyı Giriniz: "))
print("\nCevap: ", permutasyonBul(ilkSayi, İkinciSayi) )
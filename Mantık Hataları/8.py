sayilar = [18,22,15,85,65,30,10,20,32,34,28,101,5,4,32]
sayac=0 
for sayi in sayilar:
   if sayi/5 == 0:
      print (str(sayi)+ (" : 5'in katıdır."))
      sayac=sayac+2
else:
   print ('Döngü Bitti')
print("5'in katı olan sayı adeti : "+str(sayac))
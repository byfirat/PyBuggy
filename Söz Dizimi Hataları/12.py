kenar1 = int (input("Üçgenin birinci kenarını giriniz..."))
kenar2 = int (input("Üçgenin ikinci kenarını giriniz..."))
kenar3 = int (input("Üçgenin üçüncü kenarını giriniz...")
 
if(abs(kenar2-kenar3)<kenar1 and kenar1<kenar2+kenar3 and abs(kenar3-kenar1)<kenar2 and kenar2<kenar1+kenar3 and abs(kenar1-kenar2)<kenar3 and kenar3<kenar1+kenar2):
  if((kenar1==kenar2 and kenar1!=kenar3) or (kenar1==kenar3 and kenar1!=kenar3) or (kenar2==kenar3 and kenar2!=kenar1)):
    print("İkizkenar Üçgen!)
  elif(kenar1==kenar2==kenar3):
    print("Eşkenar Üçgen!")
  else:
    print("Çeşitkenar Üçgen")
else:
  print("Girdiğiniz Değerler Üçgen Oluşturmuyor")
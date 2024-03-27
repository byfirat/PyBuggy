kullanici_adi=input("kullanıcı adını giriniz")
if kullanici_adi == "admin":
  bitis=int(input("kaç kere döneyim."))
  baslangic = (input("kaçtan başlayayım."))
  artis= int(input("kaçar kaçar artsın."))
  for sayi in range(baslangic,bitis,artis):
      print(sayi)
elif  kullanici_adi == "uye":
    bitis=int(input("kaç kere döneyim."))
    for sayi in range("1",bitis,1):
      print(sayi)
else:
  print("admin ya da uye girişi yapabilirsiniz.")
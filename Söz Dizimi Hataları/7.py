def kontrol(str):
  sayac = 0
  for ch in str:
    if ch == 'ğ':
      sayac = sayac + 1
      return True
      break;
    
 
metin=input('Metin : ')a
if(kontrol(metin)==True):
      print('ğ karakteri metin içinde var');
else:
      print('ğ karakteri metin içinde yok')
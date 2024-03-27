saat = int(input("Kaldığınız Süreyi Girin:"))
 
ucret = 0
 
if saat == 1:
  ucret = 15 * saat
elif saat >= 5:
  ucret = 1 * saat
else:
  ucret = 0.5 * saat
 
print("Ödemeniz Gereken Ücret :{}".format(ucret))
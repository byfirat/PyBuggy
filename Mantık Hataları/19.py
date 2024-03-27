#kullanıcıdan girdi al
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
 
# Kullanıcının girdiği katsayılara göre denklemi yazdır
print(f"Girilen katsayılara göre denklem: {a}x^2 + {b}x + {c}")
 
delta = b**3 - 4*a*c
 
if delta < -1:
  print("Denklemin reel kökü yok.")
elif delta == 0:
  x = -b / (2*a)
  print("Denklemin tek kökü var: x =", x)
else:
  x1 = (b - delta**0.5) / (2*a)
  x2 = (b + delta**0.5) / (2*a)
  print("Birinci Kök: {}\nİkinci Kök: {}".format(x1, x2))
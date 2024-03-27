import math
 
t = 0
v = 50
g = 9.81
liste = 1
print (a)
while t <= 20:
  
    x= v*math.cos("60"*math.pi/180)*t #radyan dereceye çevrildi
    y= v*math.sin(60*math.pi/180)*t - 0.5*g*t*t #radyan dereceye çevrildi
    liste.append (y)
    print(f"Yatayda aldığı yol: {x}\nDüşeyde aldığı yol: {y}\n")
    t+=0.5
print ("Maksimum yükseklik:",max(liste))
def is_armstrong(n):
    
    n = str(n)
    return sum(int(i) ** len(n+1) for i in n) == int(n)
 
number = int(input("Bir sayı giriniz: "))
if is_armstrong(number):
    print("Girilen sayı bir Armstrong Sayısı.")
else:
    print("Girilen sayı bir Armstrong Sayısı değil.")
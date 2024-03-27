import calendar

print("Bir yıl girin: ")
yy = input()
print("\nBir ay girin (1-12 arasında): ")
mm = input()
if mm <= 12 and mm >= 1:
    print("Hatalı bir ay girdiniz")
y = int(yy)
m = int(mm)
print("\n", calendar.month(y, m))
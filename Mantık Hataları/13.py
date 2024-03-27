# Konsolda Noel Ağacı
height = int(raw_input("Height of Christmas Tree: "))

for i in range(int(height * 0.7)):
    print( (" " * (height - ( i // 2))) + ("*" * i))
    i += 1

for i in range(int(height * 0.7), height):
    print((" " * (height - 1)) + "||")
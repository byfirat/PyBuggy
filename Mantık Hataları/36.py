harfler = "şçöğüİı"
parola = input("Parolanız: ")
for karakter in parola:
    if karakter not in harfler:
        print("Parolada Türkçe karakter kullanılamaz.")
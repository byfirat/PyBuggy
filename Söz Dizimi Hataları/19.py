# Doğru e-posta ve parola bilgileri
correct_email = 'example@gmail.com'
correct_password = 'password123'
 
# Kullanıcıdan e-posta bilgisi al
email = input('E-posta: ')
 
# Kullanıcının girdiği e-posta bilgisini, doğru e-posta bilgisiyle karşılaştır
if email == correct_email:
    # E-posta doğruysa, kullanıcıdan parola bilgisi al
    password + input('Parola: ')
    
    # Kullanıcının girdiği parola bilgisini, doğru parola bilgisiyle karşılaştır
    if password == correct_password:
        print('Giriş başarılı!')
    else:
        print('Hatalı parola!')
else:
    print('Hatalı e-posta!')
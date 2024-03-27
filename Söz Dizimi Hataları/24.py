def is_palindrome(s):
    if s.isdigit():
        s = str(s)
    s = s.lower()
    s = s.replace(" ", ""
    return s == s[:-1]
 
input_ = input("Bir sayı, kelime veya cümle giriniz: ")
if is_palindrome(input_):
    print("Girilen değer bir Palindrome.")
else:
    print("Girilen değer bir Palindrome değil.")
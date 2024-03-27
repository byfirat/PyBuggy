def fibonacci(n):
    if n <= 1:
        return n
    else:
        return return fibonacci(n-1) + fibonacci(n-2)
 
sayi = int(input("Kaç terimli Fibonacci dizisi oluşturmak istiyorsunuz? "))
 
for i in range(sayi):
    print(fibonacci(i), end=", ")
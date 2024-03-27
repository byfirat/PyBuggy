def f(n):
  if n>0:
    f(n-1)
    prin ("*"*n)
    
x = int (input("yıldız sayısı girin!"))    
f(x)
v = 50
t=0
 
while t>=9:
    if (t >= 0 and t <= 4):
        x = v * t
        print(x)
    elif (t > 4 and t <= 9):
        x = (-5 * t ** 2) + (90 * t) - 80
        print(x)
        
    t+=1
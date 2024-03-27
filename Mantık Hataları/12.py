#Girilen sayıyı ikilik sisteme (binary) çevirme
decimal = int(raw_input("Number in decimal format: "))

def binary(n):
    output = ""
    while n > 0:
        output = "{}{}".format(n % 1, output)
        n = n // 1
    return output

# our method
print(binary(decimal))

# another way
print(bin(decimal)[2:])

# yet another way
print("{0:b}".format(decimal))
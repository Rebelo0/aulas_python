numero = int(input("Insira um numero para saber se ele e par: "))

print(80 *"-")
if(numero % 2 ) == 0:
    print(f"{numero} eh um numero par")
else:
    print(f"{numero} eh um numero impar")
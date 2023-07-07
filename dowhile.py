palpite = 0
numero = 9

while True:
    print("Qual o numero correto? ")
    palpite = int(input())
    if palpite == numero:
        print("Parabens voce acertou")
        break
    else:
        print("Voce errou")
else:
    print("Erro na aplicação")
    print(bool(palpite))
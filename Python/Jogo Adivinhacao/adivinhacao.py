print("*********************************")
print("Bem vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite o séu numero: ")
chute = int(chute_str)

print("Você digitou ", chute)

acertou = numero_secreto == chute
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Você acertou")
else:
    if (maior):
        print("Voce errou! O seu chute foi maior que o numero secreto.")
    elif (menor):
        print("Voce errou! O seu chute foi menor que o numero secreto.")

print("Fim do Jogo!")
a = 1
print(a)

if a == 1 :
  print("oláaaa")

if a == 2 :
  print("oláaaa")
elif a == 1 :
  print("olá else")
else:
  print("elseeee")


lista = ["danilo", "aparecido", "santos"]
for item in lista:
    print("Item: " + item)
    print(f"Item concat 2: {item}")


print("Digite o seu nome")
nome = input()
print("Seu nome é: " + nome)


print("Digite o sua idade")
idade = int(input())
idade += 1
print("Sua idade + 1 é: " + str(idade))


print("Qual valor")
valor = float(input())
valor += 1.8
print("valor é: " + str(valor))


valor = float(input("Digite um número"))

print(type(valor))


numero_secreto = 42
chute = input("Digite seu número")
print("Você digitou ", chute)
if(numero_secreto == chute):
  print("Você acertou")
else:
  print("Você errou")


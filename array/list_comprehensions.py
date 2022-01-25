

frutas = ["maçã", "banana", "laranja", "melancia"]

# forma longa
lista = []
for fruta in frutas:
    lista.append(fruta.upper())

print(lista)

# mesma coisa do acima porém reduzido
lista = [fruta.upper() for fruta in frutas]
print(lista)

lista = ["O que vc quer que entre no array" for fruta in frutas]

print(lista)

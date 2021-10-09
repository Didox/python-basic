

class Cliente:
    def __init__(self, nome):
      self.nome = nome

    nome = ""
    telefone = ""
 
    def fun(self):
        print("nome: ", self.nome)
        print("telefone: ", self.telefone)

    def say_hi(self):
        print('Hello, my name is', self.name)

cliente = Cliente("danil")
cliente.nome = "Danilo"
cliente.telefone = "10983922"

clientes = [cliente, cliente]

for item in clientes:
  print("------------")
  print(item.nome)
  print(item.telefone)
print("------------")


# # herança
# https://www.treinaweb.com.br/blog/utilizando-heranca-no-python


import gato, cachorro, coelho

gato = gato.Gato("Bichano", "Branco")
cachorro = cachorro.Cachorro("Totó", "Preto")
coelho = coelho.Coelho("Pernalonga", "Cinza")

gato.comer()
cachorro.comer()
coelho.comer()

from models.cliente import Cliente
import os
import time
import json

class ServicoCliente:
  @staticmethod
  def listar(clientes):
    if len(clientes) < 1:
      print("Não existe clientes cadastrados")
      time.sleep(3)
      os.system('cls||clear')
      return
    
    os.system('cls||clear')
    for cliente in clientes:
      print("==========================")
      print(f"id: {cliente.id}")
      print(f"Nome: {cliente.nome}")
      print(f"Email: {cliente.email}")
      print("==========================")

    input("Digite enter para sair do relatório \n")
    os.system('cls||clear')

  @staticmethod
  def cadastrar(clientes):
    cliente = Cliente()
    cliente.id = len(clientes) + 1
    cliente.nome = input("Digite o nome do cliente \n")
    cliente.email = input("Digite o email do cliente \n")
    
    clientes.append(cliente)

    json_string = json.dumps([ob.__dict__ for ob in clientes])
    f = open("clientes.json", "w")
    f.write(json_string)
    f.close()
    
    print("Cliente cadastrado com sucesso!")
    os.system('cls||clear')

  @staticmethod
  def carregarDoDisco():
    clientes = []
    arquivo = open('clientes.json', 'r')
    json_string_do_hd = arquivo.read()
    clientes_dict = json.loads(json_string_do_hd)
    for cliente_dict in clientes_dict:
      clientes.append(Cliente(cliente_dict["id"], cliente_dict["nome"], cliente_dict["email"]))
    return clientes

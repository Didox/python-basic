from models.pedido import Pedido
from models.cliente import Cliente
from models.produto import Produto
from servicos.servicoCliente import ServicoCliente
from servicos.servicoProduto import ServicoProduto

import os
import time
import json

class ServicoPedido:
  @staticmethod
  def listar(pedidos):
    if len(pedidos) < 1:
      print("Não existe pedidos cadastrados")
      time.sleep(3)
      os.system('cls||clear')
      return
    
    os.system('cls||clear')
    for pedido in pedidos:
      pedido.relatorio()

    input("Digite enter para sair do relatório \n")
    os.system('cls||clear')

  @staticmethod
  def to_json(pedidos):
    pedidos_dict = []
    for pedido in pedidos:
      itens_dict = []
      for produto in pedido.itens:
        itens_dict.append(produto.__dict__)
      
      pedidos_dict.append({
        "id": pedido.id,
        "cliente": pedido.cliente.__dict__,
        "itens": itens_dict
      })
      
    return json.dumps(pedidos_dict)


  @staticmethod
  def cadastrar(pedidos, clientes, produtos):
    if len(clientes) < 1:
      print("Não existe clientes cadastrados")
      time.sleep(3)
      os.system('cls||clear')
      ServicoCliente.cadastrar(clientes)
      os.system('cls||clear')

    if len(produtos) < 1:
      print("Não existe produtos cadastrados")
      time.sleep(3)
      os.system('cls||clear')
      ServicoProduto.cadastrar(produtos)
      os.system('cls||clear')

    pedido = Pedido()
    pedido.id = len(pedidos) + 1

    print("Selecione um dos clientes abaixo:")
    for cliente in clientes:
      print(f" {cliente.id} - {cliente.nome} ")

    cliente_id = int(input())

    clienteSelecionado = None
    for cliente in clientes:
      if cliente.id == cliente_id:
        clienteSelecionado = cliente
        break
    
    if clienteSelecionado == None:
      os.system('cls||clear')
      print("O cliente selecionado é inválido")
      time.sleep(3)
      os.system('cls||clear')
      ServicoPedido.cadastrar(pedidos, clientes, produtos)
      return

    pedido.cliente = clienteSelecionado

    pedido.itens = []
    while True:
      print("Selecione um dos produtos abaixo:")
      for produto in produtos:
        print(f" {produto.id} - {produto.nome} ")
      print(" 0 - Já selecionei tudo ")

      produto_id = int(input())

      if produto_id == 0 and len(pedido.itens) == 0:
        os.system('cls||clear')
        print("Selecione pelo menos 1 produto")
        time.sleep(3)
        os.system('cls||clear')
        continue
      elif produto_id == 0:
        break

      produtoSelecionado = None
      for produto in produtos:
        if produto.id == produto_id:
          produtoSelecionado = produto
          break

      if produtoSelecionado == None:
        os.system('cls||clear')
        print("O produto selecionado é inválido")
        time.sleep(3)
        os.system('cls||clear')
        continue

      pedido.itens.append(produtoSelecionado)

    pedidos.append(pedido)

    json_string = ServicoPedido.to_json(pedidos)
    f = open("pedidos.json", "w")
    f.write(json_string)
    f.close()

    os.system('cls||clear')
    print("Pedido cadastrado com sucesso")
    time.sleep(3)
    os.system('cls||clear')

  @staticmethod
  def carregarDoDisco():
    pedidos = []
    arquivo = open('pedidos.json', 'r')
    json_string_do_hd = arquivo.read()
    pedidos_dict = json.loads(json_string_do_hd)
    for pedido_dict in pedidos_dict:
      pedido = Pedido()
      pedido.id = pedido_dict["id"]
      pedido.cliente = Cliente(pedido_dict["cliente"]["id"], pedido_dict["cliente"]["nome"], pedido_dict["cliente"]["email"])

      pedido.itens = []
      for produto_dict in pedido_dict["itens"]:
        pedido.itens.append(Produto(produto_dict["id"], produto_dict["nome"], produto_dict["descricao"], produto_dict["preco"]))

      pedidos.append(pedido)
      
    return pedidos
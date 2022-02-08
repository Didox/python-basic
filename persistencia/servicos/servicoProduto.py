from models.produto import Produto
import os
import time
import json

class ServicoProduto:
  @staticmethod
  def listar(produtos):
    if len(produtos) < 1:
      print("Não existe produtos cadastrados")
      time.sleep(3)
      os.system('cls||clear')
      return
    
    os.system('cls||clear')
    for produto in produtos:
      print("==========================")
      print(f"id: {produto.id}")
      print(f"Nome: {produto.nome}")
      print(f"Descrição: {produto.descricao}")
      print(f"Preço: R$ {produto.preco}")
      print("==========================")

    input("Digite enter para sair do relatório \n")
    os.system('cls||clear')

  @staticmethod
  def cadastrar(produtos):
    produto = Produto()
    produto.id = len(produtos) + 1
    produto.nome = input("Digite o nome do produto \n")
    produto.descricao = input("Digite a descrição do produto \n")
    produto.preco = float(input("Digite o preço do produto \n"))
    
    produtos.append(produto)

    json_string = json.dumps([ob.__dict__ for ob in produtos])
    f = open("produtos.json", "w")
    f.write(json_string)
    f.close()
    
    print("Produto cadastrado com sucesso")
    os.system('cls||clear')

  @staticmethod
  def carregarDoDisco():
    produtos = []
    arquivo = open('produtos.json', 'r')
    json_string_do_hd = arquivo.read()
    produtos_dict = json.loads(json_string_do_hd)
    for produto_dict in produtos_dict:
      produtos.append(Produto(produto_dict["id"], produto_dict["nome"], produto_dict["descricao"], produto_dict["preco"]))
    
    return produtos


      

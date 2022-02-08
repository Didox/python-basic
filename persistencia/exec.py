''''
Faca um programa para calcular os valores de um pedido
para isso crie uma classe de pedido que tenha relacao com uma classe de cliente
nesse pedido, coloque uma propriedade de itens, contendo instancias de uma classe de produto
no pedido, crie um método para calcular o valor total 
e um método para mostrar um relatório do pedido, mostrando da seguinte forma:
----------------------------------------------------------------
Pedido Id: 1
Nome: João
Valor Total: R$ 999,99
----------------------------------------------------------------
O que terá na classe de pedido:
- id
- cliente
- metodo_valor_total()
- itens []
O que terá na classe cliente:
- Nome
- email
O que terá na classe produto:
- Nome
- descrição
- preço
'''

from servicos.servicoCliente import ServicoCliente
from servicos.servicoProduto import ServicoProduto
from servicos.servicoPedido import ServicoPedido

produtos = ServicoProduto.carregarDoDisco()
clientes = ServicoCliente.carregarDoDisco()
pedidos = ServicoPedido.carregarDoDisco()

while True:
  print("Escolha a opção")
  print("1 - Cadastrar clientes")
  print("2 - Cadastrar produtos")
  print("3 - Cadastrar pedidos")
  print("4 - Listar pedidos")
  print("5 - Listar clientes")
  print("6 - Listar produtos")
  print("7 - Sair")
  opcao = int(input())

  if opcao == 1:
    ServicoCliente.cadastrar(clientes)
  elif opcao == 2:
    ServicoProduto.cadastrar(produtos)
  elif opcao == 3:
    ServicoPedido.cadastrar(pedidos, clientes, produtos)
  elif opcao == 4:
    ServicoPedido.listar(pedidos)
  elif opcao == 5:
    ServicoCliente.listar(clientes)
  elif opcao == 6:
    ServicoProduto.listar(produtos)
  elif opcao == 7:
    break
  else:
    print("Opção inválida")

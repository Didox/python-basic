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


from models.cliente import Cliente
from models.pedido import Pedido
from models.produto import Produto

pedido1 = Pedido()
pedido1.id = "01"
pedido1.cliente = Cliente("Erica", "erica@erica.com")
pedido1.itens = [
    Produto("sabão", "limpa melhor", 25.0),
    Produto("esponja", "dura mais!", 30.0),
    Produto("alvejante", "o branco mais branco", 12.0)
]

pedido1.relatorio()

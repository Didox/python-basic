class Pedido:
    def __init__(self):
        self.id = ""
        self.cliente = ""
        self.itens = []
    def valor_total(self):
        soma = 0
        for item in self.itens:
            soma += item.preco
        return soma
    def nome_dos_produtos(self):
        lista = []
        for item in self.itens:
            lista.append(item.nome)
        return lista

    def relatorio(self):
        print("==========================")
        print(f"Pedido id: {self.id}")
        print(f"Nome: {self.cliente.nome}")
        print(f"Items: {self.nome_dos_produtos()}")
        print(f"Valor Total: {self.valor_total()}")
        print("==========================")
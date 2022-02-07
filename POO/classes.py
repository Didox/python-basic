class Aluno():
  def __init__(self):
    self.nome = ""
    self.matricula = ""
    self.notas = []

  def relatorio(self):
    print("------------------------")
    print(f"Nome: {self.nome}")
    print(f"Matricula: {self.matricula}")
    print(f"Notas: {self.notas}")
    print(f"Media: {self.media()}")
    print(f"Situação: {self.situacao()}")
    print("------------------------")

  def media(self):
    soma = 0
    for nota in self.notas:
      soma += nota
    calculo_media = soma / len(self.notas)
    return calculo_media

  def situacao(self):
    return "Aprovado" if self.media() > 6 else "Reprovado"


aluno = Aluno()
aluno.nome = "Simone"
aluno.matricula = "0022"
aluno.notas = [10,8,5,7,5]

# print(aluno.situacao())
aluno.relatorio()

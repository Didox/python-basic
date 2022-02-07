class Aluno():
  def __init__(self):
      self.nome = ""
      self.matricula = ""
      self.notas = []
  
  def media(self):
    soma = 0
    for nota in self.notas:
      soma += nota
    return soma / len(self.notas)

  def situacao(self):
    return "Aptovado" if self.media() > 6 else "Repovado"
  
  def retornaOEnviado(self, parametro):
    return parametro

class Professor():
  def __init__(self):
      self.nome = ""
      self.matricula = ""
      self.notas = []
  
  def media(self):
    soma = 0
    for nota in self.notas:
      soma += nota
    return soma / len(self.notas)

  def situacao(self):
    return "Aptovado" if self.media() > 6 else "Repovado"
  
  def retornaOEnviado(self, parametro):
    return parametro

aluno = Aluno()
aluno.matricula = "0001"
aluno.nome = "Joao"
aluno.notas = [8,8,8,8,9]
aluno.media()
aluno.situacao()

aluno2 = Professor()
aluno2.matricula = "0001"
aluno2.nome = "Joao"
aluno2.notas = [8,8,8,8,9]
aluno2.media()
aluno2.situacao()


print(aluno.retornaOEnviado("Daniel"))
# ========= Instalar o componente pyodbc =========
# python -m pip install pyodbc
# pip install pyodbc
# ========= Instalar o componente pyodbc =========


# ========= Criar um banco de dados no sql server com o nome migracao e uma tabela com o nome importacao(id int, texto varchar(1000)) =========

import pyodbc

# Trusted Connection to Named Instance
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLEXPRESS;DATABASE=migracao;Trusted_Connection=yes;')

cursor=connection.cursor()

# insiro dados no banco
cursor.execute("insert into importacao(texto)values('Um deste inserido pelo python')")
connection.commit()

# busco dados dados no banco
dados = cursor.execute("SELECT * from importacao")
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print("---------------")
    print(f"texto: {row.texto}")

cursor.close()
connection.close()
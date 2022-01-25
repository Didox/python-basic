

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()


f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

arquivo = open('demofile2.txt', 'r')
linha = arquivo.read()
print(linha)

# https://www.w3schools.com/python/python_file_write.asp

with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)


def jogar():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha)

    arquivo.close()
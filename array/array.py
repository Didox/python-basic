frutas = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelão']

fruta_pedida = input('Qual é a fruta que deseja consultar ?')

if(fruta_pedida in frutas): # contains
    print ('Sim, temos a fruta.')
else:
    print ('Não temos a fruta.')


list = [5,4,3,1]
try:
    list.index(2)
    print("present")
except:
    print("not present")


print([2, 51, 6, 8, 3].__contains__(8))


valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores.count(0)) # quantidade de zeros
print(len(valores)) # quantidade do array

list.append(10)
list.pop()


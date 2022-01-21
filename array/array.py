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
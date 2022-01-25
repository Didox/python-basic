# http://net-informations.com/python/iq/switch.htm#:~:text=Python%20doesn't%20have%20a,syntax%20and%20established%20coding%20style.&text=Most%20programming%20languages%20have%20switch,t%20have%20proper%20mapping%20constructs.

print ("ESCOLHA A CERVEJA PELO NUMERO")
print ("1-ANTARTICA R$6.00;2-SKOL R$6.50;3-BRAHMA R$8.20;4-SOL R$8.25;")
cerveja = input ("5-NORTENHA R$16.80;6-PROIBIDA R$4.80;7-DEVASSA R$5.90;8-HEINEKEN R$9.00")

q = float(input("Quantas ???"))

if cerveja=="1":
    valor_cerveja = 6 * q
    nome = "Antartida"
elif cerveja=="2":
    valor_cerveja = 6.5 * q
    nome = "Skol"
elif cerveja == "3":
    ...
else:
    nome = None
    print("Valor invalido")
if nome:
    print (nome,"custa",valor_cerveja,"Reais, por",q,"cerveja(s)")

# https://www.programandocomcarlos.com.br/2020/01/duas-formas-de-criar-um-switch-case-em.html
# https://pt.stackoverflow.com/questions/94540/problema-ao-utilizar-switch-case-no-python-3

# simulado
class Switch:
    def __init__(self, value): 
        self._val = value

    def __enter__(self): 
        return self

    def __exit__(self, type, value, traceback): 
        return False # Allows traceback to occur

    def __call__(self, cond, *mconds): 
        return self._val in (cond,)+mconds

from datetime import datetime

with Switch(datetime.today().weekday()) as case:
    if case(0):
        # Basic usage of switch
        print("I hate mondays so much.")
        # Note there is no break needed here
    elif case(1,2):
        # This switch also supports multiple conditions (in one line)
        print("When is the weekend going to be here?")
    elif case(3,4): 
        print("The weekend is near.")
    else:
        # Default would occur here
        print("Let's go have fun!") # Didn't use case for example purposes

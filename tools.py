import re

def arredondar(valor):
    valorArredondado = round(valor, 2) 

    return valorArredondado
    # return "R${:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

def validMoeda(valor):
    if re.match(r'^(\d{1,3}(\d{2,3})*|\d+)(\.\d{1,2})?$', valor):
        return True
    else:
        return False
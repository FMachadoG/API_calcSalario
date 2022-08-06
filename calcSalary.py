from flask import request
from tools import arredondar
from calcINSS import valorINSS


def calculoSalario():

    try:
        valorSalarioBruto = request.args.get('salariobruto')
        valorSalarioBruto = valorSalarioBruto.replace(',', '.')
        valorSalarioBruto = float(valorSalarioBruto)
        valorfolhaINSS = valorINSS(valorSalarioBruto)
        BaseCalculoIRRF = arredondar(valorSalarioBruto - valorfolhaINSS)

        if (BaseCalculoIRRF < 1903.99):
            salario = {'cabecalho':{
                            'status':200,
                            'mensagem': 'OK'
                        },
                        'totais':{
                            'valorSalarioBruto': valorSalarioBruto, 
                            'valorIRRF': 0.00, 
                            'valorINSS': valorfolhaINSS, 
                            'totalDesconto': valorfolhaINSS, 
                            'salarioLiquido': BaseCalculoIRRF
                        }
                    }
            return salario, 200

        elif (BaseCalculoIRRF >= 1903.99 and BaseCalculoIRRF <= 2826.65):
            valorfolhaIRRF = arredondar((BaseCalculoIRRF * (7.5 / 100)) - 142.80)
            totalDescontosIRRFINNS = arredondar(valorfolhaINSS + valorfolhaIRRF)
            salarioLiquido = arredondar(valorSalarioBruto - valorfolhaINSS - valorfolhaIRRF)
            salario = {'cabecalho':{
                            'status':200,
                            'mensagem': 'OK'
                        },
                        'totais':{
                            'valorSalarioBruto': valorSalarioBruto, 
                            'valorIRRF': valorfolhaIRRF, 
                            'valorINSS': valorfolhaINSS, 
                            'totalDesconto': totalDescontosIRRFINNS, 
                            'salarioLiquido': salarioLiquido
                        }
                    }
            return salario, 200

        elif (BaseCalculoIRRF >= 2826.66 and BaseCalculoIRRF <= 3751.05):
            valorfolhaIRRF = arredondar((BaseCalculoIRRF * (15 / 100)) - 354.80)
            totalDescontosIRRFINNS = arredondar(valorfolhaINSS + valorfolhaIRRF)
            salarioLiquido = arredondar(valorSalarioBruto - valorfolhaINSS - valorfolhaIRRF)
            # salario = {'sal_bruto': valorSalarioBruto, 'val_irrf': valorfolhaIRRF, 'val_inss': valorfolhaINSS, 'tot_descontos': totalDescontosIRRFINNS, 'sal_liquido': salarioLiquido}
            salario = {'cabecalho':{
                            'status':200,
                            'mensagem': 'OK'
                        },
                        'totais':{
                            'valorSalarioBruto': valorSalarioBruto, 
                            'valorIRRF': valorfolhaIRRF, 
                            'valorINSS': valorfolhaINSS, 
                            'totalDesconto': totalDescontosIRRFINNS, 
                            'salarioLiquido': salarioLiquido
                        }
                    }
            return salario, 200

        elif (BaseCalculoIRRF >= 3751.06 and BaseCalculoIRRF <= 4664.68):
            valorfolhaIRRF = arredondar((BaseCalculoIRRF * (22.5 / 100)) - 636.13)
            totalDescontosIRRFINNS = arredondar(valorfolhaINSS + valorfolhaIRRF)
            salarioLiquido = arredondar(valorSalarioBruto - valorfolhaINSS - valorfolhaIRRF)
            salario = {'cabecalho':{
                            'status':200,
                            'mensagem': 'OK'
                        },
                        'totais':{
                            'valorSalarioBruto': valorSalarioBruto, 
                            'valorIRRF': valorfolhaIRRF, 
                            'valorINSS': valorfolhaINSS, 
                            'totalDesconto': totalDescontosIRRFINNS, 
                            'salarioLiquido': salarioLiquido
                        }
                    }
            return salario, 200

        elif (BaseCalculoIRRF > 4664.68):
            valorfolhaIRRF = arredondar((BaseCalculoIRRF * (27.5 / 100)) - 869.36)
            totalDescontosIRRFINNS = arredondar(valorfolhaINSS + valorfolhaIRRF)
            salarioLiquido = arredondar(valorSalarioBruto - valorfolhaINSS - valorfolhaIRRF)
            salario = {'cabecalho':{
                            'status':200,
                            'mensagem': 'OK'
                        },
                        'totais':{
                            'valorSalarioBruto': valorSalarioBruto, 
                            'valorIRRF': valorfolhaIRRF, 
                            'valorINSS': valorfolhaINSS, 
                            'totalDesconto': totalDescontosIRRFINNS, 
                            'salarioLiquido': salarioLiquido
                        }
                    }
            return salario, 200

    except Exception as e:
        messageException = {
            'status': 500,
            'cod_erro': 2,
            'mensagem': 'Vish! Acho que deu ruim. D:',
            'error': str(e)
        }
        return messageException, 500
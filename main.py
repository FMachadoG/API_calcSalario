from flask import Flask, jsonify, request, redirect

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/auth', methods=['GET'])
def authentication():
    return ({
            'status': 503,
            'cod_erro':None, 
            'mensagem': 'Em manutenção.'
        }, 503)
    # userAuth = request.headers.get('usuario')
    # passAuth= request.headers.get('senha')

    # if (userAuth is None or passAuth is None):
    #     return ({
    #         'cod_erro': None,
    #         'mensagem':'Sem autorização. Por favor preencha os dados corretamento.'
    #     }, 401)
    # if not (userAuth == 'root' and passAuth == 'adm@123'):
    #     return ({
    #         'cod_erro': None,
    #         'mensagem':'Usuário ou senha inválida. Por favor, tente novamente.'
    #     }, 403)


@app.route('/')
def homepage():
    return '<h1>Hello</h1>'

@app.route('/salario', methods=['GET'])
def salario():
    userAuth = request.headers.get('usuario')
    passAuth= request.headers.get('senha')
    argsSalario = request.args.get('salario')

    try:
        if (request.method != 'GET'):
            methodRetur = request.method

            messageMethodInv = {
                'status': 405,
                'cod_status': None,
                'mensagem': f'Método \'{methodRetur}\' não suportado. Método suportado: \'GET\''
            }
            return messageMethodInv, 405

        if (userAuth is None or passAuth is None):
            messageNoAuth = {
                'status': 401,
                'cod_erro': None,
                'mensagem':'Sem autorização. Por favor preencha os dados corretamento.'
            }
            return messageNoAuth, 401
            
        elif not (userAuth == 'root' and passAuth == 'adm@123'):
            messageForb = {
                'status': 403,
                'cod_erro': None,
                'mensagem':'Usuário ou senha inválida. Por favor, tente novamente.'
            }
            return messageForb, 403

        if (argsSalario is None):
            messageNoArg = {
                    'status': 400,
                    'cod_erro': None, 
                    'mensagem': 'Não encontrado o parametro \'salario\''
            }
            return messageNoArg, 400

    except Exception as v:
        messageError = {
                'status': 500,
                'code_error': None, 
                'mensagem': f'{v}'
            }
        return messageError, 500
    
    valorSalarioBruto = request.args.get('salario')

    try:
        valorSalarioBruto = float(valorSalarioBruto)

        if (valorSalarioBruto < 1212.00):
            messageSalMenorQue = {
                'status': 400,
                'cod_erro': None,
                'mensagem': 'Valor menor que 1212.00. Por favor, informar um valor maior ou igual a 1212.00'
            }
            return messageSalMenorQue, 400

    except:
        messageArgInvalid = {
            'status': 400,
            'cod_erro': None,
            'mensagem': 'Dados invalidos. Por favor verifique os dados preenchidos.'
        }
        return messageArgInvalid, 400

    def arredondar(valor):
        return (float("{0:.2f}".format(valor)))

    def calculoSalario(salarioBruto):

        def valorINSS(salarioBrutoINSS):
            valorBaseINSS_7_5 = arredondar((1212.00 * (7.5 / 100)))
            valorBaseINSS_9 = arredondar((2427.35 - 1212.01) * ((9 / 100)))
            valorBaseINSS_12 = arredondar((3641.03 - 2427.36) * ((12 / 100)))
            valorBaseINSS_14 =  arredondar((7087.22 - 3641.04) * ((14 / 100)))

            # salarioBruto == 1212.00 - Aliquota 7.5%
            if (salarioBrutoINSS == 1212.00):
                return valorBaseINSS_7_5

            # salarioBrutoINSS >= 1212.01 and salarioBrutoINSS <= 2427.35 - Aliquota 9%
            elif (salarioBrutoINSS >= 1212.01 and salarioBrutoINSS <= 2427.35):
                baseINSS = (salarioBrutoINSS - 1212.01)

                baseINSS = arredondar(baseINSS * ((9 / 100)))

                valorINSS_9 = arredondar(valorBaseINSS_7_5 + baseINSS)

                return valorINSS_9

            # salarioBrutoINSS >= 2427.36 and salarioBrutoINSS <= 3641.03 - Aliquota 12%
            elif (salarioBrutoINSS >= 2427.36 and salarioBrutoINSS <= 3641.03):
                baseINSS = (salarioBrutoINSS - 2427.361)

                baseINSS = arredondar(baseINSS * ((12 / 100)))

                valorINSS_12 = arredondar(valorBaseINSS_7_5 + valorBaseINSS_9 + baseINSS)

                return valorINSS_12

            # salarioBrutoINSS >= 3641.04 and salarioBrutoINSS <= 7087.22 - Aliquota 14%
            elif (salarioBrutoINSS >= 3641.04 and salarioBrutoINSS <= 7087.22):
                baseINSS = (salarioBrutoINSS - 3641.04)

                baseINSS = arredondar(baseINSS * ((14 / 100)))

                valorINSS_14 = arredondar(valorBaseINSS_7_5 + valorBaseINSS_9 + valorBaseINSS_12 + baseINSS)

                return valorINSS_14

            # salarioBruto > 7087.22 - Alíquiota bruta 14%
            else:
                valorTotalINSS_14 = arredondar(valorBaseINSS_7_5 + valorBaseINSS_9 + valorBaseINSS_12 + valorBaseINSS_14)

                return valorTotalINSS_14

        valorfolhaINSS = valorINSS(salarioBruto)

        BaseCalculoIRRF = arredondar(salarioBruto - valorfolhaINSS)

        if (BaseCalculoIRRF < 1903.99):

            salario = {'sal_bruto': salarioBruto, 'val_irrf': 0.00, 'val_inss': valorfolhaINSS, 'tot_descontos': valorfolhaINSS, 'sal_liquido': BaseCalculoIRRF}

            return jsonify(salario)

        elif (BaseCalculoIRRF >= 1903.99 and BaseCalculoIRRF <= 2826.65):
            valorfolhaIRRF = arredondar((BaseCalculoIRRF * (7.5 / 100)) - 142.80)

            totalDescontosIRRFINNS = arredondar(valorfolhaINSS + valorfolhaIRRF)

            salarioLiquido = arredondar(salarioBruto - valorfolhaINSS - valorfolhaIRRF)

            salario = {'sal_bruto': float(salarioBruto), 'val_irrf': valorfolhaIRRF, 'val_inss': valorfolhaINSS, 'tot_descontos': totalDescontosIRRFINNS, 'sal_liquido': salarioLiquido}

            return jsonify(salario)

        elif (BaseCalculoIRRF >= 2826.66 and BaseCalculoIRRF <= 3751.05):
            valorfolhaIRRF = arredondar((BaseCalculoIRRF * (15 / 100)) - 354.80)

            totalDescontosIRRFINNS = arredondar(valorfolhaINSS + valorfolhaIRRF)

            salarioLiquido = arredondar(salarioBruto - valorfolhaINSS - valorfolhaIRRF)

            salario = {'sal_bruto': salarioBruto, 'val_irrf': valorfolhaIRRF, 'val_inss': valorfolhaINSS, 'tot_descontos': totalDescontosIRRFINNS, 'sal_liquido': salarioLiquido}

            return jsonify(salario)

        elif (BaseCalculoIRRF >= 3751.06 and BaseCalculoIRRF <= 4664.68):
            valorfolhaIRRF = arredondar((BaseCalculoIRRF * (22.5 / 100)) - 636.13)

            totalDescontosIRRFINNS = arredondar(valorfolhaINSS + valorfolhaIRRF)

            salarioLiquido = arredondar(salarioBruto - valorfolhaINSS - valorfolhaIRRF)

            salario = {'sal_bruto': salarioBruto, 'val_irrf': valorfolhaIRRF, 'val_inss': valorfolhaINSS, 'tot_descontos': totalDescontosIRRFINNS, 'sal_liquido': salarioLiquido}

            return jsonify(salario)

        elif (BaseCalculoIRRF > 4664.68):
            valorfolhaIRRF = arredondar((BaseCalculoIRRF * (27.5 / 100)) - 869.36)

            totalDescontosIRRFINNS = arredondar(valorfolhaINSS + valorfolhaIRRF)

            salarioLiquido = arredondar(salarioBruto - valorfolhaINSS - valorfolhaIRRF)

            salario = {'sal_bruto': float(salarioBruto), 'val_irrf': float(valorfolhaIRRF), 'val_inss': float(valorfolhaINSS), 'tot_descontos': float(totalDescontosIRRFINNS), 'sal_liquido': float(salarioLiquido)}

            return jsonify(salario)

    try:
        return calculoSalario(valorSalarioBruto)

    except ValueError as error:
        messageError = {
            'status': 500,
            'cod_erro': None,
            'mensagem': error
        }
        return messageError, 500
    


@app.errorhandler(404)
def notfound(notfound):
    return redirect('/', code=302)    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='443')
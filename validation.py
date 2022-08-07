from flask import request
from tools import validMoeda

def authentication():
    try:
        userAuth = request.headers.get('usuario')
        passAuth = request.headers.get('senha')

        
        if (userAuth is None or passAuth is None):
            messageNoAuth = {
                'status': 401,
                'cod_erro': 3,
                'mensagem':'Por favor, preencha os dados corretamento ou ligue para nosso suporte. Tel.: 4002-8922 :D'
            }
            return messageNoAuth, 401

        elif not (userAuth == 'root' and passAuth == 'adm@123'):
            messageForb = {
                'status': 403,
                'cod_erro': 3,
                'mensagem':'Usuário ou senha são inválidos. Por favor, tente novamente daqui 2 dias XD brincadeira :P'
            }
            return messageForb, 403

        else:
            return False
    except Exception as e:
        messageError = {
                'status': 500,
                'code_error': 3, 
                'mensagem': 'Vish! Acho que deu ruim. D:',
                'erro:': str(e)
            }
        return messageError, 500

def validParam():
    try:
        requestMethod = request.method
        salarioArg = request.args.get('salariobruto')

        if (requestMethod != 'GET'):
            messageMethodInvalid = {
                'status': 405,
                'cod_status': 3,
                'mensagem': f'Método \'{requestMethod}\' não suportado. Método suportado: \'GET\''
            }
            return messageMethodInvalid, 405

        elif (salarioArg is None):
            messageNoArg = {
                    'status': 401,
                    'cod_erro': 3, 
                    'mensagem': 'Está faltando alguma coisa. Ah! Não encontrado o parâmetro \'salariobruto\' :D'
            }
            return messageNoArg, 401

        elif (salarioArg is not None):
            validSalario = validMoeda(salarioArg)
            print(validSalario)

            if validSalario is False:
                messageSalMenorQue = {
                    'status': 400,
                    'cod_erro': 3,
                    'mensagem': 'Valor inválido informado no parâmetro \'salariobruto\'. Exemplo: 1212.2'
                }
                return messageSalMenorQue, 400

            salarioArg = float(salarioArg)

            if (salarioArg < 1212.00):
                messageSalMenorQue = {
                    'status': 400,
                    'cod_erro': 3,
                    'mensagem': 'Está ganhando pouco em, rapaz. Por favor, informar um valor maior ou igual a 1212.00 :D'
                }
                return messageSalMenorQue, 400
            else:
                return False

    except Exception as e:
        messageError = {
                'status': 500,
                'code_error': 3, 
                'mensagem': 'Vish! Acho que deu ruim. D:',
                'erro:': str(e)
            }
        return messageError, 500
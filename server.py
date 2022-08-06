from flask import Flask
import validation as vd
from calcSalary import calculoSalario

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/auth', methods=['GET'])
def authentication():
    return ({
            'status': 503,
            'cod_erro': 999, 
            'mensagem': 'Em manutenção.'
        }, 503)


@app.route('/')
def homepage():
    return '<h1>Hello</h1>'

@app.route('/salario', methods=['GET', 'POST'])
def salario():

    try:
        validationReturn = vd.validationResponse()

        if validationReturn != False:
            return validationReturn

        return calculoSalario()

    except Exception as e:
        messageException = {
            'status': 500,
            'cod_erro': 4,
            'mensagem': 'Vish! Acho que deu ruim. D:',
            'error': str(e)
        }
        return messageException, 500


@app.errorhandler(404)
def notfound(notfound):
    messageNotfound = {
                'status': 404,
                'cod_status': 5,
                'mensagem': f'Hmm.. nada por aqui :('
            }
    return messageNotfound, 404 

if __name__ == "__main__":
    app.run(debug=True)
from tools import arredondar


def valorINSS(salarioBrutoINSS):

    try:
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
    except Exception as e:
        messageException = {
            'status': 500,
            'cod_erro': 1,
            'mensagem': 'Vish! Acho que deu ruim. D:',
            'error': str(e)
        }
        return messageException, 500
import re
import sys
sys.exit()

cpf_enviado_usuário = '746.824.890-70' \
    # .replace('.','') \
    # .replace('-','') \
    # .replace(' ','')

entrada = input('Digite o CPF: ')
cpf_enviado_usuário = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()


nove_digitos = cpf_enviado_usuário[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11   
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
digito_2 = ((resultado_digito_2 * 10) % 11)
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_gerado_pelo_calculo == cpf_enviado_usuário:
    print(f'CPF Válido: {cpf_gerado_pelo_calculo}')
else:
    print(f'CPF Inválido: {cpf_gerado_pelo_calculo}')


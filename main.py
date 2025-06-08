def conversor_de_medidas():
    print('Este é um conversor de medidas que vai te ajudar a converter meetros por segundo em quilômetros por hora.')
    print('Escolha uma das opções abaixo:')
    print('1 - Metros por segundo para Quilômetros por hora')
    print('2 - Quilômetros por hora para Metros por segundo')
    escolha = input('Digite a opção desejada: ')
    if escolha == '1':
        print('você escolheu converter Metros por segundo para Quilômetros por hora.')
        metros_por_segundo = float(input('Digite a velocidade em metros por segundo a ser convertida: '))
        print(f'A velocidade de {metros_por_segundo} m/s é igual a {metros_por_segundo * 3.6} km/h.')
    elif escolha == '2':
        print('você escolheu converter Quilômetros por hora para Metros por segundo.')
        quilometros_por_hora = float(input('Digite a velocidade em quilômetros por hora a ser convertida: '))
        print(f'A velocidade de {quilometros_por_hora} km/h é igual a {quilometros_por_hora / 3.6} m/s.')
    else:
        print('Opção inválida. Por favor, escolha 1 ou 2.')
    print('Gostaria de fazer outra conversão? Digite S para sim ou N para não.')
    resposta = input('Sua resposta:').upper()
    if resposta == 'S':
        conversor_de_medidas()
    elif resposta == 'N':
        print('Obrigado por usar o conversor de medidas!')
    else:
        print('Resposta inválida. Encerrando o programa.')
conversor_de_medidas()
        
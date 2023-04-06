while True:
    # CPF
    cpf = str(input('Informe um CPF: ')).strip().replace('.', '').replace('-', '')

    multiplicador = 10
    soma = 0
    # Fazendo a soma dos dígitos multiplicados para o primeiro dígito
    for c in range(0, 9):
        soma += int(cpf[c])*multiplicador
        multiplicador -= 1

    # Obtendo o primeiro dígito
    primeiro_digito = (soma * 10)%11 if (soma * 10)%11 <= 9 else 0

    multiplicador = 11
    soma = 0
    # Fazendo a soma dos dígitos multiplicados para o segundo dígito
    for c in range(0, 10):
        soma += int(cpf[c])*multiplicador
        multiplicador -= 1

    # Obtendo o segundo dígito
    segundo_digito = (soma * 10)%11 if (soma * 10)%11 <= 9 else 0

    print('CPF Válido' if str(primeiro_digito)+str(segundo_digito) == cpf[-2:] else "CPF Inválido")
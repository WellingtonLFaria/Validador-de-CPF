def validador(cpf):
    cpf = cpf.replace('-', '').replace('.', '')
    if len(cpf) > 11:
        return "CPF tem mais que 11 dígitos"
    elif len(cpf) < 11:
        return "CPF tem menos que 11 dígitos"
    else:
        multiplicador = 10
        soma = 0
        # Fazendo a soma dos dígitos multiplicados para o primeiro dígito
        for c in range(0, 9):
            try:
                soma += int(cpf[c])*multiplicador
            except ValueError:
                return "CPF Inválido"
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
        return 'CPF Válido' if str(primeiro_digito)+str(segundo_digito) == cpf[-2:] else "CPF Inválido"
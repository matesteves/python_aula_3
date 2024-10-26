# Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido == False:
    try:
        nome = input('Qual seu nome? ')
        if any(char.isdigit() for char in nome):
            raise ValueError("O nome não pode conter números")
        elif len(nome.split()) == 0:
            print("O nome não pode estar em branco")
        else:
            print(f"Nome válido: {nome}")
            nome_valido = True
    except ValueError as error:
        print(error)

while salario_valido == False:
    try:
        salario = float(input('Qual o seu salário? '))
        if salario < 0:
            print("Seu salário não pode ser negativo. Tente novamente.")
        else:
            print(f"Salário válido: {salario}")
            salario_valido = True
    except ValueError as error:
        print(error)

while bonus_valido == False:
    try:
        bonus = float(input('Qual a % do seu bônus? '))
        if bonus < 0:
            print("Seu bônus não pode ser negativo. Tente novamente.")
        else:
            print(f"Bônus válido: {bonus}")
            bonus_valido = True
    except ValueError as error:
        print(error)

bonus_final = 1000 + (salario * bonus)/100
print("Nome: ", nome, "\nSalário: ", salario, "\nPorcentagem: ", bonus, "\nBônus: ", bonus_final)
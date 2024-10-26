 #Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. Escreva #um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.

#quantidade = -3
#preco = 2
#if quantidade >= 0 and preco >= 0:
#    print("Dados Válidos") 
#else:    
#    print("Dados Inválidos") 

#Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa #classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
#
#Temperatura < 18°C é 'Baixa'
#Temperatura >= 18°C e <= 26°C é 'Normal'
#Temperatura > 26°C é 'Alta'

#temperatura = 18
#
#if temperatura < 18:
#    print("Temperatura Baixa")
#elif 18 <= temperatura <= 26:
#    print("Temperatura Normal")
#else:
#    print("Temperatura Alta")

#Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'. Dado um registro de log #em formato de dicionário como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na #conexão'}, escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

#log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na #conexão'}
#
#if log['level'] == 'ERROR':
#    print(log['message'])

#Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha #idade entre 18 e 65 anos e tenha fornecido um email válido. Escreva um programa que valide essas condições e imprima #"Dados de usuário válidos" ou o erro específico encontrado.

#idade = 55
#email = 'usuario@gmail.com'
#
#if not (18 <= idade <= 65):
#    print("Idade de usuário inválida")
#elif not ('@' in email and '.' in email):
#    print("Email de usuário inválido")
#else:
#    print("Dados de usuários válidos")

#Você está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas. Uma transação é #considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois #das 18h). Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.

#transacao = {'valor': 1000, 'hora': 20}
#
#if transacao['valor'] > 12000 or transacao['valor'] > 18 or transacao['valor'] < 9:
#    print("Transação Suspeita")

#Dado um texto, contar quantas vezes cada palavra única aparece nele.

#texto = "a raposa marrom salta sobre o cachorro preguiçoso raposa"
#palavras = texto.split()
#contagem = {}
#
#for palavra in palavras:
#    if palavra in contagem:
#        contagem[palavra] += 1
#    else:
#        contagem[palavra] = 1
#
#print(contagem)

# Normalizar uma lista de números para que fiquem na escala de 0 a 1.

#numeros = [10, 20, 30, 40, 50]
#numeros.sort()
#minimo = min(numeros)
#maximo = max(numeros)
#normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]
#
#print(normalizados)

# Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.

#usuarios = [
#    {"nome": "Alice", "email": "alice@example.com"},
#    {"nome": "Bob", "email": ""},
#    {"nome": "Carol", "email": "carol@example.com"}
#]
#
#for users in usuarios:
#    for info in users:
#        if users[info] == "":
#            print("Usuário: ", users["nome"])

# Dada uma lista de números, extrair apenas aqueles que são pares.

#numeros = range(1, 11)
#pares = []
#
#for i in numeros:
#    if i % 2 == 0:
#        pares.append(i)
#print(pares)

# Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

#vendas = [
#    {"categoria": "eletrônicos", "valor": 1200},
#    {"categoria": "livros", "valor": 200},
#    {"categoria": "eletrônicos", "valor": 800}
#]
#
#agregado = {}
#for venda in vendas:
#    category = venda["categoria"]
#    total = venda["valor"]
#    if category in agregado:
#        agregado[category] += total
#    else:
#        agregado[category] = total
#print(agregado)

# Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

#dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#index = 0
#entrada = ""
#while entrada.lower() != "sair":
#    print(dados[index])
#    entrada = input("Qual a entrada? ")
#    print("A entrada é: ", entrada)
#    index += 1

# Objetivo: Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

#a = int(input("Digite um número entre 1 e 10: "))
#b = [1, 10]
#
#while not (b[0] <= a <= b[1]):
#    a = int(input("Digite um número entre 1 e 10: "))
#print(f"Esse é o número escolhido: {a}")

# Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

#pagina_atual = 1
#numero_de_paginas = 10
#
#while pagina_atual <= numero_de_paginas:
#    print(f"Processando páginas. Página {pagina_atual} de {numero_de_paginas}")
#    # Código de processamento aqui
#    pagina_atual += 1
#print("Processamento Concluído")

# Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

#tentativa = 1
#numero_maximo = 10
#
#while tentativa <= numero_maximo:
#    print(f"Tentativa {tentativa}, tentando reconectar-se.")
#    # código de reconexão
#    reconexao = False
#    if reconexao:
#        print("Conexão bem-sucedida!")
#    tentativa += 1
#print("Time Out.")

# Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada.

#itens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#valor_procurado = 7
#index = 0
#
#while itens[index] != valor_procurado:
#    print(itens[index], " não é o valor esperado. Continuando a busca.")
#    index += 1
#print("O valor ", itens[index], " foi encontrado na lista!")
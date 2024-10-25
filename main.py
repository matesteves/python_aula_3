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
import pandas as pd
from twilio.rest import Client

#*******************parte comentada pois nao vou fazer cadastro******************
# Your Account SID from twilio.com/console
#account_sid = "AC2628af3ef76cd40c0089afb9bfa8d7bf"
# Your Auth Token from twilio.com/console
#auth_token  = "efcf79aafdb10f0a995188d8825be60d"
#client = Client(account_sid, auth_token)
#*******************parte comentada pois nao vou fazer cadastro******************



# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:

    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    if (tabela_vendas['Vendas'] > 55000).any():
        
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')

#*******************parte comentada pois nao vou fazer cadastro******************
       # message = client.messages.create(
            #to="+5521972795556",
            #from_="+16093364135",
            #body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        #print(message.sid)
#*******************parte comentada pois nao vou fazer cadastro******************




# nao fazer a parte de envio de mensagem pois deve cadastra em uma site nao confiavel         

# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior do que 55.000 não quero fazer nada
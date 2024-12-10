import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


#Importar base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

#Vizualizar Base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

print('-' * 50)
#Faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

print('-' * 50)
#Quantidade de produtos vendiidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)

print('-' * 50)
#Ticket médio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
print(ticket_medio)

print('-' * 50)

# Configuração do e-mail
smtp_host = 'smtp.gmail.com'
smtp_port = 587
email_user = 'SEUEMAIL@gmail.com'  # Seu e-mail
email_pass = 'SUASENHA'  # Senha de aplicativo do Gmail
email_destino = 'EMAILDESTINATARIO' # Destino que deseja enviar esse email

# Criar o e-mail
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_destino
msg['Subject'] = 'Relatório de vendas por loja'

# Conteúdo do e-mail
corpo_email = f"""
Prezados,

Segue o Relatório de vendas por cada loja:

<b>Faturamento:</b><br>
{faturamento.to_html()}<br><br>

<b>Quantidade Vendida:</b><br>
{quantidade.to_html()}<br><br>

<b>Ticket Médio:</b><br>
{ticket_medio.to_html()}<br><br>

Qualquer dúvida, estou à disposição.

Atte.,<br>
Seu Nome meu caro amigo(a)
"""
msg.attach(MIMEText(corpo_email, 'html'))

# Enviar o e-mail
try:
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(email_user, email_pass)
    server.sendmail(email_user, email_destino, msg.as_string())
    server.quit()
    print("E-mail enviado com sucesso!")
except Exception as e:
    print("Erro ao enviar o e-mail:", e)
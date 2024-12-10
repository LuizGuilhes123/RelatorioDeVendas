# 📊 Relatório de Vendas por Loja
Bem-vindo ao Relatório de Vendas por Loja, um projeto em Python que utiliza pandas para análise de dados e gera relatórios detalhados sobre o desempenho de vendas em diferentes lojas. Além disso, ele envia esses relatórios diretamente para seu e-mail usando o Gmail! 🚀

## 🛠️ Funcionalidades do Projeto
Análise de Dados:

Calcula o faturamento total de cada loja.
Avalia a quantidade total de produtos vendidos por loja.
Determina o ticket médio de vendas por produto em cada loja.
Envio de Relatórios por E-mail:

Automatiza o envio do relatório em formato estruturado via Gmail.
Organização e Eficiência:

Processa grandes volumes de dados de forma rápida e organizada.
Ideal para gestores e analistas que buscam insights detalhados sobre o desempenho de suas lojas.

## 📝 Pré-requisitos
Certifique-se de ter as seguintes dependências instaladas antes de executar o projeto:

Python 3.7 ou superior

Pandas

OpenPyXL

smtplib

email

## 🚀 Configuração do Projeto
Pré-requisitos
Certifique-se de ter as seguintes ferramentas instaladas:

Python 3.7 ou superior
Pip (gerenciador de pacotes do Python)

## Clone o Repositório:

```git clone https://github.com/LuizGuilhes123/RelatorioDeVendas.git```

## Use o comando abaixo para instalar os pacotes necessários:

```pip install pandas openpyxl```

## Configure o Envio de E-mail

1.Ative a autenticação em duas etapas no Gmail e crie uma senha de aplicativo.
2.No arquivo App.py, configure as variáveis com suas credenciais do Gmail:

```seu_email = "seuemail@gmail.com"```

```senha = "sua_senha_de_aplicativo"```

```destinatario = "destinatario@gmail.com"```

## 🏃 Executando o Projeto
Certifique-se de que o arquivo Vendas.xlsx está no diretório principal do projeto. Em seguida, execute:

```python App.py```

## Resultado
O relatório gerado será impresso no terminal.
Um e-mail será enviado com o conteúdo detalhado.

## 🧩 Funcionalidades
Análise de Dados
Faturamento por Loja: Calcula o total vendido por cada loja.

Quantidade de Produtos Vendidos: Soma de todos os produtos vendidos por loja.

Ticket Médio por Produto: Calcula o ticket médio com base no faturamento e na quantidade vendida.

Envio de Relatórios por E-mail
O sistema automatiza o envio de relatórios com as análises descritas acima diretamente para um endereço de e-mail.


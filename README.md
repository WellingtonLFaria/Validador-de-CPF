# Validador de CPF
Um validador de CPF feito em python.

# Rodar o App na máquina local:
    python app.py

# Integração com Docker

## Instalando Docker
    sudo apt update
    sudo apt install curl -y
    sudo curl -fsSL https://get.docker.com/ | sh

## Criando a imagem
    sudo docker build -t <nome_da_imagem> .

## Criando e rodando o container
    sudo docker run -dp <porta_desejada>:5000 <nome_da_imagem>
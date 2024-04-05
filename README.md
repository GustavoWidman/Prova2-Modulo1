# Prova1-Modulo1 - Ponderada Gustavo Wagon Widman

## Descrição

Este projeto foi desenvolvido a partir da proposta entregue na prova 2 do modulo 1. O projeto consiste em um servidor que armazena logs de acesso a duas rotas, '/ping' e '/echo', e permite ao usuário visualizar o histórico de requisições realizadas através da rota '/dash'.

## Instalação e execução

Para instalar as dependências do projeto, comece clonando o repositório

```bash
git clone https://github.com/GustavoWidman/Prova2-Modulo1.git
```

Depois, entre na pasta do projeto, crie um ambiente virtual (venv) e ative-o.

```bash
cd Prova2-Modulo1 && python -m venv env && source env/bin/activate
```

Finalmente, instale as dependências do projeto com o comando:

```bash
pip install -r requirements.txt
```

Para rodar o projeto, execute:

```bash
python src/main.py
```

## Estrutura do projeto

A estrutura do projeto é composta por pastas e arquivos que organizam os comandos, classes e utilitários. Segue abaixo a estrutura do projeto, resultado do comando `tree --gitignore`

```bash
.
├── README.md
├── requirements.txt
└── src
    ├── database
    │   ├── archives
    │   │   └── logs.json
    │   └── wrapper.py
    ├── main.py
    ├── routes
    │   ├── dash.py
    │   ├── echo.py
    │   ├── info.py
    │   ├── main.py
    │   └── ping.py
    ├── templates
    │   ├── dash.html
    │   └── info.html
    └── utils
        └── logger.py
```

## Rotas

O projeto possui as seguintes rotas:

- `/ping`: Requisição do tipo GET, que retorna um JSON {'resposta': 'pong'};
- `/echo`: Requisição do tipo POST, que retorna um JSON com o seguinte formato - {'resposta': 'o que o usuário enviou'}. Os dados de entrada devem ter o seguinte formato {'dados': 'texto'};
- `/dash`: Rota que permite visualizar o histórico das requisições realizadas (front-end);
- `/info`: Rota que retorna mídia sobre os dados armazenados no banco de dados.

## Dependências

- Flask 3.0.2
- TinyDB 4.8.0

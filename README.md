# Projeto semnome-ltda

Este é um projeto de aplicativo web desenvolvido em Python utilizando o framework Flask. O objetivo deste aplicativo é permitir aos usuários calcular o Índice de Massa Corporal (IMC) com base nas informações de nome, peso e altura. Além disso, o sistema realiza a validação do nome para verificar se a informação já foi inserida no banco de dados antes de salvar os dados.

## Funcionalidades

- Formulário web com campos para inserir nome, peso e altura. ✅
- Botão para calcular o IMC com base nos valores inseridos. ✅
- Validação do nome para evitar duplicações no banco de dados.
- Botão para salvar os dados do cálculo do IMC no banco de dados. ✅

## Tecnologias Utilizadas

- Python
- Flask
- PostgreSQL (Banco de dados)
- HTML e CSS (para a interface do usuário)

## Pré-requisitos

Certifique-se de ter as seguintes tecnologias instaladas em sua máquina antes de executar o aplicativo:

- Python (https://www.python.org/)
- Flask (https://flask.palletsprojects.com/en/2.1.x/)
- PostgreSQL (https://www.postgresql.org/)

## Configuração do Ambiente

1. Clone o repositório do projeto:

   ```bash
   git clone https://github.com/seunome/seuprojeto.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd semnome-ltda
   ```

3. Crie e ative um ambiente virtual (recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

4. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

## Executando o Aplicativo

1. Após configurar o ambiente, você pode iniciar o aplicativo Flask:

   ```bash
   python app.py
   ```

2. Acesse o aplicativo em seu navegador em [http://localhost:5000](http://localhost:5000).

## Uso do Aplicativo

1. Preencha o formulário com o nome, peso e altura.
2. Clique no botão "Calcular IMC" para calcular o Índice de Massa Corporal.
3. O sistema verificará se o nome já existe no banco de dados antes de salvar os dados.
4. Se o nome for único, você pode clicar no botão "Salvar" para armazenar os dados no banco de dados.

## Contribuindo

Sinta-se à vontade para contribuir para este projeto. Você pode enviar problemas, sugestões ou até mesmo solicitar solicitações de pull.

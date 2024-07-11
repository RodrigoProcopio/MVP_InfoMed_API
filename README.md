# InfoMed (API Flask)

InfoMed é uma aplicação destinada a cuidadores de idosos, pessoas que necessitam de cuidados médicos frequentes ou que desejam gerenciar seus medicamentos e consultas médicas de maneira eficiente. A aplicação permite adicionar, remover e editar medicamentos, além de gerenciar a agenda de consultas médicas, com a capacidade de sincronizar essas informações com o Google Calendar.

## Funcionalidades

### Gerenciamento de Medicamentos:

- Visualizar, adicionar, remover e editar medicamentos.
- Inserir posologia, nome do médico e especialidade.

### Gerenciamento de Consultas Médicas:

- Visualizar, adicionar, remover e editar consultas médicas.
- Inserir nome do médico, especialidade, data e hora da consulta.

## API Flask

A API Flask associada a este projeto facilita o gerenciamento e a manipulação de dados relacionados aos medicamentos e consultas médicas.

## Requisitos

Após clonar o repositório, navegue até o diretório raiz pelo terminal e certifique-se de ter todas as bibliotecas Python listadas no arquivo `requirements.txt` instaladas. Para instalar as dependências, execute o seguinte comando:

```bash
pip install -r requirements.txt
```

## Como Usar

Para utilizar esta API, siga os passos abaixo:

1. Inicie a aplicação Flask:

   ```bash
   flask run --host 0.0.0.0 --port 5000
   ```

2. Acesse a documentação Swagger para obter detalhes sobre as rotas e os parâmetros necessários.

3. Utilize as rotas para adicionar, visualizar ou remover medicamentos e consultas.

## Utilizando o Docker

Para utilizar a API Flask com Docker, siga os passos abaixo:

1. Certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

2. Navegue até o diretório onde está localizado o arquivo `dockerfile` do projeto.

3. Construa e inicie os containers com o seguinte comando:

   ```bash
   docker-compose up --build
   ```

## Documentação Swagger

Para explorar a documentação completa da API no estilo Swagger, visite: [http://localhost:5000/openapi/swagger#/](http://localhost:5000/openapi/swagger#/)

## Rotas da API
### Consultas Médicas:
- [POST] `/add_consulta`
  
  Adiciona uma nova consulta à base de dados.

  - **Entrada**: Um objeto JSON com os dados da consulta.
  - **Saída**: Representação das consultas cadastradas.

- [PUT] `/update_consulta`
  
  Retorna uma listagem de todas as consultas cadastradas.

- [GET] `/get_consultas`
  
  Retorna informações de uma consulta com base em seu nome.

- [DELETE] `/del_consulta_id`
  
  Remove uma consulta com base em seu nome.

### Medicamentos:
- [POST] `/medicamento`

  Adiciona um novo medicamento à base de dados.

- [GET] `/medicamentos`

  Retorna uma listagem de todos os medicamentos cadastrados.

- [GET] `/medicamento`

  Retorna informações de um medicamento com base em seu nome.

- [DELETE] `/medicamento`

  Remove um medicamento com base em seu nome.

- [DELETE] `/medicamento_id`

  Remove um medicamento com base em seu Id.

## Notas de Versão

### Versão 1.0.0 (julho de 2024)

- Implementação inicial da API.
- Funcionalidades de adicionar, visualizar e remover medicamentos e consultas médicas.

## Autor

Este projeto foi desenvolvido por Rodrigo Procópio e pode ser encontrado no [GitHub](https://github.com/RodrigoProcopio).

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](https://github.com/RodrigoProcopio/MVP_InfoMed_API/blob/main/LICENSE.md) para obter detalhes.

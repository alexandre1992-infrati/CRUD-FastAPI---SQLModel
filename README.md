# CRUD FastAPI com SQLModel

Este projeto é uma API RESTful simples para gerenciamento de alunos (CRUD) usando FastAPI e SQLModel, com banco de dados PostgreSQL assíncrono.

## Tecnologias Utilizadas

- **FastAPI**: Framework web assíncrono para construção de APIs.
- **SQLModel**: Biblioteca para modelos de dados SQL com Pydantic.
- **SQLAlchemy**: ORM para interação com o banco de dados.
- **AsyncPG**: Driver assíncrono para PostgreSQL.
- **Uvicorn**: Servidor ASGI para execução da aplicação.
- **Pydantic Settings**: Para gerenciamento de configurações.

## Pré-requisitos

- Python 3.8+
- PostgreSQL rodando localmente (porta 5432)
- Banco de dados "escola" criado no PostgreSQL

## Instalação

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd crud_fastapi_sqlmodel
   ```

2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados PostgreSQL com usuário "postgres" e senha "postgres", ou ajuste em `core/configs.py`.

## Execução

1. Crie as tabelas no banco:
   ```bash
   python create_table.py
   ```

2. Execute a aplicação:
   ```bash
   python main.py
   ```

A API estará disponível em `http://localhost:8080`.

## Estrutura do Projeto

```
crud_fastapi_sqlmodel/
├── main.py                 # Aplicação principal FastAPI
├── create_table.py         # Script para criação das tabelas
├── requirements.txt         # Dependências Python
├── api/
│   └── v1/
│       ├── api.py          # Router principal da API v1
│       └── endpoints/
│           └── student.py  # Endpoints para alunos
├── core/
│   ├── configs.py          # Configurações da aplicação
│   ├── database.py         # Configuração do banco de dados
│   └── dependency.py       # Dependências (session)
└── models/
    ├── __all_models.py     # Importação de todos os modelos
    └── schooll.py          # Modelo SchoolModel (alunos)
```

## Endpoints da API

### Base URL: `http://localhost:8080/api/v1`

#### Criar Aluno
- **POST** `/school/`
- **Corpo (JSON)**:
  ```json
  {
    "name": "João Silva",
    "age": 15,
    "grade": "9º ano",
    "note": 8.5
  }
  ```
- **Resposta**: Dados do aluno criado.

#### Listar Alunos
- **GET** `/school/`
- **Resposta**: Lista de todos os alunos.

#### Obter Aluno por ID
- **GET** `/school/{student_id}`
- **Parâmetros**: `student_id` (inteiro)
- **Resposta**: Dados do aluno específico ou 404 se não encontrado.

## Modelo de Dados

### SchoolModel
- `student_id`: int (chave primária, auto-incremento)
- `name`: str (nome do aluno)
- `age`: int (idade)
- `grade`: str (série/ano)
- `note`: float (nota)

## Como Usar

1. Inicie o servidor.
2. Use ferramentas como Postman, curl ou a documentação automática do FastAPI em `http://localhost:8080/docs` para testar os endpoints.
3. Exemplo com curl:
   ```bash
   # Criar aluno
   curl -X POST "http://localhost:8080/api/v1/school/" \
        -H "Content-Type: application/json" \
        -d '{"name":"Maria Santos","age":16,"grade":"10º ano","note":9.2}'

   # Listar alunos
   curl "http://localhost:8080/api/v1/school/"

   # Obter aluno por ID
   curl "http://localhost:8080/api/v1/school/1"
   ```

## Documentação Automática

Acesse `http://localhost:8080/docs` para a documentação interativa gerada pelo FastAPI (Swagger UI).

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades.
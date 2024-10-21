## Languages: pt-Br & en-US.


# User Registration System

This is a simple user registration system implemented in Python using SQLite for database management and Colorama for colored terminal output. The system allows you to register, list, update, and delete users.

## Features

- Register a new user
- List all registered users
- Update user information
- Delete a user
- Input validation for name, email, and age
- Colored terminal output for better user experience

## Requirements

- Python 3.x
- SQLite3
- Colorama

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/user-registration-system.git
    cd user-registration-system
    ```

2. Install the required packages:

    ```sh
    pip install colorama
    ```

## Usage

1. Run the script:

    ```sh
    python app.py
    ```

2. Follow the on-screen instructions to interact with the system.

## Code Overview

### `app.py`

This is the main script that contains the `UserRegister` class and the `main` function.

#### `UserRegister` Class

- `__init__`: Initializes the database connection.
- `conect_db`: Connects to the database.
- `desconect_db`: Disconnects from the database.
- `create_table`: Creates the `users` table if it doesn't exist.
- `insert_user`: Inserts a new user into the database.
- `list_users`: Lists all registered users.
- `delete_user`: Deletes a user by ID.
- `update_user`: Updates user information by ID.
- `user_exists`: Checks if a user with the same name or email already exists.

#### Helper Functions

- `print_title`: Prints the title of the application.
- `validate_name`: Validates the user's name.
- `validate_age`: Validates the user's age.
- `validate_email`: Validates the user's email.

#### `main` Function

The main function that provides a menu for the user to interact with the system.

## Example

```sh
1 - Register User
2 - List Users
3 - Delete User
4 - Update User
5 - Exit
Choose an option: 1

Register User

Name: John Doe
Email: john.doe@example.com
Age: 30
User registered successfully!
```

### License

This project is licensed under the MIT License. See the LICENSE file for details.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### Acknowledgements
- `Colorama` for colored terminal output.
- `SQLite` for the database management.


--------------------------------------------------------------------------------------------------------

--------------------------------------------------------------------------------------------------------


# Sistema de Registro de Usuários

Este é um sistema simples de registro de usuários implementado em Python usando SQLite para gerenciamento de banco de dados e Colorama para saída colorida no terminal. O sistema permite que você registre, liste, atualize e exclua usuários.

## Funcionalidades

- Registrar um novo usuário
- Listar todos os usuários registrados
- Atualizar informações do usuário
- Excluir um usuário
- Validação de entrada para nome, email e idade
- Saída colorida no terminal para uma melhor experiência do usuário

## Requisitos

- Python 3.x
- SQLite3
- Colorama

## Instalação

1. Clone o repositório:

    ```sh
    git clone https://github.com/seuusuario/sistema-registro-usuarios.git
    cd sistema-registro-usuarios
    ```

2. Instale os pacotes necessários:

    ```sh
    pip install colorama
    ```

## Uso

1. Execute o script:

    ```sh
    python app.py
    ```

2. Siga as instruções na tela para interagir com o sistema.

## Visão Geral do Código

### `app.py`

Este é o script principal que contém a classe `UserRegister` e a função `main`.

#### Classe `UserRegister`

- `__init__`: Inicializa a conexão com o banco de dados.
- `conect_db`: Conecta ao banco de dados.
- `desconect_db`: Desconecta do banco de dados.
- `create_table`: Cria a tabela `users` se ela não existir.
- `insert_user`: Insere um novo usuário no banco de dados.
- `list_users`: Lista todos os usuários registrados.
- `delete_user`: Exclui um usuário pelo ID.
- `update_user`: Atualiza as informações do usuário pelo ID.
- `user_exists`: Verifica se um usuário com o mesmo nome ou email já existe.

#### Funções Auxiliares

- `print_title`: Imprime o título da aplicação.
- `validate_name`: Valida o nome do usuário.
- `validate_age`: Valida a idade do usuário.
- `validate_email`: Valida o email do usuário.

#### Função `main`

A função principal que fornece um menu para o usuário interagir com o sistema.

## Exemplo

```sh
1 - Registrar Usuário
2 - Listar Usuários
3 - Excluir Usuário
4 - Atualizar Usuário
5 - Sair
Escolha uma opção: 1

Registrar Usuário

Nome: João Silva
Email: joao.silva@exemplo.com
Idade: 30
Usuário registrado com sucesso!
```

### Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

### Contribuindo

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request para quaisquer melhorias ou correções de bugs.

### Agradecimentos

- `Colorama` pela saída colorida no terminal.
- `SQLite` pelo gerenciamento do banco de dados.
# Personal Journal API

API RESTful para um diário pessoal, desenvolvida com Django e Django REST Framework (DRF), utilizando autenticação JWT (JSON Web Tokens). O projeto inclui permissões de acesso, suporte a HATEOAS e proteção de rotas.

## Instalação e Execução

### 1. Acessar o Repositório
Navegue até a pasta do projeto:
```bash
cd api-jwt
```

### 2. Ativar o Ambiente Virtual e Instalar Dependências
```bash
source venv/bin/activate

pip install django djangorestframework djangorestframework-simplejwt
```

### 3. Rodar as Migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Iniciar o Servidor
```bash
python manage.py runserver
```
O servidor estará disponível em `http://127.0.0.1:8000/`.

---

## Autenticação (JWT)

A maioria dos endpoints requer autenticação. O token de acesso deve ser enviado no cabeçalho HTTP:
`Authorization: Bearer <access_token>`

### Criar Usuário (Registro)
- **Rota:** `POST /api/auth/register/`
- **Acesso:** Público (AllowAny)
- **Body (JSON):**
  ```json
  {
      "username": "joao",
      "email": "joao@email.com",
      "password": "senha_segura123"
  }
  ```

### Fazer Login
- **Rota:** `POST /api/auth/login/`
- **Acesso:** Público (AllowAny)
- **Body (JSON):**
  ```json
  {
      "username": "joao",
      "password": "senha_segura123"
  }
  ```
- **Retorno:** Retorna os tokens `access` e `refresh`. Utilize o token `access` no cabeçalho `Authorization` nas requisições subsequentes.

### Renovar Token de Acesso
- **Rota:** `POST /api/auth/refresh/`
- **Body:** `{ "refresh": "<refresh_token>" }`

### Logout (Blacklist do Token)
- **Rota:** `POST /api/auth/logout/`
- **Acesso:** Protegido (IsAuthenticated)
- **Body:** `{ "refresh": "<refresh_token>" }`

### Obter Dados do Usuário Logado
- **Rota:** `GET /api/me/`
- **Acesso:** Protegido (IsAuthenticated)

---

## Diário (Journal)

### Listar Diários Públicos
- **Rota:** `GET /api/journal/public/`
- **Acesso:** Público (AllowAny)
- **Descrição:** Retorna os diários onde o campo `is_public` é igual a `true`.

### Criar Entrada no Diário
- **Rota:** `POST /api/entries/`
- **Acesso:** Protegido (IsAuthenticated)
- **Body (JSON):**
  ```json
  {
      "title": "Registro inicial",
      "content": "Conteúdo do diário.",
      "mood": "happy",
      "is_public": false
  }
  ```
  *(Opções para `mood`: `happy`, `neutral`, `sad`)*.

### Listar Entradas
- **Rota:** `GET /api/entries/`
- **Acesso:** Protegido (IsAuthenticated)
- **Descrição:** Retorna as anotações do usuário autenticado. Membros do grupo `Editor` possuem permissão para listar as entradas de todos os usuários.

### Atualizar, Visualizar ou Deletar Entrada
- **Rota:** `GET`, `PUT`, `PATCH` ou `DELETE /api/entries/<id>/`
- **Acesso:** Protegido (IsAuthenticated e dono da entrada)
- **Descrição:** Permite interação apenas com os itens de autoria do usuário requisitante. A resposta inclui links HATEOAS no campo `links` indicando as operações suportadas.

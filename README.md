# Projeto-AcervosLiterarios
Plataforma de Gestão de Livros Pessoais Aplicação web desenvolvida para modernizar, agilizar e organizar o fluxo de empréstimos de acervos literários particulares de docentes no ambiente escolar. 


```markdown
##  Como Executar o Projeto Localmente

Siga o passo a passo abaixo para clonar, configurar e rodar a aplicação na sua máquina.

### Pré-requisitos
Antes de começar, certifique-se de ter instalado em sua máquina:
* [Python 3.10+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)

---

### 1. Clonar o repositório
Abra o terminal e execute o comando abaixo para baixar o projeto:
```bash
git clone https://github.com/JacksonDev-BR/Projeto-AcervosLiterarios.git
cd Projeto-AcervosLiterarios

```

### 2. Criar e ativar o Ambiente Virtual (`venv`)

É recomendável isolar as dependências do projeto utilizando um ambiente virtual:

**No Windows:**

```bash
python -m venv venv
venv\Scripts\activate

```

**No Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate

```

*(Você saberá que deu certo quando aparecer `(venv)` no início da linha do seu terminal).*

### 3. Instalar as dependências

Com o ambiente virtual ativo, instale o Django e as demais bibliotecas necessárias:

```bash
pip install -r requirements.txt

```

### 4. Configurar as Variáveis de Ambiente (`.env`)

Na raiz do projeto (ao lado do arquivo `manage.py`), crie um arquivo chamado `.env` e adicione a chave secreta do Django:
Markdown

Gere uma chave secreta segura executando o comando abaixo no terminal (com a `venv` ativa):
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

Em seguida, crie um arquivo chamado .env na raiz do projeto (ao lado do arquivo manage.py) e cole a chave gerada:

Snippet de código
SECRET_KEY=cole-aqui-a-chave-gerada-no-terminal
DEBUG=True
```

### 5. Executar as Migrações do Banco de Dados

Crie as tabelas iniciais do SQLite executando:

```bash
python manage.py migrate

```

*(Opcional)* Caso queira acessar o painel administrativo (`/admin`), crie um superusuário:

```bash
python manage.py createsuperuser

```

### 6. Iniciar o Servidor

Agora basta rodar o servidor de desenvolvimento do Django:

```bash
python manage.py runserver

```

Acesse no seu navegador: **[http://127.0.0.1:8000/](https://www.google.com/search?q=http://127.0.0.1:8000/)**

```

---

### 💡 Dica importante antes de subir para o GitHub:
Certifique-se de rodar o comando `pip freeze > requirements.txt` no seu terminal (com a `venv` ativa) antes de fazer o `git push`, para garantir que todas as bibliotecas que você instalou estejam listadas lá dentro.

```

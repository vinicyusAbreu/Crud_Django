
# 📋 Crud simples feito em Django

## 🤔 Sobre o projeto

Um simples aplicativo da web de gerenciamento de tarefas utilizando as operações do CRUD (Criar, Ler, Atualizar, Excluir) usando Django.

## ✨ Demonstração    
Veja abaixo um gif do projeto.</br>
[![Image from Gyazo](https://i.gyazo.com/c53ab20fc636f9e90ef8cc93f3b681eb.gif)](https://gyazo.com/c53ab20fc636f9e90ef8cc93f3b681eb)

## Iniciar projeto


Depois de clonar o repositório, você deseja criar um ambiente virtual, para ter uma instalação limpa do Python. Você pode fazer isso executando o comando

```
python -m venv env
```
Depois disso, é necessário ativar o ambiente virtual.

Você pode instalar todas as dependências necessárias executando
```
pip install -r requirements.txt
```

Definir banco de dados (verifique se você está no mesmo diretório que o manage.py)
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Criar o SuperUser 
```
python manage.py createsuperuser
```

Após todas essas etapas, você pode começar a testar este projeto usando o comando.
```
python manage.py runserver
```

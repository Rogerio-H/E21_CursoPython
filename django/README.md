###Django

Anotações referente ao Django

1. Subdiretorio django 
2.Virtual enviroment python -m venv venv
3.adicionar ao repositorio git
4. pip freeze
5. pip install django


Projeto --> 
    app1    
    app2
    app3
    app4


# como criar o projeto
django-admin startproject proj .
## não esquecer do ponto no final

# Como criar o app

django-admin startapp app1

### Testar
python manage.py runserver

### Deploy da aplicação web para o heroku.com


### Aula 22/08

Settings.py --> aponto qual ENGINE

python manage.py makemigrations --> prepara scripts para trabalhar com qualquer ENGINE

python manage.py showmigrations --> Mostra migrações preparadas efetivadas ou não.

ENGINES: posrgreSQL, SQLite, MySQL, MongoDB

MVT = Models Views Templates

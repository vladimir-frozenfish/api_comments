# api_final
api final

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/.../
```

```
cd ...
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## URLS проекта:
### авторизация:
/api/v1/users/ - регистрация нового пользователя
/api/v1/users/me/ - получить/обновить текущего пользователя
/api/v1/jwt/create/ - создать JWT-токен
/api/v1/jwt/refresh/ - обновить JWT-токен



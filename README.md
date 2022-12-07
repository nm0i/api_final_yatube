Описание
========

Имплементация  API  для  проекта  социальной сети  Yatube,  в  котором
имплементированы  некоторые   основные  функции  как  то   создание  и
получение записей, подписка на авторов.

Зависимости
===========

Используются python3, Django 2.2. Основные зависимости прописаны в
requirements.txt, но для установки нужны [python3.8](python.org) и
[direnv](https://direnv.net/)

Установка
=========

    git clone https://github.com/nm0i/api_final_yatube.git api_final_yatube
    cd api_final_yatube

    echo 'layout_python3' > .envrc
    direnv allow

    python3.8 -m pip install -r requirements.txt

    cd yatube_api
    python3.8 manage.py migrate

    python3.8 manage.py runserver

[45](123)

Примеры
=======

Получении публикации:

    GET http://127.0.0.1:8000/api/v1/posts/

Ответ, 200:
    {
      "count": 123,
      "next": "http://api.example.org/accounts/?offset=400&limit=100",
      "previous": "http://api.example.org/accounts/?offset=200&limit=100",
      "results": [
        {
          "id": 0,
          "author": "string",
          "text": "string",
          "pub_date": "2021-10-14T20:41:29.648Z",
          "image": "string",
          "group": 0
        }
      ]
    }

Удаление публикации:

    DELETE http://127.0.0.1:8000/api/v1/posts/{id}/

Ответ, 401

    {
      "detail": "Учетные данные не были предоставлены."
    }

Ответ, 403

    {
      "detail": "У вас недостаточно прав для выполнения данного действия."
    }

Ответ, 404

    {
      "detail": "Страница не найдена."
    }

Обновление коментария:

    PUT http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/

    {
      "text": "string"
    }

Ответ, 200:

    {
      "id": 0,
      "author": "string",
      "text": "string",
      "created": "2019-08-24T14:15:22Z",
      "post": 0
    }

Ответ, 403:

    {
      "detail": "У вас недостаточно прав для выполнения данного действия."
    }

Более примеров на http://127.0.0.1:8000/redoc/

Автор
=====

Элмер Ефлов

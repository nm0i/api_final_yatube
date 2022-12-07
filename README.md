# Описание #

Имплементация API для проекта Yatube

# Установка #

Нужны python3.8 и direnv

    git clone URL api_final_yatube
    cd api_final_yatube

    echo 'layout_python3' > .envrc
    direnv allow

    python3.8 -m pip install -r requirements.txt

    cd yatube_api
    python3.8 manage.py migrate

    python3.8 manage.py runserver

# Примеры #

С.м. http://127.0.0.1:8000/redoc/

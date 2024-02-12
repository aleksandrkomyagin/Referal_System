<div align=center>
  
  # [Referal_System](https://github.com/aleksandrkomyagin/Referal_System) <br> (Реализация тестового задания) <br>
  
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
  ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

  ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
  ![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)


</div>


## Описание:
Необходимо разработать простой RESTful API сервис для реферальной системы.

## Функциональные требования:
регистрация и аутентификация пользователя (JWT, Oauth 2.0);
аутентифицированный пользователь должен иметь возможность создать или удалить свой реферальный код. Одновременно может быть активен только 1 код. При создании кода обязательно должен быть задан его срок годности;
возможность получения реферального кода по email адресу реферера;
возможность регистрации по реферальному коду в качестве реферала;	
получение информации о рефералах по id реферера;
UI документация (Swagger/ReDoc).

## Опциональные задачи:
использование clearbit.com/platform/enrichment для получения дополнительной информации о пользователе при регистрации;
использование emailhunter.co для проверки указанного email адреса;
кеширование реферальных кодов с использованием in-memory БД. 
Readme.md файл с описанием проекта и инструкциями по запуску и тестированию

## Стек:
использование любого современного веб фреймворка;
использование СУБД и миграций (Sqlite, PostgreSQL, MySQL);
размещение проекта на GitHub;

## Требования к проекту:
чистота и читаемость кода;
все I/O bound операции должны быть асинхронными;
проект должен быть хорошо структурирован.
проект должен быть простым в деплое, обеспечивать обработку нестандартных ситуаций, быть устойчивой к неправильным действиям пользователя и т.д.



## Описание проекта


Referal_System - REST API проект на DRF, в котором представлена реферальная система, с возможностью активации инвайт-кода, как при регистрации, так и после нее.

## Пользовательские роли и права доступа

* **Аноним** — доступен эндпоинт регистрации.
* **Аутентифицированный пользователь** — доступны эндпоинты `users/{user_id}/`, `users/invite_code/`, `users/get_invite_code_by_email/`, `users/activate_invite_code/` и `auth/refresh_token/`с помощью которых пользователь может получать список рефералов, создавать, удалять свой инвайт код, получать инвайт код по email другого пользователя, активировать инвайт код от других пользователей и обновлять токен соответственно.

## Алгоритм регистрации нового пользователя

* Пользователь отправляет POST-запрос на добавление нового пользователя на эндпоинт `/api/v1/auth/signup/`. В запросе можно указать атрибут "code_by_inviter" и в БД появится появится связь реферер-реферал. 
* При успешной регистрации пользователь получит токен доступа.
  

## Алгоритм активации инвайт кода

* Пользователь может запросить инвайт-код, указав в POST-запросе email реферера.
* Предварительно авторизовавшись, пользователь отправляет POST-запрос с кодом к эндпоинту `/api/v1/users/activate_invite_code/`.
* В случае валидности предоставленного кода создаётся связь в БД между текущим пользователем и ползователем, предоставившим код.

<details>
  <summary>
    <h2>Запуск проекта на локальном сервере</h2>
  </summary>



> Для MacOs и Linux вместо python использовать python3
> Для запуска проекта на Windows потребуется установить вирутальную машину для запуска Redis.

1. Клонировать репозиторий.
   ```
   $ git@github.com:aleksandrkomyagin/Referal_System.git
   ```
2. Cоздать и активировать виртуальное окружение, установить зависимости:
   - **pip**

     ```
      $ python -m venv venv
     ```
    
    Для Windows:
    ```
      $ source venv/Scripts/activate
    ```
    Для MacOs/Linux:
    ```
      $ source venv/bin/activate
    ```

    ```
    (venv) $ cd backend
    (venv) $ python -m pip install --upgrade pip
    (venv) $ pip install -r requirements.txt
    ```
    - **poetry**
    ```
    (venv) $ cd backend
    poetry install
    ```
  
5. Создать файл .env в корневой папке проекта и заполнить файл по шаблону. Для успешного подключения к Redis параметру DEV должен быть в значении True. Если нужно запустить кол с БД postgres, установить значение параметра DB_ENGINE_POSTGRES в True.
 
    ```
    POSTGRES_USER = логин для подключения к базе данных
    POSTGRES_PASSWORD = пароль для подключения к БД
    DB_HOST = название сервиса (контейнера)
    DB_PORT = порт для подключения к БД
    POSTGRES_DB = имя базы данных
    DB_ENGINE_POSTGRES = ДБ Postgres (True/False)
    DEBUG=True
    DEV = режим разработки (True/False)
    ```

6. Выполнить миграции:
    ```
    (venv) $ python manage.py migrate
    ```

7. Запустить сервер:
    ```
    (venv) $ python manage.py runserver
    ```

> После выполнения вышеперечисленных инструкций бэкенд проекта будет доступен по адресу http://127.0.0.1:8000/

> Подробная документация API доступна после запуска сервера по адресу http://127.0.0.1:8000/api/v1/schema/docs/

</details>

<details>
  <summary>
    <h2> Запуск проекта в контейнере. </h2>
  </summary>

1. В файле .env закомментируйте две строки: DB_HOST и DB_PORT. Параметр DEV установите в значение False.

2. Из каталога gateway выполните команду:
    ```
    (venv) $ docker-compose up --build
    ```
</details>


---
<div align=center>

## Контакты

[![Telegram Badge](https://img.shields.io/badge/-aleksandrkomyagin8-blue?style=social&logo=telegram&link=https://t.me/aleksandrkomyagin8)](https://t.me/aleksandrkomyagin8) [![Gmail Badge](https://img.shields.io/badge/-aleksandrkomyagin8@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:aleksandrkomyagin8@gmail.com)](mailto:aleksandrkomyagin8@gmail.com)

</div>

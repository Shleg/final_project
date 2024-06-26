# Руководство по развёртыванию проекта "Сайт рецептов" на PythonAnywhere

Это руководство поможет вам развернуть ваш проект на PythonAnywhere. Следуйте этим шагам для настройки вашего приложения.

## Клонирование репозитория

1. Клонируйте репозиторий на PythonAnywhere:

   *git clone https://github.com/myusername/myproject.git*

2. Дождитесь завершения клонирования.

## Создание виртуального окружения и установка зависимостей

1. Оставаясь в консоли PythonAnywhere, создайте виртуальное окружение и активируйте его:

   *cd myproject*
    *mkvirtualenv --python=/usr/bin/python3.10 virtualenv*

2. Установите необходимые пакеты:

   *pip install -r requirements.txt8

## Создание веб-приложения

1. Перейдите на вкладку Dashboard на PythonAnywhere.
2. Нажмите "Add a new web app".
3. Выберите "Manual configuration (including virtualenvs)".
4. Выберите последнюю доступную версию Python.
5. Следуйте инструкциям на экране.

## Настройка веб-приложения

1. Укажите путь до вашего виртуального окружения в разделе Virtualenv (/home/username/.virtualenvs/virtualenv).
2. Отредактируйте файл WSGI, указав путь к вашему проекту.

## Сохранение "секретов" в окружении

1. Создайте секретный ключ:

  *echo "export SECRET_KEY=ваш_секретный_ключ" >> .env*

2. Добавьте настройки для базы данных MySQL (если требуется):

  *echo "export MYSQL_PASSWORD=dbpassword" >> .env*
3. Обновите приложение.

## Применение миграций к базе данных

1. Запустите консоль PythonAnywhere в виртуальном окружении.

2. Примените миграции:

  *python manage.py migrate*
  
## Раздача статики сервером

1. Соберите статические файлы проекта:

*python manage.py collectstatic*
2. Укажите путь до каталога со статикой в разделе Static files.

## Создание суперпользователя

1. В консоли PythonAnywhere выполните:

  *python manage.py createsuperuser*
2. Введите имя пользователя, адрес электронной почты и пароль.

Перезагрузите сервер.

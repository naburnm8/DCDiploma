Для подгрузки продуктов чтобы посмотреть как они отображаются без необходимости создавать объекты самому выполните следующие действия:

Сначала введите эти две команды (в любом порядке):

1) python -Xutf8 .\manage.py loaddata products/fixtures/categories.json 

2) python -Xutf8 .\manage.py loaddata products/fixtures/shops.json 

Затем введите эту команду:

3) python -Xutf8 .\manage.py loaddata products/fixtures/products.json 

# DOCKER
1) Склонируйте эту ветку.
2) Установите Docker для Вашей ОС. (Я использовал Windows)

**ПРИМЕЧАНИЕ: прежде чем запускать контейнер, поменяйте в settings.py доменное имя на своё.**

3) Находясь в директории с проектом напишите в терминале следующее:
``docker-compose up --build``
4) Не забудьте применить миграции и фикстуры:
`docker-compose exec web python manage.py migrate` `docker-compose exec web [команды из раздела выше]`
5) Вполне вероятно, что сервер не запустился без миграций, запускаем его ещё раз:
`docker-compose up --build`
6) Создайте суперюзера с нашими данными. `docker-compose exec web manage.py createsuperuser`
7) Зайдите в админ-панель и нажмите Save на каждый объект Products. Это необходимо для работы оплаты.


*При запуске пользовался следующей статьёй, если что-то не работает, посмотрите туда, только потом уже ChatGPT:*
[статья](https://betterstack.com/community/guides/scaling-python/dockerize-django/#step-10-deploying-the-django-application-with-docker-compose)

*P.S Вы знаете кто это писал, так что при возникновении проблем, можете обращаться ко мне*


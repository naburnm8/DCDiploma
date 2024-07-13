Для подгрузки продуктов чтобы посмотреть как они отображаются без необходимости создавать объекты самому выполните следующие действия:

Сначала введите эти две команды (в любом порядке):

1) python -Xutf8 .\manage.py loaddata products/fixtures/categories.json 

2) python -Xutf8 .\manage.py loaddata products/fixtures/shops.json 

Затем введите эту команду:

3) python -Xutf8 .\manage.py loaddata products/fixtures/products.json 

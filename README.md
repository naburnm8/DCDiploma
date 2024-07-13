Для подгрузки продуктов чтобы посмотреть как они отображаются без необходимости создавать объекты самому выполните следующие действия:

Сначала введите эти две команды (в любом порядке):
python -Xutf8 .\manage.py loaddata products/fixtures/categories.json 
python -Xutf8 .\manage.py loaddata products/fixtures/shops.json 

Затем введите эту команду:
python -Xutf8 .\manage.py loaddata products/fixtures/products.json 

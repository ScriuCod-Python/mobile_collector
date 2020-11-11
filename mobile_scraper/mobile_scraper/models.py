from peewee import *

db = SqliteDatabase('phones.db')


class Products(Model):
    title = CharField()
    brand = CharField()
    price = IntegerField()
    page_link = CharField()

    class Meta:
        database = db  # This model uses the "people.db" database.

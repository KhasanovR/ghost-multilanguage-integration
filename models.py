from peewee import SqliteDatabase, CharField, IntegerField, Model, ForeignKeyField
from setting import DB_CONNECTION_URL

db = SqliteDatabase(DB_CONNECTION_URL)


class Translation(Model):
    post_id = CharField(primary_key=True)
    post_slug = CharField(unique=True)
    post_lang = CharField()
    o_post = ForeignKeyField('self', related_name='translations', null=True)

    class Meta:
        database = db
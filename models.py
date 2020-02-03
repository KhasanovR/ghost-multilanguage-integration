from peewee import SqliteDatabase, BooleanField, CharField, Model, ForeignKeyField
from setting import DB_CONNECTION_URL

db = SqliteDatabase(DB_CONNECTION_URL)


class Translation(Model):
    post_id = CharField(primary_key=True)
    post_slug = CharField(unique=True)
    post_lang = CharField()
    is_published = BooleanField(default=0)
    o_post = ForeignKeyField('self', related_name='translations', null=True)

    class Meta:
        database = db
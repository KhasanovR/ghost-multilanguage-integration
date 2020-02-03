from peewee import SqliteDatabase, BooleanField, CharField, Model, ForeignKeyField
from setting import DB_CONNECTION_URL

db = SqliteDatabase(DB_CONNECTION_URL)


class Translation(Model):
    post_id = CharField(primary_key=True)
    post_slug = CharField(unique=True)
    post_lang = CharField()
    is_published = BooleanField(default=0)
    o_post = ForeignKeyField('self', related_name='translations', null=True)

    @property
    def serialize(self):
        data = {
            'post_id': str(self.post_id),
            'post_slug': str(self.post_slug),
            'post_lang': str(self.post_lang),
            'is_published': self.is_published,
            'o_post_id': str(self.o_post),
        }

        return data

    def __repr__(self):
        return "{}, {}, {}, {}, {}".format(
            self.post_id,
            self.post_slug,
            self.post_lang,
            self.is_published,
            self.o_post_id
        )

    class Meta:
        database = db
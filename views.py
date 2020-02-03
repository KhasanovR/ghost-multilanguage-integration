from flask import jsonify
from flask import request
import json
from flask import Response
from models import db, Translation
from ghost_admin_api import send_post
from setting import LANGAUGES
from googletrans import Translator

translator = Translator()


def translate_post():
    post = json.loads(request.data)['post']['current']
    src_lang = translator.detect(post['title']).lang
    for tag in post['tags']:
        if tag['visibility'][1:] in LANGAUGES:
            src_lang = tag['visibility'][1:]
    db.connect()
    if Translation.select().where(Translation.post_id == post["id"]):
        print("Not Cool")
        return Response("Not Cool", 200)
    Translation.create(post_id=str(post["id"]), post_slug=str(post["slug"]), post_lang=src_lang, is_published=1,
                       o_post=str(post["id"]))
    translations = send_post(post, src_lang)
    for trans in translations:
        lang = trans['lang']
        trans = trans['data']['posts'][0]
        Translation.create(post_id=str(trans["id"]), post_slug=str(trans["slug"]), is_published=0, post_lang=lang,
                           o_post=str(post["id"]))
    db.commit()
    db.close()
    return Response("Cool", 200)


def get_translations():
    post_id = json.loads(request.data)['id']
    db.connect()
    translation = (Translation.get(Translation.post_id == post_id))
    original_post = translation.o_post
    translations = original_post.translations
    db.close()
    _json = json.dumps({ 'posts' : [i.serialize for i in translations]})
    return Response(_json, 200)

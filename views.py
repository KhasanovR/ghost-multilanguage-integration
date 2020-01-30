from flask import jsonify
from flask import request
import json
from flask import Response
from models import db, Translation
from ghost_admin_api import send_post

def new_post():

    post = json.loads(request.data)['post']['current']
    db.connect()
    if Translation.select().where(Translation.post_id == post["id"]):
        print("Not Cool")
        return Response("Not Cool", 200)
    translations = Translation.create(post_id=str(post["id"]), post_slug=str(post["slug"]), post_lang=str("eng"), o_post=str(post["id"]))
    print(send_post(post))
    db.commit()
    db.close()
    return Response("Cool", 200)

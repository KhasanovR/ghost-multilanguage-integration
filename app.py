from flask import Flask

app = Flask(__name__)

from views import new_post

app.add_url_rule('/newpost', 'publish', methods=['POST'], view_func=new_post)


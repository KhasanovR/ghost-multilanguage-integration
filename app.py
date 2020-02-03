from flask import Flask
from views import translate_post, get_translations


app = Flask(__name__)

app.add_url_rule('/translate_post',  methods=['POST'], view_func=translate_post)
app.add_url_rule('/get_translations', methods=['POST'], view_func=get_translations)

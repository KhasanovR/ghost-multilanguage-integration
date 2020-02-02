from flask import Flask

app = Flask(__name__)
import requests  # pip install requests
import jwt  # pip install pyjwt
from datetime import datetime as date
from setting import GHOST_ADMIN_API_TOKEN
from setting import GHOST_ADMIN_URL
from googletrans import Translator
import re, json

translator = Translator()
# Admin API key goes here
key = GHOST_ADMIN_API_TOKEN

# Split the key into ID and SECRET
id, secret = key.split(':')

# Prepare header and payload
iat = int(date.now().timestamp())

header = {'alg': 'HS256', 'typ': 'JWT', 'kid': id}
payload = {
    'iat': iat,
    'exp': iat + 5 * 60,
    'aud': '/v3/admin/'
}

# Create the token (including decoding secret)
token = jwt.encode(payload, bytes.fromhex(secret), algorithm='HS256', headers=header)

# Make an authenticated request to create a post
url = GHOST_ADMIN_URL + '/posts/'
headers = {'Authorization': 'Ghost {}'.format(token.decode())}


def send_post(post):
    title = ""
    mobiledoc = ''
    feature_image = ''
    custom_excerpt = ''
    if post['title']:
        title = translator.translate(post['title'], src='en', dest='ru').text
    if post['mobiledoc']:
        i = 0
        mobiledoc = json.loads(post['mobiledoc'])
        for p in mobiledoc['sections']:
            j = 0
            for block in p[2]:
                mobiledoc['sections'][i][2][j][3] = translator.translate(block[3], src='en', dest='ru').text
                j = j + 1
            i = i + 1
        mobiledoc = json.dumps(mobiledoc)
    if post['feature_image']:
        feature_image = post['feature_image']
    if post['custom_excerpt']:
        custom_excerpt = translator.translate(post['custom_excerpt'], src='en', dest='ru').text
    status = 'draft'
    body = {'posts': [
        {'title': title,
         'mobiledoc': mobiledoc,
         'feature_image': feature_image,
         'custom_excerpt':  custom_excerpt,
         'status': status}]}
    print(body)
    r = requests.post(url, json=body, headers=headers)
    return r

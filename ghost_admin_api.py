from flask import Flask
app = Flask(__name__)
import requests # pip install requests
import jwt	# pip install pyjwt
from datetime import datetime as date
from setting import GHOST_ADMIN_API_TOKEN
from setting import GHOST_ADMIN_URL
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
url = GHOST_ADMIN_URL+'/posts/'
headers = {'Authorization': 'Ghost {}'.format(token.decode())}
def send_post(post):
	body = {'posts': [{'title': post['title'], 'mobiledoc': post['mobiledoc'], 'html': post['html'], 'plaintext': post['plaintext'], 'feature_image': post['feature_image'], 'custom_excerpt': post['custom_excerpt'], 'status' :'draft'}]}
	r = requests.post(url, json=body, headers=headers)
	return r
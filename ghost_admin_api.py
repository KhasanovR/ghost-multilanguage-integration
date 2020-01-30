from flask import Flask
app = Flask(__name__)
import requests # pip install requests
import jwt	# pip install pyjwt
from datetime import datetime as date
from setting import GHOST_ADMIN_API_TOKEN
from setting import GHOST_ADMIN_URL
from googletrans import Translator
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
url = GHOST_ADMIN_URL+'/posts/'
headers = {'Authorization': 'Ghost {}'.format(token.decode())}
def send_post(post):
	title = ''
	mobiledoc = ''
	html = ''
	plaintext = ''
	feature_image = ''
	custom_excerpt = ''
	if post['title']:
		title=translator.translate(post['title'], src='en', dest='ru').text
	if post['mobiledoc']:
		mobiledoc=post['mobiledoc']
	if post['html']:
		html=translator.translate(post['html'], src='en', dest='ru').text
	if post['plaintext']:
		plaintext=translator.translate(post['plaintext'], src='en', dest='ru').text
	if post['feature_image']:
		feature_image=post['feature_image']
	if post['custom_excerpt']:
		custom_excerpt= translator.translate(post['custom_excerpt'], src='en', dest='ru').text 
	status='draft'
	body = {'posts': [
		{'title':  title, 
		'mobiledoc':  mobiledoc, 
		'html':  html, 
		'plaintext':  plaintext, 
		'feature_image': feature_image, 
		'custom_excerpt':  custom_excerpt, 
		'status' : status}]}
	print(body)
	r = requests.post(url, json=body, headers=headers)
	return r
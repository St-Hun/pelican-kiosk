# generate_jwt.py

import jwt
import datetime

secret_key = 'your_secret_key'
payload = {
    'user_id': '12345',
    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
}

token = jwt.encode(payload, secret_key, algorithm='HS256')
print(token)

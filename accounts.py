import jwt
import requests
import uuid
# from urllib.parse import urlencode, unquote

with open("./upbit.key") as f:
    lines = f.readlines()
    access_key = lines[0].strip()
    secret_key = lines[1].strip()
    server_url = 'https://api.upbit.com'

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorization = 'Bearer {}'.format(jwt_token)

headers = {
  'Authorization': authorization,
}

res = requests.get(server_url + '/v1/accounts', headers=headers)
balance = int(float(res.json()[0]["balance"]))
print(f"{balance : ,}")
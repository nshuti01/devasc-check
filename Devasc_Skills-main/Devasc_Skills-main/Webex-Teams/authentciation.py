import requests
import json

access_token = 'Njc3NDE5YjktZDc5MC00ZWRiLWFiMTUtMGI0NWEwZDJkMDExMDE3YzBhZDEtNGMy_PE93_74cc8408-7643-4e09-b2b1-682def4bf071'
url = 'https://webexapis.com/v1/people/me'
headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
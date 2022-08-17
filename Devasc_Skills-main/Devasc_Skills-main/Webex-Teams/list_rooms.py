import requests

access_token = 'Njc3NDE5YjktZDc5MC00ZWRiLWFiMTUtMGI0NWEwZDJkMDExMDE3YzBhZDEtNGMy_PE93_74cc8408-7643-4e09-b2b1-682def4bf071' 
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'max': '100'}
res = requests.get(url, headers=headers, params=params)
print(res.json())
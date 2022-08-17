import requests

access_token = 'Njc3NDE5YjktZDc5MC00ZWRiLWFiMTUtMGI0NWEwZDJkMDExMDE3YzBhZDEtNGMy_PE93_74cc8408-7643-4e09-b2b1-682def4bf071'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'Devasc_Skills_RedonMiftari'}
res = requests.post(url, headers=headers, json=params)
print(res.json())
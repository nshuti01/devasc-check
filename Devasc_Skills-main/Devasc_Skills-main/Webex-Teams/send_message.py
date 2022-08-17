import requests

access_token = 'Njc3NDE5YjktZDc5MC00ZWRiLWFiMTUtMGI0NWEwZDJkMDExMDE3YzBhZDEtNGMy_PE93_74cc8408-7643-4e09-b2b1-682def4bf071'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vZmQ0NzhhYzAtNzg0YS0xMWVjLWIzNzQtNGI0ODljOGI4MjYy'
message = 'Here are my screenshots of devasc skills-based exam'
url = 'https://webexapis.com/v1/messages'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())
import requests
import json

ALL_PLAYERS = 'https://fantasy.premierleague.com/api/bootstrap-static/'

players = {}

r = requests.get(ALL_PLAYERS)
json_resp = json.loads(r.text)
for elem in json_resp['elements']:
	players[elem['id']] = str(elem['first_name']) + ' ' + str(elem['second_name'])

print(players[5])

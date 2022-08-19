import requests
import json
import pandas as pd

def weapons_name():
	response = requests.get('https://valorant-api.com/v1/weapons')
	result = pd.DataFrame(response.json()['data'])
	result2 = result['displayName']
	with open('weapons_data.txt', 'w') as f:
		for line in result2:
			f.write(line)
			f.write('\n')
weapons_name()

def weapons_uuid():
	response = requests.get('https://valorant-api.com/v1/weapons')
	result = pd.DataFrame(response.json()['data'])
	result2 = result['uuid']
	with open('weapons_data_uuid.txt', 'w') as f:
		for line in result2:
			f.write(line)
			f.write('\n')
weapons_uuid()

data = data2 = ""
with open('weapons_data.txt') as fp:
	data = fp.read()

with open('weapons_data_uuid.txt') as fp:
	data2 = fp.read()

data += '''
--------------------uuid--------------------\n'''
data += data2

with open('Weapons_Result.txt', 'w') as fp:
	fp.write(data)
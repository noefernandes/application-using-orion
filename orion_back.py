import requests
import json

#Resgistrar loja ***********************************************************************************

#Loja1
'''
data = { "contextElements": [{ "type": "LojaRoupas", "isPattern": "false", "id":
"loja1", "attributes": [ { "name": "position", "type": "coords",
"value": "-5.80248, -35.201", "metadatas": [ { "name":
"location", "type": "string", "value": "WGS84" } ] }, { "name": "roupa", "type": "estilo",
"value": "esportiva"} ] } ],
"updateAction": "APPEND" }
'''
'''
data = { "contextElements": [{ "type": "LojaRoupas", "isPattern": "false", "id":
"loja1", "attributes": [ { "name": "position", "type": "coords",
"value": "-5.80248, -35.201", "metadatas": [ { "name":
"location", "type": "string", "value": "WGS84" } ] }, { "name": "roupa", "type": "estilo",
"value": "tradicional"} ] } ],
"updateAction": "APPEND" }
'''

#Loja2

data = { "contextElements": [{ "type": "LojaRoupas", "isPattern": "false", "id":
"loja2", "attributes": [ { "name": "position", "type": "coords",
"value": "-5.78648, -35.201", "metadatas": [ { "name":
"location", "type": "string", "value": "WGS84" } ] }, { "name": "roupa", "type": "estilo",
"value": "esportiva"} ] } ],
"updateAction": "APPEND" }

'''
data = { "contextElements": [{ "type": "LojaRoupas", "isPattern": "false", "id":
"loja2", "attributes": [ { "name": "position", "type": "coords",
"value": "-5.78648, -35.201", "metadatas": [ { "name":
"location", "type": "string", "value": "WGS84" } ] }, { "name": "roupa", "type": "estilo",
"value": "tradicional"} ] } ],
"updateAction": "APPEND" }
'''

URL = "http://127.0.0.1:1026/v1/updateContext"
headers = {'content-type': 'application/json'}
r = requests.post(url = URL, data = json.dumps(data), headers=headers)
data = r.json()
print(data)






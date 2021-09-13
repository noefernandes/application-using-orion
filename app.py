from flask import Flask, request
import json
import requests

app = Flask(__name__)

# Abrir localhost:5000 para ver a respostas.
@app.route('/')
def get_lojas():
	r = requests.get(url = "http://127.0.0.1:1026/v2/entities?type=LojaRoupas")
	data = r.json()
	return json.dumps(data)
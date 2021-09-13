import requests
import json
import time
import pandas as pd
import folium
import webbrowser

estilo_pref = 'esportiva'

estilo_1 = ''
estilo_2 = ''
while(True):
	URL = "http://localhost:5000/"
	r = requests.get(url = URL)
	data = r.json()
	if(len(data) > 0):
		coord_str_1 = data[0]['position']['value'].split(',')
		coord_1 = float(coord_str_1[0].strip()), float(coord_str_1[1].strip())
		estilo_1_novo = data[0]['roupa']['value']
		print("Loja 1 = " + estilo_1_novo)
		if(estilo_1_novo != estilo_1 and estilo_1_novo == estilo_pref):
			natal = folium.Map(location=[-5.79448, -35.211], zoom_start=15)
			folium.Marker(
				location=coord_1
			).add_to(natal)
			natal.save("natal.html")
			webbrowser.open("natal.html", 0)
		elif(len(data) > 1):
			coord_str_2 = data[1]['position']['value'].split(',')
			coord_2 = float(coord_str_2[0].strip()), float(coord_str_2[1].strip())
			estilo_2_novo = data[1]['roupa']['value']
			print("loja 2 = " + estilo_2_novo)
			if(estilo_2_novo != estilo_2 and estilo_2_novo == estilo_pref):
				natal = folium.Map(location=[-5.79448, -35.211], zoom_start=15)
				folium.Marker(
					location=coord_2,
				).add_to(natal)
				natal.save("natal.html")
				webbrowser.open("natal.html", 0)
			estilo_2 = estilo_2_novo
		estilo_1 = estilo_1_novo
	time.sleep(3)




import json

#1. Listar información: listar los nombres de cada campeón con
#su título y las etiquetas de cada uno.
def listar(lol):
	campeon=[]
	titulo=[]
	roles=[]
	for i in lol:
		campeon.append(i['name'])
		titulo.append(i['title'])
		roles.append(i['tags'])
	return zip(campeon,titulo,roles)

#2. Contar información: contar el número de campeones total existentes
#y el número de etiquetas distintas en total.
def contar_campeones(lol):
	campeones=[]
	for i in lol:
		campeones.append(i['name'])
	return campeones
def contar_roles(lol):
	roles=[]
	for i in lol:
		for j in i['tags']:
			if j not in roles:
				roles.append(j)
	return roles

#3. Buscar o filtrar información: introducir el nombre de un campeón y
#mostrar sus estadísticas.
def buscar(lol,nombre):
	estadisticas=[]
	for i in lol:
		if nombre in i['name']:
			estadisticas.append(i['stats'])
	if len(estadisticas)==0:
		return False
	else:
		return estadisticas


#4. Buscar información relacionada: introducir una etiqueta y
#mostrar todos los campeones que tienen esa etiqueta.
def buscar_info(lol,rol):
	campeones=[]
	for i in lol:
		if rol in i['tags']:
			campeones.append(i['name'])
	if len(campeones)==0:
		return False
	else:
		return campeones

#5. Libre: introducir un valor de una estadística de armadura,
#vida o ataque, y mostrar los campeones que tienen una estadística igual
#o superior al valor dado.
def libre(lol,opcion,valor):
	campeones=[]
	if opcion==1:
		for i in lol:
			if i['stats']['hp'] >= valor:
				campeones.append(i['name'])
	if opcion==2:
		for i in lol:
			if i['stats']['armor'] >= valor:
				campeones.append(i['name'])
	if opcion==3:
		for i in lol:
			if i['stats']['attackdamage'] >= valor:
				campeones.append(i['name'])
	return campeones
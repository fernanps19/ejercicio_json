import json
from FuncionesJSON import *

with open("lol_characters.json") as fichero:
	lol=json.load(fichero)
	
print('MENU')
print('1. Listar campeones con su título y rol/es.')
print('2. Mostrar el número de campeones en total y de roles distintos en total.')
print('3. Mostrar las estadísticas del campeón a buscar.')
print('4. Buscar campeones a partir de un rol.')
print('5. Buscar un campeón a partir de una estadística: vida, armadura o ataque.')
print('0. Salir')
opcion=int(input('Introduzca una opcion:'))

while opcion!=0:

#1
	if opcion==1:
		for i in listar(lol):
			print('*',i[0])
			print('  -Título:',i[1])
			print('  -Roles:')
			for j in i[2]:
				print('   ',j)

#2
	elif opcion==2:
		print('Campeones:',len(contar_campeones(lol)))
		print('Roles:',len(contar_roles(lol)))

#3
	elif opcion==3:
		nombre=input('Introduzca un campeón:')
		if buscar(lol,nombre)==False:
			print('No existe ese campeón.')
		else:
			for i in buscar(lol,nombre):
				print('Vida:',i['hp'])
				print('Armadura:',i['armor'])
				print('Resistencia Mágica:',i['spellblock'])
				print('Daño Físico:',i['attackdamage'])
				print('Rango:',i['attackrange'])

#4
	elif opcion==4:
		rol=input('Introduzca un rol de campeón:')
		if buscar_info(lol,rol)==False:
			print('No existe ese rol.')
		else:
			for i in buscar_info(lol,rol):
				print(i)

#5
	elif opcion==5:
		print('1. Puntos de vida.')
		print('2. Puntos de armadura.')
		print('3. Puntos de ataque.')
		opcion1=int(input('Introduzca una opción:'))
		if opcion1==1:
			valor=int(input('Introduzca un valor a buscar:'))
			print('Campeones con una vida igual o superior:')
			for i in libre(lol,opcion1,valor):
				print(i)
		elif opcion1==2:
			valor=int(input('Introduzca un valor a buscar:'))
			print('Campeones con una armadura igual o superior:')
			for i in libre(lol,opcion1,valor):
				print(i)
		elif opcion1==3:
			valor=int(input('Introduzca un valor a buscar:'))
			print('Campeones con un ataque igual o superior:')
			for i in libre(lol,opcion1,valor):
				print(i)
		else:
			print('¡Tiene que ser un valor de la lista!')

	else:
		print('¡Error: debe ser un valor de la lista anterior!')

	print('1. Listar campeones con su título y rol/es.')
	print('2. Mostrar el número de campeones en total y de roles distintos en total.')
	print('3. Mostrar las estadísticas del campeón a buscar.')
	print('4. Buscar campeones a partir de un rol.')
	print('5. Buscar un campeón a partir de una estadística: vida, armadura o ataque.')
	print('0. Salir')
	opcion=int(input('Introduzca un valor de los anteriores:'))

print('¡Hasta luego!')
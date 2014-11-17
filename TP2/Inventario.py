#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

d = []
S = 0
C = 0
K = 0
n = 0

def parsear_entrada(nombre_archivo):
	global d
	global S
	global C
	global K
	global n

	try:
		archivo = open(nombre_archivo,'r')
	except IOError:
		raise IOError, "Fallo al abrir el archivo de entrada"

	n = int( archivo.readline().rstrip() )
	S = int( archivo.readline().rstrip() )
	C = int( archivo.readline().rstrip() )
	K = int( archivo.readline().rstrip() )
	#salteo linea en blanco
	archivo.readline()

	for i in xrange(0,n):
		d.append( int( archivo.readline().rstrip() ) )


def matriz_de_costos():
	#inicializo costos y estados
	costos = []
	for i in xrange(0,n):
		costos.append([])

	for j in xrange(0,S):
		#tupla(costo del mes, sobrante al final del mes anterior)
		costos[0].append( (K, 0) )

	#matriz: costos[mes, sobrante_al_final] = costo incurrido
	for i in xrange(1,n):
		for j in xrange(0,S):
			if j+d[i] >= S:
				#costos[i][j] = costos[i-1][0] + K
				costos[i].append( (costos[i-1][0][0] + K, 0) )
			else:
				#costos[i][j] = min(costos[i-1][j+d[i]] + C*(j+d[i]), costos[i-1][0] + K)
				costo_de_almacenamiento = costos[i-1][j+d[i]][0] + C*(j+d[i])
				costo_de_compra = costos[i-1][0][0] + K
				if costo_de_almacenamiento <= costo_de_compra:
					costos[i].append( (costo_de_almacenamiento, j+d[i]) )
				else:
					costos[i].append( (costo_de_compra, 0) )

	#costo total: print( costos[n-1][0] )
	return costos


def plan_de_compras(matriz_costos, meses, sobrante_final):
	#inicializo para <meses> meses
	plan = [None] * meses

	sobrante = sobrante_final
	#bucle desde el último mes hasta el primero
	for mes in xrange(meses-1, -1, -1):
		#compro lo que espero vender + lo que tiene que sobrar al final - lo que tenia guardado
		plan[mes] = d[mes] + sobrante - matriz_costos[mes][sobrante][1]
		#actualizo el sobrante
		sobrante = matriz_costos[mes][sobrante][1]

	return plan


def mostrar_plan_de_compras(plan):
	print("Plan de compras a " + str(n) + " meses:\n")

	for i in xrange(0, len(plan)):
		print( "Mes " + str(i+1) + ": " + str(plan[i]) + " camiones")


def main(argv):
	parsear_entrada(argv[1])
	costos = matriz_de_costos()
	plan = plan_de_compras( costos, n, 0)
	mostrar_plan_de_compras( plan )

main(sys.argv)
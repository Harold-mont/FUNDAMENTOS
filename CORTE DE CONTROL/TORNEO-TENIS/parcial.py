'''
A) El famoso torneo de tenis Rolan Garrón se disputa todos los años. Los resultados se guardan en el archivo resultados.csv. 
Este archivo tiene el siguiente formato:
dia, participantel, puntos1_sets, participante2, puntos2_sets
El archivo se guarda en forma secuencial, comenzando desde el día 1 del campeonato, por lo que queda ordenado por día. 
Los partidos se juegan al mejor de cinco sets, en caso de ganar los tres primeros, no hace falta jugar los dos que le siguen, 
es por lo que hay partidos de tres, de cuatro y de cinco sets.

Ejemplo:
1,Jarry Nicolas,6-6-6,Dellien Hugo,4-4-2
1,Purcell Max,7-1-6-6,Thompson Jordan,5-6-4-4
2,Zapata Miralles,6-7-2-0-4,Schwartzman Diego,1-6-6-6-6
etc...

Se pide realizar un programa modular (compuesto por funciones), en Python que:

1) Recorriendo una sola vez el archivo de resultados y sin cargarlo completamente en memoria, haga un corte por día, indicando: 
día, cantidad de partidos jugados, cantidad de set jugados.
Con nuestro ejemplo sería:
Día     Partidos    Sets
1           2         7
2           1         5

2) Realizando una nueva lectura del archivo, arme un diccionario en donde la clave será el nombre del jugador y el dato la cantidad de partidos ganados. 
Tener en cuenta que gana el jugador que consigue tres sets.

3) En base al diccionario generado en el punto 2, dejar en el archivo ganados.txt, un listado, ordenado de mayor a menor por cantidad de partidos ganados, 
indicando por cada línea del archivo: el nombre del jugador - la cantidad de partidos ganados.
'''
MAX = 50

def leer(archivo):
    linea = archivo.readline()
    if linea:
        devolver = linea.rstrip('\n').split(',')
    else:
        devolver = MAX,'','','',''
    return devolver

def listar(archivo):
    dia, participante1, puntos1_sets, participante2, puntos2_sets = leer(archivo)
    dia = int(dia)
    print('Día   Partidos   Sets')
    while dia < MAX:
        partidos_jugados = 0
        sets_jugados = 0
        dia_anterior = dia
        
        while dia < MAX and dia_anterior == dia:
            partidos_jugados += 1
            sets = len(puntos1_sets.split('-'))
            sets_jugados += sets
            
            dia, participante1, puntos1_sets, participante2, puntos2_sets = leer(archivo)
            dia = int(dia)
        print(f'{dia_anterior}       {partidos_jugados}         {sets_jugados}')

def diccionario(archivo):
    dia, participante1, puntos1_sets, participante2, puntos2_sets = leer(archivo)
    dia = int(dia)
    diccionario = {}
    puntos1_sets = puntos1_sets.split('-')
    puntos2_sets = puntos2_sets.split('-')

    while dia < MAX:
        ganados1 = 0
        ganados2 = 0
        partidos1 = 0
        partidos2 = 0
        
        for i in range(len(puntos1_sets)):
            puntos1 = int(puntos1_sets[i])
            puntos2 = int(puntos2_sets[i])
            
            if puntos1 > puntos2:
                ganados1 += 1
            elif puntos1 < puntos2:
                ganados2 += 1
                
        if ganados1 >= 3:
            partidos1 += 1
        elif ganados2 >= 3:
            partidos2 += 1
        
        diccionario[participante1] = partidos1
        diccionario[participante2] = partidos2
        
        dia, participante1, puntos1_sets, participante2, puntos2_sets = leer(archivo)
        puntos1_sets = puntos1_sets.split('-')
        puntos2_sets = puntos2_sets.split('-')
        dia = int(dia)
        
    return diccionario

def escribir(jugador, partidos_ganados, archivo):
    archivo.write('Nombre de jugador: ' + jugador + ' - ' + 'Partidos ganados: ' + str(partidos_ganados) + '\n')

def dicc_ordenado(diccionario, archivo):
    ordenado = sorted(diccionario.items(), key = lambda x : x[1], reverse = True)
    
    for item in ordenado:
        jugador = item[0]
        partidos_ganados = item[1]
        escribir(jugador, partidos_ganados, archivo)

def main():
    archivo = open('./2DO-PARCIAL/parcial3/resultados.csv')
    listar(archivo)
    archivo.close()
    
    archivo2 = open('./2DO-PARCIAL/parcial3/resultados.csv')
    resultado = diccionario(archivo2)
    archivo2.close()
    
    archivo3 = open('./2DO-PARCIAL/parcial3/ganados.txt', 'w')
    dicc_ordenado(resultado, archivo3)
    archivo3.close()

main()
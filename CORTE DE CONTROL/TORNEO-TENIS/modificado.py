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

# ==========================================
# Lee un registro del archivo resultados.csv
# ==========================================
def leer_partido(archivo):
    linea = archivo.readline()
    
    if not linea:
        fin = True
        dia = participante1 = puntos1 = participante2 = puntos2 = ""
    else:
        fin = False
        linea = linea.rstrip()
        campos = linea.split(",")
        dia = int(campos[0])
        participante1 = campos[1]
        puntos1 = campos[2].split("-")  # lista de sets
        participante2 = campos[3]
        puntos2 = campos[4].split("-")  # lista de sets

    return fin, dia, participante1, puntos1, participante2, puntos2


# ==========================================
# Punto 1: Informe por día
# ==========================================
def informe_por_dia(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    fin, dia, p1, sets1, p2, sets2 = leer_partido(archivo)

    print("Día\tPartidos\tSets")

    while not fin:
        dia_actual = dia
        partidos_dia = 0
        sets_dia = 0

        while not fin and dia == dia_actual:
            partidos_dia += 1
            sets_dia += len(sets1)  # cantidad de sets jugados
            fin, dia, p1, sets1, p2, sets2 = leer_partido(archivo)

        print(f"{dia_actual}\t{partidos_dia}\t\t{sets_dia}")

    archivo.close()


# ==========================================
# Punto 2: Diccionario de partidos ganados
# ==========================================
def diccionario_partidos_ganados(nombre_archivo):
    dic = {}

    archivo = open(nombre_archivo, "r")
    fin, dia, p1, sets1, p2, sets2 = leer_partido(archivo)

    while not fin:
        # Contar sets ganados manualmente sin zip
        sets_ganados_p1 = 0
        sets_ganados_p2 = 0

        for i in range(len(sets1)):
            s1 = int(sets1[i])
            s2 = int(sets2[i])
            if s1 > s2:
                sets_ganados_p1 += 1
            elif s2 > s1:
                sets_ganados_p2 += 1

        # Determinar ganador sin usar None
        if sets_ganados_p1 >= 3:
            ganador = p1
        elif sets_ganados_p2 >= 3:
            ganador = p2
        else:
            ganador = ""  # si por error no hay ganador, no lo contamos

        if ganador != "":
            if ganador not in dic:
                dic[ganador] = 0
            dic[ganador] += 1

        fin, dia, p1, sets1, p2, sets2 = leer_partido(archivo)

    archivo.close()
    return dic


# ==========================================
# Punto 3: Archivo ganados.txt
# ==========================================
def generar_archivo_ganadores(dic):
    lista = []

    for jugador in dic:
        lista.append((jugador, dic[jugador]))

    # Ordenar de mayor a menor por partidos ganados usando lambda
    lista.sort(key=lambda x: x[1], reverse=True)

    archivo = open("ganados.txt", "w")
    for jugador, ganados in lista:
        archivo.write(f"{jugador} - {ganados}\n")
    archivo.close()


# ==========================================
# Programa principal
# ==========================================
def main():
    archivo = "resultados.csv"

    print("=== Informe por día ===")
    informe_por_dia(archivo)

    dic_ganadores = diccionario_partidos_ganados(archivo)
    generar_archivo_ganadores(dic_ganadores)


main()

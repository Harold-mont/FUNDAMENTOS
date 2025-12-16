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


def leer(arc):
    linea = arc.readline()
    if linea:
        devolver = linea.rstrip("\n").split(",")
    else:
        devolver = "", "", "", "", ""
    return devolver


# ---------------------------------------------------------
# 1) CORTE DE CONTROL POR DÍA
# ---------------------------------------------------------
def corte_por_dia(nombre_archivo):

    with open(nombre_archivo, "r") as arc:
        dia, p1, sets1, p2, sets2 = leer(arc)

        print("Día\tPartidos\tSets")

        while dia:
            dia_actual = dia
            cant_partidos = 0
            cant_sets = 0

            # Corte por día
            while dia == dia_actual:
                cant_partidos += 1
                cant_sets += len(sets1.split("-"))
                dia, p1, sets1, p2, sets2 = leer(arc)

            print(f"{dia_actual}\t{cant_partidos}\t\t{cant_sets}")


# ---------------------------------------------------------
# 2) DICCIONARIO DE PARTIDOS GANADOS
# ---------------------------------------------------------
def determinar_ganador(sets1, sets2):

    lista1_str = sets1.split("-")
    lista2_str = sets2.split("-")

    lista1 = []
    lista2 = []

    for valor in lista1_str:
        lista1.append(int(valor))

    for valor in lista2_str:
        lista2.append(int(valor))

    puntos1 = 0
    puntos2 = 0

    i = 0
    while i < len(lista1) and i < len(lista2):
        if lista1[i] > lista2[i]:
            puntos1 += 1
        else:
            puntos2 += 1
        i += 1

    # Determinar ganador sin usar múltiples returns
    ganador = 1
    if puntos2 > puntos1:
        ganador = 2

    return ganador


# ---------------------------------------------------------
# 3) GENERAR ARCHIVO ganados.txt ORDENADO
# ---------------------------------------------------------
def calcular_ganados(nombre_archivo):
    ganados = {}

    with open(nombre_archivo, "r") as arc:
        dia, p1, sets1, p2, sets2 = leer(arc)

        while dia:
            ganador = determinar_ganador(sets1, sets2)

            if ganador == 1:
                jugador = p1
            else:
                jugador = p2

            if jugador in ganados:
                ganados[jugador] += 1
            else:
                ganados[jugador] = 1

            dia, p1, sets1, p2, sets2 = leer(arc)

    return ganados


def guardar_ganados(ganados):
    # Ordenar de mayor a menor
    lista_ordenada = sorted(ganados.items(), key=lambda x: x[1], reverse=True)

    with open("ganados.txt", "w") as salida:
        for jugador, cantidad in lista_ordenada:
            salida.write(f"{jugador} - {cantidad}\n")


# ---------------------------------------------------------
# BLOQUE PRINCIPAL
# ---------------------------------------------------------
def main():
    archivo = "resultados.csv"

    print("\n--- CORTE POR DÍA ---")
    corte_por_dia(archivo)

    print("\n--- CALCULANDO GANADOS ---")
    ganados = calcular_ganados(archivo)

    print("\n--- GENERANDO ARCHIVO ganados.txt ---")
    guardar_ganados(ganados)


main()

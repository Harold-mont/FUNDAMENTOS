'''
A) Se tienen los resultados de la Eurocopa y la Copa América en dos archivos de texto con formato csv, llamados eurocopa.csv y copa_america.csv. 
Estos archivos tienen en cada línea, el resultado de un partido. Los campos son:

dia, equipo_local, goles_local, equipo_visitante, goles_visitante

Los archivos se guardaron en forma secuencial, comenzando desde el día 1 del campeonato, por lo que están ordenados por dia.
Ejemplo:
1,Alemania,5,Escocia,1
2,Hungria,1,Suiza,3
2,Espania,3,Croacia,0
2,Italia,2,Albania,1
etc..

Se pide realizar un programa modular (compuesto por funciones), en Python que:
1) Recorriendo una sola vez los dos archivos y sin cargarlos completamente en memoria, los unifique (merge) en un único archivo ordenado por dia, 
manteniendo el orden original y agregando un campo que indique de qué archivo es la linea que se está escribiendo (EUROCOPA o COPA AMERICA), 
ante igualdad de dia, guardar en primer lugar los de la EUROCOPA

2) Realizando una lectura del archivo generado en el punto anterior, arme un diccionario en donde la clave será el país y el dato será una lista de 
longitud 3: partidos ganados, empatados y perdidos.

3) En base al diccionario generado en el punto 2 mostrar por pantalla un listado, ordenado de mayor a menor por cantidad de partidos ganados, 
indicando: pais, partidos ganados. En este listado no deben figurar los países que no ganaron ningún partido.
'''

# ===============================
# LECTURA DE REGISTRO
# ===============================
def leer(archivo):
    linea = archivo.readline()

    if linea == "":
        fin = True
        dia = equipo_l = equipo_v = ""
        goles_l = goles_v = 0
    else:
        fin = False
        linea = linea.rstrip()
        campos = linea.split(",")

        dia = int(campos[0])
        equipo_l = campos[1]
        goles_l = int(campos[2])
        equipo_v = campos[3]
        goles_v = int(campos[4])

    return fin, dia, equipo_l, goles_l, equipo_v, goles_v


# ===============================
# GUARDAR REGISTRO
# ===============================
def guardar(dia, equipo_l, goles_l, equipo_v, goles_v, torneo, archivo):
    archivo.write(
        str(dia) + "," +
        equipo_l + "," +
        str(goles_l) + "," +
        equipo_v + "," +
        str(goles_v) + "," +
        torneo + "\n"
    )


# ===============================
# MERGE DE LOS DOS ARCHIVOS
# ===============================
def mezclar(euro, copa, salida):

    f1, d1, el1, gl1, ev1, gv1 = leer(euro)
    f2, d2, el2, gl2, ev2, gv2 = leer(copa)

    while not f1 or not f2:

        minimo = 9999
        if not f1 and d1 < minimo:
            minimo = d1
        if not f2 and d2 < minimo:
            minimo = d2

        # ===== EUROCOPA (PRIORIDAD) =====
        while not f1 and d1 == minimo:
            guardar(d1, el1, gl1, ev1, gv1, "EUROCOPA", salida)
            f1, d1, el1, gl1, ev1, gv1 = leer(euro)

        # ===== COPA AMERICA =====
        while not f2 and d2 == minimo:
            guardar(d2, el2, gl2, ev2, gv2, "COPA_AMERICA", salida)
            f2, d2, el2, gl2, ev2, gv2 = leer(copa)


# ===============================
# ACTUALIZAR ESTADISTICAS
# ===============================
def actualizar(dic, equipo, resultado):
    if equipo not in dic:
        dic[equipo] = [0, 0, 0]

    dic[equipo][resultado] += 1


# ===============================
# ARMAR DICCIONARIO
# ===============================
def armar_diccionario(archivo):

    dic = {}

    linea = archivo.readline()
    while linea != "":
        campos = linea.rstrip().split(",")

        equipo_l = campos[1]
        goles_l = int(campos[2])
        equipo_v = campos[3]
        goles_v = int(campos[4])

        if goles_l > goles_v:
            actualizar(dic, equipo_l, 0)
            actualizar(dic, equipo_v, 2)
        elif goles_l < goles_v:
            actualizar(dic, equipo_l, 2)
            actualizar(dic, equipo_v, 0)
        else:
            actualizar(dic, equipo_l, 1)
            actualizar(dic, equipo_v, 1)

        linea = archivo.readline()

    return dic


# ===============================
# MOSTRAR RESULTADOS
# ===============================
def mostrar(dic):

    lista = []
    for pais in dic:
        if dic[pais][0] > 0:
            lista.append((pais, dic[pais][0]))

    lista.sort(key=lambda x: x[1], reverse=True)

    for pais, ganados in lista:
        print(pais, ganados)


# ===============================
# PROGRAMA PRINCIPAL
# ===============================
def main():

    euro = open("eurocopa.csv", "r")
    copa = open("copa_america.csv", "r")
    salida = open("partidos_merge.csv", "w")

    mezclar(euro, copa, salida)

    euro.close()
    copa.close()
    salida.close()

    salida = open("partidos_merge.csv", "r")
    dic = armar_diccionario(salida)
    salida.close()

    mostrar(dic)


main()

'''
A) Durante el año 2023, la Facultad de Ingeniería ha dictado cursos para el plan Argentina Programa 4.0. En el segundo tramo del programa, 
se ofrecieron los cursos de: Python, Java, Programación Front End, Programación Back End y Testing. Cada uno de estos cursos tenía entre 2 y 
hasta 6 comisiones, con 120 alumnos en promedio por comisión.

El archivo inscriptos_AP40.csv, posee los siguientes datos:
Nro_Inscripto, Nivel_Educativo, Trabaja_Actualmente, Nombre_Curso, Codigo_Comision
Se encuentra ordenado por Curso y dentro de este por Comisión.

Escribir un programa modular (compuesto por funciones), en Python, que en base a los datos que se encuentran en el archivo inscriptos_AP40.csv, genere:

a. Recorriendo sólo una vez el archivo, un informe indicando el nombre del curso, y para cada curso, las comisiones y la cantidad de alumnos inscriptos 
en cada una de las comisiones. Además por cada curso debe informar el total de alumnos inscriptos. Al final del listado se debe informar el total 
de alumnos inscriptos en todos los cursos, y que porcentaje de estos trabaja (este dato viene indicado con un "si", en el respectivo campo).

b. Realizando una nueva lectura del archivo, arme un diccionario en donde la clave será el Nombre del Curso y asociado a este, una lista con: 
la cantidad de inscriptos con estudios primarios, la cantidad con estudios secundarios y la cantidad con estudios universitarios (este dato viene 
indicado en el campo Nivel Educativo, como "PRI", "SEC", "UNI").

c. En base al diccionario del punto anterior, dejar en el archivo inscripciones.txt, un listado ordenado de menor a mayor por el total de inscriptos 
en cada curso, indicando por cada línea del archivo: Nombre del Curso - Total Inscriptos - Cant. Est. Prim. - Cant. Est. Sec. - Cant. Est. Univ.
'''

def leer(arc):
    linea = arc.readline()
    if linea:
        return linea.rstrip("\n").split(",")
    else:
        return "", "", "", "", ""


def informe_cursos(nombre_archivo):
    with open(nombre_archivo, "r") as arc:
        nro, nivel, trabaja, curso, comision = leer(arc)

        print("Curso         Comisión     Inscriptos")
        print("--------------------------------------")

        total_general = 0
        total_trabajan = 0

        while curso:
            curso_actual = curso
            total_curso = 0

            while curso == curso_actual:
                comision_actual = comision
                cant_comision = 0

                while curso == curso_actual and comision == comision_actual:
                    cant_comision += 1
                    total_curso += 1
                    total_general += 1

                    if trabaja.lower() == "si":
                        total_trabajan += 1

                    nro, nivel, trabaja, curso, comision = leer(arc)

                print(f"{curso_actual:15} {comision_actual:10} {cant_comision}")

            print(f"TOTAL {curso_actual}: {total_curso}\n")

        # Porcentaje
        if total_general > 0:
            porcentaje = (total_trabajan * 100) / total_general
        else:
            porcentaje = 0

        print("--------------------------------------")
        print(f"TOTAL GENERAL DE INSCRIPTOS: {total_general}")
        print(f"PORCENTAJE QUE TRABAJA: {porcentaje:.2f}%")


def diccionario_niveles(nombre_archivo):
    datos = {}

    with open(nombre_archivo, "r") as arc:
        nro, nivel, trabaja, curso, comision = leer(arc)

        while curso:
            if curso not in datos:
                datos[curso] = [0, 0, 0]   # PRI, SEC, UNI

            # contar niveles
            if nivel == "PRI":
                datos[curso][0] += 1
            elif nivel == "SEC":
                datos[curso][1] += 1
            elif nivel == "UNI":
                datos[curso][2] += 1

            nro, nivel, trabaja, curso, comision = leer(arc)

    return datos


def guardar_inscripciones(diccionario):
    lista = []

    # Convertir diccionario → lista para ordenar
    for curso in diccionario:
        pri, sec, uni = diccionario[curso]
        total = pri + sec + uni
        lista.append((curso, total, pri, sec, uni))

    # ordenar de menor a mayor
    lista_ordenada = sorted(lista, key=lambda x: x[1])

    with open("inscripciones.txt", "w") as salida:
        for curso, total, pri, sec, uni in lista_ordenada:
            salida.write(f"{curso} - {total} - {pri} - {sec} - {uni}\n")


def main():
    archivo = "inscriptos_AP40.csv"

    print("\n--- INFORME (UNA SOLA PASADA) ---")
    informe_cursos(archivo)

    print("\n--- GENERANDO DICCIONARIO DE NIVELES ---")
    dicc = diccionario_niveles(archivo)

    print("\n--- GENERANDO ARCHIVO inscripciones.txt ---")
    guardar_inscripciones(dicc)


main()

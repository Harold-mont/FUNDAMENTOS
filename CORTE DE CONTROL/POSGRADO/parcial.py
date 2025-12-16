'''
En una materia de un posgrado, se aplica evaluación continua.
Esto consiste en pedir la entrega de actividades semanales.
En una semana puede haber ninguna, una o varias actividades.
Los resultados se guardan en un archivo notas.txt (CSV) con el
siguiente formato (a excepción de la primera línea, en donde
figura la cantidad de trabajos totales):

semana,actividad,apellido_nombre,nota

Ejemplo:
5
1,cuestionario t1,Gonzalez Carlos,5
1,cuestionario t1,Rodriguez Rosa,8
1,trabajo practico t1,Rodriguez Rosa,10
3,cuestionario t2_3,Gonzalez Carlos,4
...

En el ejemplo anterior, el docente pidió 5 trabajos en total
(primera línea). En la semana 1 se entregaron dos cuestionarios
y un trabajo práctico, con notas 5, 8 y 10, etc. Sabiendo que el
archivo está ordenado por semana y dentro de cada semana, por
actividad, y que la aprobación es con una nota de 6 o superior,
se pide realizar un programa modular en Python que:

1) Recorriendo una sola vez el archivo notas.txt y sin cargarlo
completamente en memoria, haga un corte de control por día y por
actividad, indicando: Cantidad de actividades semanales entregadas
y dentro de cada actividad, cantidad de entregados y aprobados.

Tomando el ejemplo anterior sería:

Semana 1:
--cuestionario t1: entregados: 2 - aprobados: 1
--trabajo practico t1: entregados: 1 - aprobados: 1
--Total de actividades semanales entregadas: 3

2) Realizando una nueva lectura del archivo notas.txt, arme un
diccionario en donde la clave será el nombre del estudiante y
el dato será una lsita de longitud 2: actividades entregadas,
actividades aprobadas. Al finalizar, imprimir un listado de los
estudiantes que entregaron todas las actividades (en el ejemplo,
deberían tener 5 actividades entregadas).

3) En base al diccionario generado en el punto 2 armar un listado,
ordenado de mayor a menor por cantidad de actividades aprobadas,
indicando: estudiante - actividades aprobadas. En este listado no
deben figurar los estudiantes que no aprobaron ninguna actividad.
'''

def leer(arc):
    linea = arc.readline()
    if linea:
        devolver = linea.rstrip("\n").split(",")
    else:
        devolver = "", "", "", ""
    return devolver


def listar_con_corte():
    with open("notas.txt", "r", encoding="utf-8") as arc:

        # Leer la primera línea (cantidad total de trabajos)
        total_trabajos = arc.readline().strip()

        # Leer primer registro útil
        semana, actividad, alumno, nota = leer(arc)

        # ---- CORTE GENERAL POR SEMANA ----
        while semana:
            semana_actual = semana
            print(f"Semana {semana_actual}:")
            total_semana = 0

            # ---- CORTE POR SEMANA ----
            while semana == semana_actual:

                actividad_actual = actividad
                entregados = 0
                aprobados = 0

                # ---- CORTE POR ACTIVIDAD ----
                while semana == semana_actual and actividad == actividad_actual:
                    entregados += 1
                    if int(nota) >= 6:
                        aprobados += 1

                    semana, actividad, alumno, nota = leer(arc)

                # Fin corte de actividad
                print(f"--{actividad_actual}: entregados: {entregados} - aprobados: {aprobados}")

                total_semana += entregados

            # Fin corte de semana
            print(f"--Total de actividades semanales entregadas: {total_semana}\n")

    return


# ----------------------------- #
#        BLOQUE PRINCIPAL      #
# ----------------------------- #
listar_con_corte()

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

# ==========================================
# Lee un registro del archivo de notas
# ==========================================
def leer(archivo):
    linea = archivo.readline()

    if linea == "":
        fin = True
        semana = actividad = alumno = ""
        nota = 0
    else:
        fin = False
        linea = linea.rstrip()
        campos = linea.split(",")

        semana = int(campos[0])
        actividad = campos[1]
        alumno = campos[2]
        nota = int(campos[3])

    return fin, semana, actividad, alumno, nota


# ==========================================
# Punto 1: corte de control por semana y actividad
# ==========================================
def informe_por_semana(archivo_notas):
    archivo = open(archivo_notas, "r")

    total_trabajos = int(archivo.readline().strip())
    fin, semana, actividad, alumno, nota = leer(archivo)

    while not fin:
        semana_actual = semana
        total_entregas_semana = 0
        print(f"Semana {semana_actual}:")

        while not fin and semana == semana_actual:
            actividad_actual = actividad
            entregados = 0
            aprobados = 0

            while (not fin and
                   semana == semana_actual and
                   actividad == actividad_actual):

                entregados += 1
                total_entregas_semana += 1
                if nota >= 6:
                    aprobados += 1

                fin, semana, actividad, alumno, nota = leer(archivo)

            print(f"--{actividad_actual}: entregados: {entregados} - aprobados: {aprobados}")

        print(f"--Total de actividades semanales entregadas: {total_entregas_semana}")
        print()

    archivo.close()


# ==========================================
# Punto 2: generar diccionario por estudiante
# ==========================================
def diccionario_estudiantes(archivo_notas):
    entregas_por_estudiante = {}

    archivo = open(archivo_notas, "r")

    total_trabajos = int(archivo.readline().strip())
    fin, semana, actividad, alumno, nota = leer(archivo)

    while not fin:
        if alumno not in entregas_por_estudiante:
            entregas_por_estudiante[alumno] = [0, 0]

        entregas_por_estudiante[alumno][0] += 1
        if nota >= 6:
            entregas_por_estudiante[alumno][1] += 1

        fin, semana, actividad, alumno, nota = leer(archivo)

    archivo.close()

    print("Estudiantes que entregaron todas las actividades:")
    for alumno in entregas_por_estudiante:
        if entregas_por_estudiante[alumno][0] == total_trabajos:
            print(alumno)

    return entregas_por_estudiante


# ==========================================
# Punto 3: listado ordenado por aprobadas
# ==========================================
def ranking_aprobaciones(entregas_por_estudiante):
    ranking = []

    for alumno in entregas_por_estudiante:
        aprobadas = entregas_por_estudiante[alumno][1]
        if aprobadas > 0:
            ranking.append((alumno, aprobadas))

    ranking.sort(key=lambda x: x[1], reverse=True)

    print("\nListado de estudiantes por actividades aprobadas:")
    for alumno, aprobadas in ranking:
        print(f"{alumno} - {aprobadas}")


# ==========================================
# Programa principal
# ==========================================
def main():
    archivo = "notas.txt"

    informe_por_semana(archivo)
    entregas = diccionario_estudiantes(archivo)
    ranking_aprobaciones(entregas)


main()

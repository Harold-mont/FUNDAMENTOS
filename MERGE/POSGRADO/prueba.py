'''
En una materia de un posgrado, se aplica evaluación continua.
Esto consiste en pedir la entrega de actividades semanales.
En una semana puede haber ninguna, una o varias actividades.
Los resultados se guardan en los archivos notas_m1.csv, notas_m2.csv,
notas_m3.csv con el siguiente formato:

semana,actividad,apellido_nombre,nota

Ejemplo:
1,cuestionario t1,Gonzalez Carlos,5
1,cuestionario t1,Rodriguez Rosa,8
1,trabajo practico t1,Rodriguez Rosa,10
3,cuestionario t2_3,Gonzalez Carlos,4
...

Sabiendo que los archivos está ordenados por semana y que la aprobación
es con una nota de 4 o superior, se pide realizar un programa modular en
Python que:

1) Recorriendo una sola vez los tres archivos de notas y sin cargarlos
completamente en memoria ni utilizado estructuras auxiliares, obtenga un
único archivo llamado aprobados.csv, ordenado por semana. Ante igualdad
de semana, se deberá informar las de la materia 1 (m1), en primer lugar,
luego los registros de la materia 2 (m2) y finalmente los del archivo 3,
agregando un campo extra: m1, m2 o m3, segun corresponda.
Además, agregar los desaprobados en rec_m1.csv, rec_m2.csv y rec_m3.csv
segun corresponda.
'''


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


def guardar(semana, actividad, alumno, nota, materia, archivo):
    archivo.write(
        str(semana) + ',' +
        actividad + ',' +
        alumno + ',' +
        str(nota) + '\n'
    )


def mezclar(m1, m2, m3, aprobados, rec1, rec2, rec3):
    fila_1, semana_1, actividad_1, alumno_1, nota_1 = leer(m1)
    fila_2, semana_2, actividad_2, alumno_2, nota_2 = leer(m2)
    fila_3, semana_3, actividad_3, alumno_3, nota_3 = leer(m3)

    while not fila_1 or not fila_2 or not fila_3:
        minimo = 9999
        if not fila_1 and semana_1 < minimo:
            minimo = semana_1
        if not fila_2 and semana_2 < minimo:
            minimo = semana_2
        if not fila_3 and semana_3 < minimo:
            minimo = semana_3

        while not fila_1 and semana_1 == minimo:
            if nota_1 >= 4:
                guardar(
                    semana_1, actividad_1, alumno_1, nota_1, "m1", aprobados
                )
            else:
                guardar(
                    semana_1, actividad_1, alumno_1, nota_1, "m1", rec1
                    )
            fila_1, semana_1, actividad_1, alumno_1, nota_1 = leer(m1)
        while not fila_2 and semana_2 == minimo:
            if nota_2 >= 4:
                guardar(
                    semana_2, actividad_2, alumno_2, nota_2, "m2", aprobados
                    )
            else:
                guardar(
                    semana_2, actividad_2, alumno_2, nota_2, "m2", rec2
                    )
            fila_2, semana_2, actividad_2, alumno_2, nota_2 = leer(m2)
        while not fila_3 and semana_3 == minimo:
            if nota_3 >= 4:
                guardar(
                    semana_3, actividad_3, alumno_3, nota_3, "m3", aprobados
                    )
            else:
                guardar(
                    semana_3, actividad_3, alumno_3, nota_3, "m3", rec3
                    )
            fila_3, semana_3, actividad_3, alumno_3, nota_3 = leer(m3)


def main():
    notas_m1 = open('notas_m1.csv', 'r')
    notas_m2 = open('notas_m2.csv', 'r')
    notas_m3 = open('notas_m3.csv', 'r')

    aprobados = open('aprobados.csv', 'w')
    rec_m1 = open('rec_m1.csv', 'w')
    rec_m2 = open('rec_m2.csv', 'w')
    rec_m3 = open('rec_m3.csv', 'w')

    mezclar(notas_m1, notas_m2, notas_m3, aprobados, rec_m1, rec_m2, rec_m3)

    notas_m1.close()
    notas_m2.close()
    notas_m3.close()
    aprobados.close()
    rec_m1.close()
    rec_m2.close()
    rec_m3.close()


main()

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

# ===============================
# LECTURA DE REGISTRO
# ===============================
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



# ===============================
# GUARDAR REGISTRO
# ===============================
def guardar(semana, actividad, alumno, nota, materia, archivo):
    archivo.write(
        str(semana) + "," +
        actividad + "," +
        alumno + "," +
        str(nota) + "," +
        materia + "\n"
    )


# ===============================
# MERGE DE LOS TRES ARCHIVOS
# ===============================
def mezclar(m1, m2, m3, aprobados, rec1, rec2, rec3):

    f1, s1, a1, al1, n1 = leer(m1)
    f2, s2, a2, al2, n2 = leer(m2)
    f3, s3, a3, al3, n3 = leer(m3)

    while not f1 or not f2 or not f3:

        minimo = 9999
        if not f1 and s1 < minimo:
            minimo = s1
        if not f2 and s2 < minimo:
            minimo = s2
        if not f3 and s3 < minimo:
            minimo = s3

        # ===== MATERIA 1 =====
        while not f1 and s1 == minimo:
            if n1 >= 4:
                guardar(s1, a1, al1, n1, "m1", aprobados)
            else:
                guardar(s1, a1, al1, n1, "m1", rec1)
            f1, s1, a1, al1, n1 = leer(m1)

        # ===== MATERIA 2 =====
        while not f2 and s2 == minimo:
            if n2 >= 4:
                guardar(s2, a2, al2, n2, "m2", aprobados)
            else:
                guardar(s2, a2, al2, n2, "m2", rec2)
            f2, s2, a2, al2, n2 = leer(m2)

        # ===== MATERIA 3 =====
        while not f3 and s3 == minimo:
            if n3 >= 4:
                guardar(s3, a3, al3, n3, "m3", aprobados)
            else:
                guardar(s3, a3, al3, n3, "m3", rec3)
            f3, s3, a3, al3, n3 = leer(m3)


# ===============================
# PROGRAMA PRINCIPAL
# ===============================
def main():

    notas_m1 = open("notas_m1.csv", "r")
    notas_m2 = open("notas_m2.csv", "r")
    notas_m3 = open("notas_m3.csv", "r")

    aprobados = open("aprobados.csv", "w")
    rec_m1 = open("rec_m1.csv", "w")
    rec_m2 = open("rec_m2.csv", "w")
    rec_m3 = open("rec_m3.csv", "w")

    mezclar(notas_m1, notas_m2, notas_m3,
            aprobados, rec_m1, rec_m2, rec_m3)

    notas_m1.close()
    notas_m2.close()
    notas_m3.close()
    aprobados.close()
    rec_m1.close()
    rec_m2.close()
    rec_m3.close()


main()

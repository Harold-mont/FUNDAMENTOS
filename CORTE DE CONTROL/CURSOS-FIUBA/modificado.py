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

# ==========================================
# Lee un registro del archivo de inscriptos
# ==========================================
def leer_inscripto(archivo):
    linea = archivo.readline()

    if not linea:
        fin = True
        nro = nivel = trabaja = curso = comision = ""
    else:
        fin = False
        linea = linea.rstrip()
        campos = linea.split(",")

        nro = campos[0]
        nivel = campos[1]
        trabaja = campos[2]
        curso = campos[3]
        comision = campos[4]

    return fin, nro, nivel, trabaja, curso, comision


# ==========================================
# Punto A: informe por curso y comisión
# ==========================================
def informe_cursos(archivo_inscriptos):
    archivo = open(archivo_inscriptos, "r")

    fin, nro, nivel, trabaja, curso, comision = leer_inscripto(archivo)

    total_general = 0
    total_trabajan = 0

    while not fin:
        curso_actual = curso
        total_curso = 0

        print(f"Curso: {curso_actual}")

        while not fin and curso == curso_actual:
            comision_actual = comision
            inscriptos_comision = 0

            while (not fin and
                   curso == curso_actual and
                   comision == comision_actual):

                inscriptos_comision += 1
                total_curso += 1
                total_general += 1

                if trabaja.lower() == "si":
                    total_trabajan += 1

                fin, nro, nivel, trabaja, curso, comision = leer_inscripto(archivo)

            print(f"  Comisión {comision_actual}: {inscriptos_comision} alumnos")

        print(f"  Total inscriptos en {curso_actual}: {total_curso}\n")

    porcentaje_trabajan = (total_trabajan * 100) / total_general if total_general > 0 else 0

    print(f"Total general de inscriptos: {total_general}")
    print(f"Porcentaje que trabaja: {porcentaje_trabajan:.2f}%\n")

    archivo.close()


# ==========================================
# Punto B: diccionario por curso y nivel
# ==========================================
def diccionario_por_curso(archivo_inscriptos):
    dic = {}

    archivo = open(archivo_inscriptos, "r")

    fin, nro, nivel, trabaja, curso, comision = leer_inscripto(archivo)

    while not fin:
        if curso not in dic:
            dic[curso] = [0, 0, 0]  # PRI, SEC, UNI

        if nivel == "PRI":
            dic[curso][0] += 1
        elif nivel == "SEC":
            dic[curso][1] += 1
        elif nivel == "UNI":
            dic[curso][2] += 1

        fin, nro, nivel, trabaja, curso, comision = leer_inscripto(archivo)

    archivo.close()
    return dic


# ==========================================
# Punto C: archivo ordenado usando lambda
# ==========================================
def generar_archivo_ordenado(dic_cursos):
    lista = []

    for curso in dic_cursos:
        pri, sec, uni = dic_cursos[curso]
        total = pri + sec + uni
        lista.append((curso, total, pri, sec, uni))

    # 🔹 Orden con lambda (por total de inscriptos)
    lista.sort(key=lambda x: x[1])

    archivo = open("inscripciones.txt", "w")

    for curso, total, pri, sec, uni in lista:
        linea = f"{curso} - {total} - {pri} - {sec} - {uni}\n"
        archivo.write(linea)

    archivo.close()


# ==========================================
# Programa principal
# ==========================================
def main():
    archivo = "inscriptos_AP40.csv"

    informe_cursos(archivo)
    dic = diccionario_por_curso(archivo)
    generar_archivo_ordenado(dic)


main()

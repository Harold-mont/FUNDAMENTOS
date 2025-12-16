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
def leer(archivo):
    linea = archivo.readline()
    if linea:
        devolver = linea.rstrip('\n').split(',')
    else:
        devolver = '','','','',''
    return devolver

def listar(archivo):
    Nro_Inscripto, Nivel_Educativo, Trabaja_Actualmente, Nombre_Curso, Codigo_Comision = leer(archivo)
    total_alumnos_general = 0
    total_trabajan = 0
    
    while Nro_Inscripto != '':
        Nombre_Curso_Anterior = Nombre_Curso
        total_alumnos_inscriptos = 0
        print(f'Curso: {Nombre_Curso_Anterior}')
        
        while Nro_Inscripto != '' and Nombre_Curso_Anterior == Nombre_Curso:  
            Codigo_Comision_Anterior = Codigo_Comision
            cantidad_alumnos_inscriptos = 0
            print(f'Comision: {Codigo_Comision_Anterior}')
            
            while Nro_Inscripto != '' and Nombre_Curso_Anterior == Nombre_Curso and Codigo_Comision_Anterior == Codigo_Comision:     
                cantidad_alumnos_inscriptos += 1
                if Trabaja_Actualmente == 'si':
                    total_trabajan += 1
                
                Nro_Inscripto, Nivel_Educativo, Trabaja_Actualmente, Nombre_Curso, Codigo_Comision = leer(archivo)
            print(f'Tiene {cantidad_alumnos_inscriptos} alumnos inscriptos')
            total_alumnos_inscriptos += cantidad_alumnos_inscriptos
            
        print(f'El curso {Nombre_Curso_Anterior} tiene {total_alumnos_inscriptos} alumnos inscriptos\n')
        total_alumnos_general += total_alumnos_inscriptos
        
    print(f'Total de alumnos: {total_alumnos_general}')
    
    porcentaje_trabajan = (total_trabajan / total_alumnos_general) * 100
    print(f'Porcentaje de alumnos que trabajan : {porcentaje_trabajan}\n')

def diccionario(archivo):
    Nro_Inscripto, Nivel_Educativo, Trabaja_Actualmente, Nombre_Curso, Codigo_Comision = leer(archivo)
    diccionario = {}
    
    while Nro_Inscripto != '':        
        if Nombre_Curso not in diccionario:
            diccionario[Nombre_Curso] = [0, 0, 0]
        
        Nombre_Curso_Anterior = Nombre_Curso
        while Nro_Inscripto != '' and Nombre_Curso_Anterior == Nombre_Curso:
            if Nivel_Educativo == 'PRI':
                diccionario[Nombre_Curso_Anterior][0] += 1
            elif Nivel_Educativo == 'SEC':
                diccionario[Nombre_Curso_Anterior][1] += 1
            elif Nivel_Educativo == 'UNI':
                diccionario[Nombre_Curso_Anterior][2] += 1

            Nro_Inscripto, Nivel_Educativo, Trabaja_Actualmente, Nombre_Curso, Codigo_Comision = leer(archivo)        
    return diccionario

def escribir(curso, inscriptos, est_prim, est_sec, est_uni, archivo):
    archivo.write(curso + '-' + str(inscriptos) + '-' + str(est_prim) + '-' + str(est_sec) + '-' + str(est_uni) + '\n')

def listado_ordenado(diccionario, archivo):
    dicc_ordenado = sorted(diccionario.items(), key = lambda x : sum(x[1]))
    
    for item in dicc_ordenado:
        curso = item[0]
        est_prim = item[1][0]
        est_sec = item[1][1]
        est_uni = item[1][2]
        total_insc = est_prim + est_sec + est_uni
        
        escribir(curso, total_insc, est_prim, est_sec, est_uni, archivo)

def main():
    archivo_inscriptos = open('./2DO-PARCIAL/parcial2/inscriptos_AP40.csv', 'r')
    listar(archivo_inscriptos)
    archivo_inscriptos.close()
    
    archivo_inscriptos2 = open('./2DO-PARCIAL/parcial2/inscriptos_AP40.csv', 'r')
    dicc_cursos = diccionario(archivo_inscriptos2)
    archivo_inscriptos2.close()
    
    archivo_txt = open('./2DO-PARCIAL/parcial2/inscripciones.txt', 'w')
    listado_ordenado(dicc_cursos, archivo_txt)
    archivo_txt.close()
    
main()
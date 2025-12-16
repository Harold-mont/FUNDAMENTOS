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
MAX = 50

def leer(arch, campos):
    linea = arch.readline()    
    if campos == 5:
        if linea:
            devolver = linea.rstrip('\n').split(',')
        else:
            devolver = MAX,'','','',''
    elif campos == 6:
        if linea:
            devolver = linea.rstrip('\n').split(',')
        else:
            devolver = MAX,'','','','',''
    return devolver

def guardar(dia, equipo_local, goles_local, equipo_visitante, goles_visitante, torneo, arch):
    arch.write(str(dia) + ',' + equipo_local + ',' + goles_local + ',' + equipo_visitante + ',' + goles_visitante + ',' + torneo + '\n')

def mezclar(arch1, arch2, arch_unificado):
    dia1, equipo_local1, goles_local1, equipo_visitante1, goles_visitante1 = leer(arch1, 5)
    dia2, equipo_local2, goles_local2, equipo_visitante2, goles_visitante2 = leer(arch2, 5)
    dia1 = int(dia1)
    dia2 = int(dia2)
    
    while dia1 < MAX or dia2 < MAX:
        minimo = min(dia1, dia2)
        while dia1 == minimo:
            guardar(dia1, equipo_local1, goles_local1, equipo_visitante1, goles_visitante1, 'EUROCOPA', arch_unificado)
            dia1, equipo_local1, goles_local1, equipo_visitante1, goles_visitante1 = leer(arch1, 5)
            dia1 = int(dia1)
        while dia2 == minimo:
            guardar(dia2, equipo_local2, goles_local2, equipo_visitante2, goles_visitante2, 'COPA_AMERICA', arch_unificado)
            dia2, equipo_local2, goles_local2, equipo_visitante2, goles_visitante2 = leer(arch2, 5)
            dia2 = int(dia2)
    return

def diccionario(arch_unif):
    dia, equipo_local, goles_local, equipo_visitante, goles_visitante, torneo = leer(arch_unif, 6)
    diccionario = {}
    
    while (int(dia) < MAX):        
        goles_local = int(goles_local)
        goles_visitante = int(goles_visitante)
        
        if equipo_local not in diccionario:
            diccionario[equipo_local] = [0, 0, 0]
        
        if equipo_visitante not in diccionario:
            diccionario[equipo_visitante] = [0, 0, 0]
        
        if goles_local > goles_visitante:
            diccionario[equipo_local][0] += 1
            diccionario[equipo_visitante][2] += 1
        
        elif goles_local < goles_visitante:
            diccionario[equipo_local][2] += 1
            diccionario[equipo_visitante][0] +=1
        
        else:
            diccionario[equipo_local][1] +=1
            diccionario[equipo_visitante][1] +=1
        
        dia, equipo_local, goles_local, equipo_visitante, goles_visitante, torneo = leer(arch_unif, 6)
    
    return diccionario

def mostrar_listado(datos):
    listado_ordenado = sorted(datos.items(), key = lambda x : x[1][0], reverse = True)
    
    for item in listado_ordenado:
        partidos_ganados = item[1][0]
        pais = item[0]
        if int(partidos_ganados) > 0:
            print(f'Pais: {pais} - Partidos ganados: {partidos_ganados}')

def main ():
    arch1 = open('./parcial1/eurocopa.csv', 'r')
    arch2 = open('./parcial1/copa_america.csv', 'r')
    
    arch_unificado = open('./parcial1/unificado.csv', 'w')
    mezclar(arch1, arch2, arch_unificado)
    arch_unificado.close()
    arch1.close()
    arch2.close()
    
    arch_unificado2 = open('./parcial1/unificado.csv', 'r')
    resultado = diccionario(arch_unificado2)
    arch_unificado2.close()
        
    mostrar_listado(resultado)

main()
'''
La ferretería Fede Reía tiene dos sucursales y por cada una guarda un registro diario de cada venta realizada. 
Este registro se cierra mensualmente en un archivo CSV (ventas1.csv y ventas2.csv), por lo que queda ordenado por día, con el siguiente formato:

dia,codigo_producto,cantidad_vendida

Ejemplo:
1,176,12
1,45,1

Además, se cuenta con un diccionario reposicion, ya cargado, con los códigos de artículos como clave y una lista con dos valores: 
la descripción del artículo y el nivel de ventas de cada artículo para solicitar reposición. 
Por ejemplo, si del artículo 45 se vendieron 3 unidades y el nivel de reposición es 10, no hay que solicitar ninguna reposición. 
En cambio, si se vendieron 13 unidades, hay que reponer solo 3 (la resta de la cantidad vendida menos el nivel de reposición).

Si aceptas la misión, deberás realizar un programa en Python que:

1)	Recorriendo una sola vez los archivos de ventas y sin cargarlos completamente en memoria, haga un merge de ambos archivos, 
agregando en cada línea SUC_1 o SUC_2, dependiendo de dónde proviene la información. Este archivo unificado, debe estar ordenado por día, 
y ante igualdad de día, en primer lugar, deben estar las ventas de la sucursal 1.

2)	Genere un diccionario con el código de artículo como clave y la cantidad vendida. Para este punto hay que leer el archivo unificado 
generado en el punto 1, no hacerlo en forma conjunta.

3)	En base al diccionario generado en el punto 2 y el diccionario reposicion, armar un listado, ordenado de mayor a menor por cantidad de
unidades a reponer, indicando: descripción del artículo, unidades a reponer. En este listado no deben figurar los artículos que no hay que reponer.
'''
MAX = 50

def leer(archivo, campos):
    linea = archivo.readline()
    if linea:
        devolver = linea.rstrip('\n').split(',')
    else:
        devolver = [MAX] + [''] * (campos - 1)
    return devolver

def escribir(dia, codigo, cantidad, sucursal, archivo):
    archivo.write(str(dia) + ',' + codigo + ',' + cantidad + ',' + sucursal + '\n')

def merge(archivo1, archivo2, archivo3):
    dia1, codigo_producto1, cantidad_vendida1 = leer(archivo1, 3)
    dia2, codigo_producto2, cantidad_vendida2 = leer(archivo2, 3)
    dia1 = int(dia1)
    dia2 = int(dia2)
    
    while dia1 < MAX or dia2 < MAX:
        minimo = min(dia1, dia2)
        while dia1 == minimo:
            escribir(dia1, codigo_producto1, cantidad_vendida1, 'SUC_1', archivo3)
            dia1, codigo_producto1, cantidad_vendida1 = leer(archivo1, 3)
            dia1 = int(dia1)
        while dia2 == minimo:
            escribir(dia2, codigo_producto2, cantidad_vendida2, 'SUC_2', archivo3)
            dia2, codigo_producto2, cantidad_vendida2 = leer(archivo2, 3)
            dia2 = int(dia2)

def diccionario(archivo):
    dia, codigo_producto, cantidad_vendida, sucursal = leer(archivo, 4)
    dia = int(dia)
    diccionario = {}
    
    while dia < MAX:
        diccionario[codigo_producto] = cantidad_vendida
        dia, codigo_producto, cantidad_vendida, sucursal = leer(archivo, 4)
        dia = int(dia)
    return diccionario

def listado(diccionario, dicc_reposicion):
    dicc_final = {}
    
    for item in dicc_reposicion.items():
        nivel_ventas = item[1][1]
        descripcion = item[1][0]
        codigo = str(item[0])
        
        if codigo in diccionario:
            cantidad = int(diccionario[codigo])
        
            if cantidad > nivel_ventas:
                reponer = cantidad - nivel_ventas
                dicc_final[descripcion] = reponer
    
    dicc_ordenado = sorted(dicc_final.items(), key = lambda x: x[1], reverse = True)
    print(dicc_ordenado)

def main():
    archivo1 = open('./Parciales(2do)/parcial1/ventas1.csv')
    archivo2 = open('./Parciales(2do)/parcial1/ventas2.csv')
    archivo3 = open('./Parciales(2do)/parcial1/unificado.csv', 'w')
    merge(archivo1, archivo2, archivo3)
    archivo1.close()
    archivo2.close()
    archivo3.close()
    
    archivo4 = open('./Parciales(2do)/parcial1/unificado.csv')
    resultado = diccionario(archivo4)
    archivo4.close()
    print(resultado)
    
    diccionario_reposicion = {176: ['descripcion 176', 10], 45: ['descripcion 45', 4], 90: ['descripcion 90', 2], 34: ['descripcion 34', 1]}
    listado(resultado, diccionario_reposicion)

main()
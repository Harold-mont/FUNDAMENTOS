'''
La ferretería Fede Reía, que ya es cliente habitual, te pide un encargo más. En el archivo ventas.csv tiene registradas todas las ventas del mes, 
con el siguiente formato:

dia,id_articulo,cantidad,precio_unitario

Ejemplo:
1,45,20,1.32
1,130,1,10.05
1,45,12,1.32
2,160,50,0.80

Este archivo se encuentra ordenado por día.
Te piden realizar un programa en Python, compuesto por funciones y que respete las prácticas y conceptos vistos en clase; que cumpla con los siguientes 
requerimientos:

1)	Recorriendo una sola vez el archivo de ventas, sin cargarlo por completo en estructuras adicionales, como listas o diccionarios, hagas un Corte de 
Control por día. La aplicación deberá imprimir un total diario y un total general cuando termine de recorrer el archivo.

2)	Mientras recorrés el archivo del punto anterior, tenés que generar un diccionario con los identificadores de los artículos y el monto recaudado en 
el mes para cada uno.
3)	En base al diccionario generado en el punto anterior, imprimir un informe indicando: código de artículo, monto recaudado, ordenado por este último
campo de mayor a menor.
'''
MAX_DIA = 50
def leer(archivo):
    linea = archivo.readline()
    if linea:
        devolver = linea.rstrip('\n').split(',')
    else:
        devolver = MAX_DIA,'','',''
    return devolver

def listar(archivo):
    dia, id_articulo, cantidad, precio_unitario = leer(archivo)
    dia = int(dia)
    total_general = 0
    diccionario = {}
    
    while dia < MAX_DIA:
        
        dia_anterior = dia
        total_diario = 0
        print(f'Dia: {dia_anterior}')
        
        while dia < MAX_DIA and dia_anterior == dia:
            
            monto_actual = int(cantidad) * float(precio_unitario)
            total_diario += monto_actual
            
            if id_articulo not in diccionario:
                diccionario[id_articulo] = 0
            
            diccionario[id_articulo] += monto_actual
            
            dia, id_articulo, cantidad, precio_unitario = leer(archivo)
            dia = int(dia)
            
        print(f'Total: {total_diario}\n')
        total_general += total_diario
        
    print(f'Total general: {total_general}')
    return diccionario

def mostrar_informe(diccionario):
    dicc_ordenado = sorted(diccionario.items(), key = lambda x: x[1], reverse = True)
    
    for item in dicc_ordenado:
        codigo = item[0]
        monto = item[1]
        print(f'Codigo de articulo: {codigo}, Monto recaudado: {monto}.')

def main():
    archivo_ventas = open('./Parciales(2do)/parcial2/ventas.csv')
    diccionario = listar(archivo_ventas)
    archivo_ventas.close()
    
    mostrar_informe(diccionario)
    
main()
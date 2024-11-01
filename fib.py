#!/usr/bin/python3

# Calcula fibonacci de un termino a otro pasado por parametros en terminal
# será mas eficiente con cada ejecucion al guardar resultados previos en archivo

import sys

# Definicion de funciones
def contar_lineas(archivo:str) -> int:
    '''
        Cuenta cuantas lineas tiene un archivo.
    '''
    # Abro el archivo pasado por parametro en modo lectura
    arch = open(str(archivo), 'r')
    # Cuento lineas
    lineas = arch.readlines().__len__()
    # Cierro el archivo para poder usarlo mas adelante
    arch.close()
    # Devuelvo Cantidad de lineas
    return lineas

def guardar(valor:str, archivo:str):
    '''
        Guarda en una linea nueva determinado valor de
        texto sin borrar lo que ya habia antes.
    '''
    # Abro archivo pasado por parametro en modo escritura aditiva
    arch = open(str(archivo), 'a')
    # Agrego valor y su respectiva nueva linea
    arch.write(str(valor) + '\n')
    # Cierro el archivo para que siga accesible
    arch.close()

def esta(valor:str, archivo:str) -> bool:
    '''
        Dice si un valor está en alguna linea del archivo
    '''
    # Abro archivo en modo lectura
    arch = open(str(archivo), 'r')
    # Recorro lineas hasta encontrar una coincidencia, si la hay para cambiar estado

    estado = False

    for linea in arch.readlines():
        # La coincidencia debe ser exacta para este script
        if (linea.replace('\n', '') == str(valor)):
            # Cambio estado a verdadero porque encontre dicho valor en una linea
            estado = True
            # Corto bucle porque ya encontre lo que buscaba para no perder velocidad
            break
    # Cierro el archivo porque termine y se pueda usar luego
    arch.close()

def linea(n:int, archivo:str):
    '''
        Devuelve valor que hay en la linea n de un archivo.
    '''
    # Abro archivo en modo lectura
    arch = open(str(archivo), 'r')
    # Gurado contenido de linea n sin nueva linea
    linea = arch.readlines()[(n - 1)].replace('\n', '')
    # Cierro el archivo para usarlo despues
    arch.close()
    # Devuelvo contenido en linea n del archivo
    return linea

def fib(n:int, archivo_terminos:str) -> int:
    '''
        Calcula fibonacci de forma optima:
            Si es termino dentro de lineas de archivo lo muestro,
            sino calculo sumando lineas anteriores.
    '''
    if (n <= contar_lineas(str(archivo_terminos))):
        # Si es conocido simplemente lo uso (Cada linea un termino)
            return int(linea(n, archivo_terminos))
    else:
        # Si es desconocido (fuera de las lineas de terminos conocidos), sumo hasta llegar a ultimas lineas conocidas
            return fib((n - 2), str(archivo_terminos)) + fib((n - 1), str(archivo_terminos))
# Algoritmo principal
# Digo cuantas lineas hay ahora
print(f'\nHasta ahora se conocen {contar_lineas("terminos.txt")} terminos de fibonacci:\n')
# Nota: es aconsejable arrancar siempre desde siguiente a último termino conocido
# N inicial desde donde calcular terminos de fibonacci
inicio = int(sys.argv[1])
# N final hasta que termino de fibonacci calcular
fin = (int(sys.argv[2]) + 1)
# Nombre de archivo con los terminos de fibonacci, uno en cada linea
nombre_archivo = str(sys.argv[3])
# Bucle que recorre ese intervalo de terminos de fibonacci a calcular
for termino in range(inicio, fin):
    # Guardo temporalmente el termino para calcular una vez y no tres
    resultado = fib(termino, nombre_archivo)
    # Muestro que termino estoy calculando y cuanto es en fibonacci
    print(f'\n\tfib({termino}) = {resultado}')
    # Guardo nuevo termino si no estaba antes en el archivo
    if contar_lineas(nombre_archivo) < termino:
        guardar(resultado, nombre_archivo)
# Digo cuantos terminos hay ahora
print(f'\nAhora se conocen {contar_lineas("terminos.txt")} terminos de fibonacci.\n')

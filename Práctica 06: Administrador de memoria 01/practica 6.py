# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:35:41 2024

@author: Usuario
"""

def primer_ajuste(files, memory_blocks):
    asignaciones = []
    for file, size in files.items():
        asignado = False
        for i in range(len(memory_blocks)):
            if memory_blocks[i] >= size:
                asignaciones.append((file, size, memory_blocks[i]))
                memory_blocks[i] -= size
                asignado = True
                break
        if not asignado:
            asignaciones.append((file, size, None))
    return asignaciones

def mejor_ajuste(files, memory_blocks):
    asignaciones = []
    for file, size in files.items():
        mejor_bloque = -1
        for i in range(len(memory_blocks)):
            if memory_blocks[i] >= size:
                if mejor_bloque == -1 or memory_blocks[i] < memory_blocks[mejor_bloque]:
                    mejor_bloque = i
        if mejor_bloque != -1:
            asignaciones.append((file, size, memory_blocks[mejor_bloque]))
            memory_blocks[mejor_bloque] -= size
        else:
            asignaciones.append((file, size, None))
    return asignaciones

def peor_ajuste(files, memory_blocks):
    asignaciones = []
    for file, size in files.items():
        peor_bloque = -1
        for i in range(len(memory_blocks)):
            if memory_blocks[i] >= size:
                if peor_bloque == -1 or memory_blocks[i] > memory_blocks[peor_bloque]:
                    peor_bloque = i
        if peor_bloque != -1:
            asignaciones.append((file, size, memory_blocks[peor_bloque]))
            memory_blocks[peor_bloque] -= size
        else:
            asignaciones.append((file, size, None))
    return asignaciones

def siguiente_ajuste(files, memory_blocks):
    asignaciones = []
    ultima_posicion = 0
    for file, size in files.items():
        asignado = False
        for i in range(ultima_posicion, len(memory_blocks)):
            if memory_blocks[i] >= size:
                asignaciones.append((file, size, memory_blocks[i]))
                memory_blocks[i] -= size
                ultima_posicion = i + 1
                asignado = True
                break
        
        if not asignado:
            for i in range(0, ultima_posicion):
                if memory_blocks[i] >= size:
                    asignaciones.append((file, size, memory_blocks[i]))
                    memory_blocks[i] -= size
                    ultima_posicion = i + 1
                    asignado = True
                    break
        
        if not asignado:
            asignaciones.append((file, size, None))
    
    return asignaciones

def mostrar_asignaciones(asignaciones):
    for archivo, peso, bloque in asignaciones:
        if bloque is not None:
            print(f"El archivo {archivo} de {peso}kb fue asignado a un bloque de {bloque}kb.")
        else:
            print(f"El archivo {archivo} de {peso}kb no pudo ser asignado a ningún bloque.")
            
files = {
    "hola_mundo.py": 500,
    "lista_de_compras.txt": 950,
    "resumen.docx": 1200,
    "persona.h": 350,
    "reporte.xlsx": 2000
}
while True:
    print("\nadministración de memoria")
    
    print("\nEspacios de memoria disponibles (en kb): [1000, 400, 1800, 900, 2000, 1200, 1500, 700]")
    print("Archivos a guardar:")
    for archivo, peso in files.items():
        print(f"- {archivo}: {peso}kb")
    
    bloques_disponibles = [1000, 400, 1800, 900, 2000, 1200, 1500, 700]
    

    while True:
        print("\nElije el algoritmo:")
        print("1. Primer ajuste")
        print("2. Mejor ajuste")
        print("3. Peor ajuste")
        print("4. Siguiente ajuste")
        eleccion = input("Ingresa el número del algoritmo (1-4): ")
        
        if eleccion in ['1', '2', '3', '4']:
            break
        else:
            print("Entrada no valida, ingresa un numero entre 1 y 4.")
    
    if eleccion == '1':
        resultado = primer_ajuste(files, bloques_disponibles)
    elif eleccion == '2':
        resultado = mejor_ajuste(files, bloques_disponibles)
    elif eleccion == '3':
        resultado = peor_ajuste(files, bloques_disponibles)
    elif eleccion == '4':
        resultado = siguiente_ajuste(files, bloques_disponibles)
    
    print("\n Resultados de la asignación de memoria")
    mostrar_asignaciones(resultado)
    
    while True:
        repetir = input("\n¿Deseas intentar de nuevo con otro algoritmo? (s/n): ").lower()
        if repetir in ['s', 'n']:
            break
        else:
            print("ingresa 's' para sí o 'n' para no.")
    
    if repetir == 'n':
        print("\nCerrando el programa")
        break 

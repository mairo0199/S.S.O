# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 22:44:24 2024

@author: Usuario
"""

import os

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

def agregar_bloque_memoria(memory_blocks):
    while True:
        try:
            tamano = int(input("Ingrese el tamaño del bloque de memoria (en kb): "))
            estado = input("Ingrese el estado (Disponible/Ocupado): ").lower()
            posicion = input("Ingrese la posición (Inicio/Final): ").lower()
            
            if estado == "disponible":
                if posicion == "inicio":
                    memory_blocks.insert(0, tamano)
                else:
                    memory_blocks.append(tamano)
            else:
                print("Solo se pueden agregar bloques en estado Disponible.")
            break
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")

def agregar_archivo(files):
    while True:
        try:
            nombre = input("Ingrese el nombre del archivo: ")
            tamano = int(input("Ingrese el tamaño del archivo (en kb): "))
            posicion = input("Ingrese la posición (Inicio/Final): ").lower()
            
            if posicion == "inicio":
                files = {nombre: tamano, **files}
            else:
                files[nombre] = tamano
            break
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")
    return files

files = {
    "hola_mundo.py": 500,
    "lista_de_compras.txt": 950,
    "resumen.docx": 1200,
    "persona.h": 350,
    "reporte.xlsx": 2000
}
memory_blocks = [1000, 400, 1800, 900, 2000, 1200, 1500, 700]

while True:
    print("\n--- Simulación de administración de memoria ---")
    print("Espacios de memoria disponibles (en kb):", memory_blocks)
    print("Archivos a guardar:")
    for archivo, peso in files.items():
        print(f"- {archivo}: {peso}kb")
    
    while True:
        opcion = input("\n¿Desea agregar un bloque de memoria o un archivo? (bloque/archivo/ninguno)(ingresa solo la inicial): ").lower()
        if opcion == "b":
            agregar_bloque_memoria(memory_blocks)
        elif opcion == "a":
            files = agregar_archivo(files)
        elif opcion == "n":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
    
    while True:
        print("\nElija el algoritmo de administración de memoria:")
        print("1. Primer ajuste")
        print("2. Mejor ajuste")
        print("3. Peor ajuste")
        print("4. Siguiente ajuste")
        eleccion = input("Ingrese el número del algoritmo (1-4): ")
        
        if eleccion in ['1', '2', '3', '4']:
            break
        else:
            print("Entrada no válida. Por favor, ingrese un número entre 1 y 4.")
    
    bloques_disponibles = memory_blocks.copy()  # Copiamos la lista original para no alterarla
    if eleccion == '1':
        resultado = primer_ajuste(files, bloques_disponibles)
    elif eleccion == '2':
        resultado = mejor_ajuste(files, bloques_disponibles)
    elif eleccion == '3':
        resultado = peor_ajuste(files, bloques_disponibles)
    elif eleccion == '4':
        resultado = siguiente_ajuste(files, bloques_disponibles)
    
    print("\n--- Resultados de la asignación de memoria ---")
    mostrar_asignaciones(resultado)
    
    repetir = input("\n¿Desea intentar de nuevo con otro algoritmo o nuevas configuraciones? (s/n): ").lower()
    if repetir != 's':
        print("\nCerrando el programa")
        break

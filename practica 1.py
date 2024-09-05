# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 22:09:42 2024

@author: Usuario
"""
import os

# Esto convierte un el número hexadecimal a decimal
def hex_dec(hex_str):
    return int(hex_str, 16)

# convierte decimal a hexadecimal
def dato_hex(dato_str):
# Convertir cada dato en su equivalente hexadecimal
    return '.'.join([format(int(dat), 'X') for dat in dato_str.split('.')])

# procesa linea del archivo de entrada
def procesa_linea(linea):
    partes = linea.strip().split(',')
    
    # Obtiene la primera parte de números hexadecimales
    hex_numeros = partes[0].split(':')
    
    # Elimina cualquier caracter que no sea parte del número hexadecimal
    hex_numeros = [num.split('/')[0] for num in hex_numeros]
    
    # Extrae la segunda cadena (nombre o texto)
    segundo_string = partes[2].strip()
    
    # Extrae los ultimos datos
    ulti_datos = partes[-1].strip()

    # Convierte los números hexadecimales a decimales
    dec_numeros = [hex_dec(num) for num in hex_numeros]
    
    # Convierte los ultimos datos a hexadecimal
    hex_ulda = dato_hex(ulti_datos)

    # Devuelve el formato final: segunda cadena, números en decimal y ultimos datos en hexadecimal
    return f"{segundo_string} : {' : '.join(map(str, dec_numeros))} : {hex_ulda}"

# Rutas de los archivos de entrada y salida
input_file = 'C:/Users/Usuario/Desktop/Universidad/S.S.O/prueba2.txt'
output_file = 'C:/Users/Usuario/Desktop/Universidad/S.S.O/resultado.txt'

# Verifica si el archivo de entrada existe
if os.path.exists(input_file):
    # Abrre el archivo de entrada para lectura y el archivo de salida para escritura
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Lee y procesa cada línea del archivo de entrada
        for line in infile:
            processed_line = procesa_linea(line)
            # Escribe la línea procesada en el archivo de salida
            outfile.write(processed_line + '\n')
    # Indica que el procesamiento ha sido completado
    print("Completado. Revisa el archivo de salida.")
else:
    # Muestra mensaje de error si el archivo de entrada no existe
    print(f"El archivo {input_file} no se encuentra en la ruta especificada.")








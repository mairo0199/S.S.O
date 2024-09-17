# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:47:22 2024

@author: Usuario
"""

import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

extension = ['.bat']

def eliminar(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if any(file.endswith(ext) for ext in extension):
                print(f"Eliminando archivo maligno: {file_path}")
                os.remove(file_path)

class monitorear(FileSystemEventHandler):
    def creado(self, event):
        if not event.is_directory:
            file_path = event.src_path
            # Si el archivo recién creado tiene una extensión maligna, se elimina
            if any(file_path.endswith(ext) for ext in extension):
                print(f"Archivo maligno detectado y eliminado: {file_path}")
                os.remove(file_path)

    def modificado(self, event):
        if not event.is_directory:
            file_path = event.src_path
            # Si el archivo modificado tiene una extensión maligna, se elimina
            if any(file_path.endswith(ext) for ext in extension):
                print(f"Archivo maligno modificado detectado y eliminado: {file_path}")
                os.remove(file_path)

# Función principal para monitorear la carpeta
def monitorear_carpeta(carpeta):
    event_handler = monitorear()
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=True)
    observer.start()

    try:
        while True:
            eliminar(carpeta)
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    folder_path = input("Ingresar la ruta de la carpeta a monitorear: ")
    if os.path.isdir(folder_path):
        print(f"Monitoreando la carpeta: {folder_path}")
        monitorear_carpeta(folder_path)
    else:
        print("La ruta ingresada no es válida.")

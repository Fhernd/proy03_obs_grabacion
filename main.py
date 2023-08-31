import os
import sys
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from util import es_nombre_valido, renombrar_archivo


class GestorGrabacionObs(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        
        nombre_inicial = event.src_path
        
        print(f'Archivo modificado: {nombre_inicial}')
        
        root = tk.Tk()
        root.withdraw()
        
        nombre_archivo = os.path.basename(nombre_inicial)
        
        while True:
            nuevo_nombre = simpledialog.askstring("Input", "Introduce el nuevo nombre del archivo:", initialvalue=nombre_archivo)
            
            if nuevo_nombre is None:
                break
            
            if len(nuevo_nombre):
                
                if es_nombre_valido(nuevo_nombre):
                    if renombrar_archivo(event.src_path, nuevo_nombre):
                        simpledialog.messagebox.showinfo('Información', f'Archivo renombrado correctamente: {nuevo_nombre}')
                        
                        break
                    else:
                        messagebox.showwarning('Advertencia', f'No se pudo renombrar el archivo: {nuevo_nombre}')
                else:
                    messagebox.showwarning('Advertencia', f'Nombre de archivo inválido: {nuevo_nombre}')
            else:
                messagebox.showwarning('Advertencia', f'Nombre de archivo inválido: {nuevo_nombre}')
                    
        root.destroy()

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    event_handler = GestorGrabacionObs()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

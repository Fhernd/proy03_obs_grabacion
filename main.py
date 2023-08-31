import sys
import time
import tkinter as tk
from tkinter import simpledialog

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from util import es_nombre_valido


class GestorGrabacionObs(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        
        nombre_inicial = event.src_path
        
        print(f'Archivo modificado: {nombre_inicial}')
        
        root = tk.Tk()
        root.withdraw()
        
        nombre_archivo = nombre_inicial.split('/')[-1]
        
        nuevo_nombre = simpledialog.askstring("Input", "Introduce el nuevo nombre del archivo:", initialvalue=nombre_inicial)
        
        root.destroy()
        
        if nuevo_nombre and len(nuevo_nombre):
            
            if es_nombre_valido(nuevo_nombre):
                pass
            


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

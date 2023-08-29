import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        # Se detectó un cambio en un archivo o carpeta
        if event.is_directory:
            return
        print(f'Archivo modificado: {event.src_path}')

    def on_created(self, event):
        # Se detectó la creación de un nuevo archivo o carpeta
        if event.is_directory:
            return
        print(f'Archivo creado: {event.src_path}')

    def on_deleted(self, event):
        # Se detectó la eliminación de un archivo o carpeta
        if event.is_directory:
            return
        print(f'Archivo eliminado: {event.src_path}')

    # Puedes añadir más métodos para manejar otros tipos de eventos, como on_moved.

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'  # Monitorea el directorio actual como predeterminado
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

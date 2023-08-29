import sys
import time
import tkinter as tk
from tkinter import simpledialog

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class GestorGrabacionObs(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        
        print(f'Archivo modificado: {event.src_path}')


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

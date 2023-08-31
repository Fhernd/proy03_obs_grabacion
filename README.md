# 1. Introducción

Con este script de Python podemos mostrar un diálogo para escribir el nombre de archivo de una grabación de OBS Studio. Al finalizar la grabación no se muestra ningún diálogo; es el comportamiento nativo de OBS Studio. Lo que se busca consiste en automatizar el renombrado del archivo: el usuario únicamente escribe el nombre del archivo como tal.

# 2. Instalación

## 2.1. Requisitos

- Python 3.8 o superior
- OBS Studio
- Librería watchdog

## 2.2 Creación de un entorno virtual

Para crear un entorno virtual, ejecuta el siguiente comando:

```bash
python -m venv venv
```

## 2.3. Activación del entorno virtual

Para activar el entorno virtual, ejecuta el siguiente comando:

Linux/macOS:
```bash
source venv/bin/activate
```

Windows:
```bash
venv\Scripts\activate.bat
```

## 2.4. Instalación de dependencias

Para instalar las dependencias, ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

# 3. Uso

Para ejecutar el script, ejecuta el siguiente comando:

```bash
python main.py [ruta de la carpeta de grabación]
```

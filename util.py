import re


def es_nombre_valido(nombre_archivo):
    """
    Valida si el nombre de archivo es válido.
    
    Args:
        nombre_archivo (str): Nombre de archivo a validar.
    
    Returns:
        bool: True si el nombre de archivo es válido, False en caso contrario.
    """
    invalid_chars = r'[\\/:*?"<>|]'
    if re.search(invalid_chars, nombre_archivo):
        return False

    if any(char < ' ' for char in nombre_archivo):
        return False

    reserved_names = ["CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", 
                      "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", 
                      "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"]
    
    name_without_extension = nombre_archivo.split('.')[0].upper()
    if name_without_extension in reserved_names:
        return False

    if len(nombre_archivo) >= 255:
        return False

    return True

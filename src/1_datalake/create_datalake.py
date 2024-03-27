"""create datalake in the main directory"""

import os

import pkg_resources

STRUCTURE_FILE = "datalake_structure.txt"


def get_datalake_dirs():  ##funcion que lee el archivo de la estructura, esta ubicado donde esta el programa principal
    """Returns the datalake directories stored in the file structure.txt"""

    if not pkg_resources.resource_exists(__name__, STRUCTURE_FILE):
        raise FileNotFoundError(f"File {STRUCTURE_FILE} not found")

    with pkg_resources.resource_stream(__name__, STRUCTURE_FILE) as f:
        dirs = f.readlines()
        dirs = [dir.strip() for dir in dirs]
    return dirs  ##lee el contenido de datalake 1 por fila y lo devuelve como strings


def create_datalake(dirs):  ## iterar sobre la lista de strings y crear la carpeta
    """Creates datalake in the main directory"""

    for path in dirs:
        if not os.path.exists(path):
            os.makedirs(path)


def main():  ##las funciones llaman funciones.
    """Orchestrates the creation of the datalake"""

    dirs = get_datalake_dirs()
    create_datalake(dirs)


if __name__ == "__main__":
    main()

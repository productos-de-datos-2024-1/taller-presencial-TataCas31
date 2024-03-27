"""Create a datalake in the main directory"""

import os

import pkg_resources

STRUCTURE_FILE = "datalake_structure.txt"


if not pkg_resources.resource_exists(__name__, STRUCTURE_FILE):
    raise FileNotFoundError(f"File {STRUCTURE_FILE} not found")

with pkg_resources.resource_stream(__name__, STRUCTURE_FILE) as f:
    dirs = f.readlines()
    dirs = [dir.strip() for dir in dirs]


for path in dirs:
    if not os.path.exists(path):
        os.makedirs(path)

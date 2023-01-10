import os

def installModules(file):
    os.system(f'pip install -r {file}')
    return print(f'Successful! Installed modules from {file}')

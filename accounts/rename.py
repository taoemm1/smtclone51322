import glob
import os

identificador = 0


lista_fotos = sorted(glob.glob( '*.json'))

for i in lista_fotos:   
    nuevo_nombre = str(identificador).zfill(1) + '.json'        
    identificador = identificador + 1
    os.rename(i, nuevo_nombre)

##THIS FILE ONLY RUN PYTHON 3
import  glob
import os.path
from pathlib import Path
import re
def concat(basefile):#no modificar esta parte del codigo a menos que estes seguro....
    if Path(basefile+"/complete.bin").exists():
        print("ERROR CAMBIA EL NOMBRE A complete.bin para evitar errores")
        exit(0)
    objetivo = open(basefile+"/complete.bin","wb")
    original = []
    concatenadores = []
    for archivo in glob.glob(basefile+"/*.*"):
        target = os.path.basename(archivo)

        if target == "complete.bin":
            continue
        m = re.compile("([0-9]+)\\.tmp")
        if m.match(target) :
            concatenadores.append(m.search(target).group(1))
        else:
            original.append(target)
    if not concatenadores or not original:
        print("VERIFICA EL ARCHIVO ORIGIANL Y LOS TEMPORALES QUE EMPIEZACON CON NUMEROS Y EXTENSION .tmp")
        exit(0)
    concatenadores.sort(key=int)
    tmp = open(basefile+"/"+original[0],"rb")
    while True:
        buffer = tmp.read(2048)
        if not buffer:
            break
        objetivo.write(buffer)
        objetivo.flush()
    tmp.close()
    os.remove(basefile+"/"+original[0])
    print("REMOVIENDO EL ARCHIVO PRINCIPAL ANIDAD AL OTRO")
    for temporal in concatenadores:
        tmp = open(basefile+"/"+temporal+".tmp","rb")
        while True:
            buffer = tmp.read(2048)
            if not buffer:
                break
            objetivo.write(buffer)
            objetivo.flush()
        tmp.close()
        os.remove(basefile+"/"+temporal+".tmp")
        print("EL ARCHIVO "+temporal+".tmp A SIDO GUARDADO AL OBJETIVO Y BORRADO ESPERA TERMINANDO")
    objetivo.close()
    print("SE TERMINO EL PROCESO EL ARCHIVO A SIDO UNIDO")

print("///////ESCRIPT DESARROLLADO POR WILLIAM THOMSON 2018\\\\\\\\")
print("---------* ESCOGE QUE HACER *-------------")
print("[1] Obtener el tamaño en bytes del archivo ")
print("[2] Concatenar archivos segun el directorio")
seleccion = input("CUAL ELIGes: ")
if seleccion == "1":
    archivo = input("PEGA AQUI LA RUTA DEL ARCHIVO CON EL ARCHIVO EJEMPLO: /sdcard/example.iso: ")
    print(os.path.getsize(archivo))
    input("PRESION ENTER PARA SALIR")
    exit(0)
if seleccion == "2":
    archivo = input("PEGA EL DIRECTORIO DONDE SE ENCUENTRE EL ARCHIVO Y LOS ARCHIVOS TEMPORALES ej: /sdcard/archivos:  ")
    concat(archivo)

else:
    print("ERRO")

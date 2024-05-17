import os
import subprocess

# Funcion/Script que extrae los keywords targets
# como agrego el nombre de la estrella en el comando???
def buscar_archivos(directorio,name):
    result=subprocess.run("dfits *ccf_*A*.fits | fitsort 'HIERARCH OHP TARG NAME' 'HIERARCH OHP DPR TYPE' 'HIERARCH OHP OBS DATE START' | grep "+name+" | grep -vi offset | grep -vi vignet | grep -vi defoc",
                          stdout=subprocess.PIPE,shell=True)
    return(result)


# Esto lo corro en mi home de spirou
directorio_maestro = "/home/sophie/SOPHIE_data/reduced"       # directorio a usar
# Obtener todos los subdirectorios del directorio_maestro recursivamente y guardarlos en una lista:
directorios = [os.path.abspath(x[0]) for x in os.walk(directorio_maestro)]
# Sacar el directorio maestro de la lista
directorios.remove(os.path.abspath(directorio_maestro))
# Sacar los directorios que no son de 2018, 2019, 2020 y 2021
directorios_a_usar=[i for i in directorios if "2018" in i or "2019" in i or "2020" in i or "2021" in i] # ojo que 2021 no va

# nuevos targets
list_of_targets = ['HD224016', 'HD17820', 'BD+700503', 'TOI1273', 'TOI1736', 'TOI2134', 'TOI1710',
                  'TOI1296', 'TOI1298', 'HD88986', 'HD207897', 'J165631']


#star = list_of_targets[1]

# correr para toda la lista de estrellas
for star in list_of_targets:
    salida = open("/home/jserrano/scripts/new_data/with_planets/planets_dataset_type_"+star+".dat","w") # Archivo1 de salida
    for i in directorios_a_usar:
        os.chdir(i)                        # Cambia el directorio de trabajo
        result = buscar_archivos(i,star)        # Corre la funcion (script)
        p = result.stdout.splitlines()     # Separa linea por linea
        for k in p:                        # Recorre cada linea 
            a=k.decode('utf-8')            # bytes to str   
            if a.find('error') == -1:      # Excluye las lineas de error (si no habia ningun archivo en el dir)
                salida.write(a+'\n')

    salida.close() 
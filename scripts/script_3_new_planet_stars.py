import os
import subprocess

# Funcion/Script que extrae los keywords targets
# como agrego el nombre de la estrella en el comando???
def buscar_archivos(directorio,name):
    result=subprocess.run("dfits *ccf_*A*.fits | fitsort 'HIERARCH OHP TARG NAME' 'HIERARCH OHP DRS CCF RV' 'HIERARCH OHP DRS DVRMS' 'HIERARCH OHP DRS CCF FWHM' 'HIERARCH OHP DRS CCF CONTRAST' 'HIERARCH OHP DRS CCF SPAN' 'HIERARCH OHP DRS BERV' 'HIERARCH OHP DRS CAL EXT SN0' 'HIERARCH OHP DRS CAL EXT SN1' 'HIERARCH OHP DRS CAL EXT SN2' 'HIERARCH OHP DRS CAL EXT SN3' 'HIERARCH OHP DRS CAL EXT SN4' 'HIERARCH OHP DRS CAL EXT SN5' 'HIERARCH OHP DRS CAL EXT SN6' 'HIERARCH OHP DRS CAL EXT SN7' 'HIERARCH OHP DRS CAL EXT SN8' 'HIERARCH OHP DRS CAL EXT SN9' 'HIERARCH OHP DRS CAL EXT SN10' 'HIERARCH OHP DRS CAL EXT SN11' 'HIERARCH OHP DRS CAL EXT SN12' 'HIERARCH OHP DRS CAL EXT SN13' 'HIERARCH OHP DRS CAL EXT SN14' 'HIERARCH OHP DRS CAL EXT SN15' 'HIERARCH OHP DRS CAL EXT SN16' 'HIERARCH OHP DRS CAL EXT SN17' 'HIERARCH OHP DRS CAL EXT SN18' 'HIERARCH OHP DRS CAL EXT SN19' 'HIERARCH OHP DRS CAL EXT SN20' 'HIERARCH OHP DRS CAL EXT SN21' 'HIERARCH OHP DRS CAL EXT SN22' 'HIERARCH OHP DRS CAL EXT SN23' 'HIERARCH OHP DRS CAL EXT SN24' 'HIERARCH OHP DRS CAL EXT SN25' 'HIERARCH OHP DRS CAL EXT SN26' 'HIERARCH OHP DRS CAL EXT SN27' 'HIERARCH OHP DRS CAL EXT SN28' 'HIERARCH OHP DRS CAL EXT SN29' 'HIERARCH OHP DRS CAL EXT SN30' 'HIERARCH OHP DRS CAL EXT SN31' 'HIERARCH OHP DRS CAL EXT SN32' 'HIERARCH OHP DRS CAL EXT SN33' 'HIERARCH OHP DRS CAL EXT SN34' 'HIERARCH OHP DRS CAL EXT SN35' 'HIERARCH OHP DRS CAL EXT SN36' 'HIERARCH OHP DRS CAL EXT SN37' 'HIERARCH OHP DRS CAL EXT SN38' 'HIERARCH OHP OBS DATE START' 'HIERARCH OHP DRS BJD'| grep "+name+" | grep -vi offset | grep -vi vignet | grep -vi defoc",
                          stdout=subprocess.PIPE,shell=True)
    return(result)
def buscar_archivos2(directorio,name):
    result2=subprocess.run("dfits *e2ds_*A*.fits | fitsort 'HIERARCH OHP TARG NAME' 'HIERARCH OHP INS FIBER' 'HIERARCH OHP CCD DIT' 'HIERARCH OHP INS ADCANG' 'HIERARCH OHP INS ADCNUM' 'HIERARCH OHP INS TEMP1 MIN' 'HIERARCH OHP INS TEMP1 MAX' 'HIERARCH OHP INS TEMP3 MIN' 'HIERARCH OHP INS TEMP3 MAX' 'HIERARCH OHP INS PRES1 MIN' 'HIERARCH OHP INS PRES1 MAX' 'HIERARCH OHP INS PRES2 MIN' 'HIERARCH OHP INS PRES2 MAX' 'HIERARCH OHP OBS DATE START' 'HIERARCH OHP OBS DATE END' 'HIERARCH OHP TARG RADVEL' 'HIERARCH OHP TEL AIRM END' 'HIERARCH OHP TEL AIRM START' 'HIERARCH OHP TEL ALT' 'HIERARCH OHP GUID SEEING' 'HIERARCH OHP GUID SKY LEVEL' 'HIERARCH OHP GUID ALPHA MEAN' 'HIERARCH OHP GUID ALPHA RMS' 'HIERARCH OHP GUID DELTA MEAN' 'HIERARCH OHP GUID DELTA RMS' 'HIERARCH OHP SENTI TEXT' 'HIERARCH OHP SENTI HUMI' 'HIERARCH OHP SENTI SEEING' 'HIERARCH OHP SENTI TCIEL' 'HIERARCH OHP SENTI MAG' 'HIERARCH OHP DRS BJD' 'HIERARCH OHP TARG ALPHA' 'HIERARCH OHP TARG DELTA' 'HIERARCH OHP DRS DRIFT RV' 'HIERARCH OHP DRS DRIFT NBCOS' 'HIERARCH OHP DRS DRIFT RFLUX' | grep "+name+" | grep -vi offset | grep -vi vignet | grep -vi defoc",
                          stdout=subprocess.PIPE,shell=True)
    return(result2)

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
    salida = open("/home/jserrano/scripts/new_data/with_planets/planets_dataset_ccf_"+star+".dat","w") # Archivo1 de salida
    salida2 = open("/home/jserrano/scripts/new_data/with_planets/planets_dataset_e2ds_"+star+".dat","w") # Archivo2 de salida
    for i in directorios_a_usar:
        os.chdir(i)                        # Cambia el directorio de trabajo
        result = buscar_archivos(i,star)        # Corre la funcion (script)
        result2 = buscar_archivos2(i,star)
        p = result.stdout.splitlines()     # Separa linea por linea
        p2 = result2.stdout.splitlines() 
        for k,j in zip(p, p2):                        # Recorre cada linea 
            a=k.decode('utf-8')            # bytes to str
            b=j.decode('utf-8')    
            if a.find('error') == -1:      # Excluye las lineas de error (si no habia ningun archivo en el dir)
                salida.write(a+'\n')
                salida2.write(b+'\n')

    salida.close() 
TempXL 
''son las temperaturas integradas cada 1 hora, desde 2017 a la fecha''

master_constant_neda2024 
''es la master constant armada por neda que se usa actualmente''

HD185144_data_for_activity_removal 
''son las VRs que neda usó para remover la actividad de HD185144 antes de hacer la master constant
cuidado: hay que remover los "test days" primero, los dias que tiene mas de 3 o 4 observaciones son porque estaban testeando el instrumento
If the observation of HD185144 is more than 3/4 times, they are
tested and should be removed.
The bissmoy is a master constant correction on the bisector (for more
information see section 2 of my thesis). We usually use them for the sp1
targets.''

train
''aca van todos los datasets que se van a usar para el training
superconstantes + estrellas con poca dispersion''

test
''aca van todos los datasets que se van a usar para testear luego
la corrección, tienen que ser estrellas con planetas conocidos para luego comparar parametros''

header keys meaning
''
temperatures
HIERARCH OHP INS TEMP1 NAME=    'GRATING'  /
HIERARCH OHP INS TEMP2 NAME=        'CCD'  /
HIERARCH OHP INS TEMP3 NAME=  'Air local'  /
Pressure
HIERARCH OHP INS PRES1 NAME=        'AIR'  /
HIERARCH OHP INS PRES2 NAME=       'TANK'  /''
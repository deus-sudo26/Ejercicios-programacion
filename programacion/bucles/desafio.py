#quiero

cantidad_masculinos_ia_iot = 0
cantidad_no_ia = 0
edad_empleado_menor = 0
nombre_empleado_menor = "menor"
tecnologia_empleado_menor = "menor"

edad_empleado_mayor = 0
nombre_empleado_mayor = "mayor"
tecnologia_empleado_mayor = "mayor"

contador = 0

tecnologia_ia = 0
tecnologia_rv_ra = 0
tecnologia_iot = 0
cantidad_masculinos_total = 0

while contador < 3:
    nombre = input("ingresa tu nombre: ")
    edad = int(input("ingresa tu edad: "))
    while edad < 18:   ################################################# VALIDACION DE EDAD
        edad = int(input("vuelve a ingresar tu edad: "))

    genero = input("ingresa tu genero (masculino/femenino/otro): ")
    while genero != "masculino" and genero != "femenino" and genero != "otro": ######## VALIDACION DE GENERO
        genero = input("vuelve a ingresar tu genero: ")
    tecnologia_elegida = input("ingresa la tecnoloigia de preferencia (ia/ rv-ra /iot)")
    while tecnologia_elegida != "ia" and tecnologia_elegida != "rv-ra" and tecnologia_elegida != "iot":  ## VALIDACION DE TECNOLOGIAS
        tecnologia_elegida = input("vuelve a ingresar la tecnologia: ")

################## conteo de tecnologias y separacion de masculinos y femeninos #################################

    match tecnologia_elegida:
        case "ia":
            tecnologia_ia += 1
            if genero == "masculino":
                cantidad_masculinos_total += 1
                if edad >=25 and edad <= 50:
                    cantidad_masculinos_ia_iot += 1

        case "iot":
            tecnologia_iot += 1
            if genero == "masculino":
                cantidad_masculinos_total += 1
                if edad >=25 and edad <= 50:
                    cantidad_masculinos_ia_iot += 1
                if edad >= 33 and edad <= 40 :
                    cantidad_no_ia += 1
        case "rv-ra":
            tecnologia_rv_ra += 1
            if genero == "masculino":
                cantidad_masculinos_total += 1
                if edad >= 33 and edad <= 40:
                    cantidad_no_ia += 1
##################### Maximos y Minimos ###############################
    if edad_empleado_menor == 0 or edad < edad_empleado_menor:
        edad_empleado_menor = edad
        nombre_empleado_menor = nombre
        tecnologia_empleado_menor = tecnologia_elegida

        if edad_empleado_mayor == 0 and genero == "masculino":
            edad_empleado_mayor = edad
            nombre_empleado_mayor = nombre
            tecnologia_empleado_mayor = tecnologia_elegida
    
    if edad > edad_empleado_mayor and genero == "masculino":
        edad_empleado_mayor = edad
        nombre_empleado_mayor = nombre
        tecnologia_empleado_mayor = tecnologia_elegida
    contador += 1

total_votos_no_ia = tecnologia_iot + tecnologia_rv_ra
porcentaje_no_votaron_ia = (total_votos_no_ia * 100) / 10
porcentaje_masculino_no_ia = (cantidad_no_ia * porcentaje_no_votaron_ia) / total_votos_no_ia

porcentaje_total_masculinos = ( cantidad_masculinos_total  * 100 ) / 10

print(f"""
El empleado de menor edad es:
{nombre_empleado_menor}
{edad_empleado_menor} de edad.
Tecnologia elegida: {tecnologia_empleado_menor}.

El empleado de mayor edad:
{nombre_empleado_mayor}
{edad_empleado_mayor} de edad.
Tecnologia elegida: {tecnologia_empleado_mayor}.

El porcentaje de empleados masculinos que no votaron por ia de entre 33 y 40 años de edad son el {porcentaje_masculino_no_ia}%
La cantidad de empleados masculinos que votaron por ia/iot son: {cantidad_masculinos_ia_iot}  votantes
 """)

altura_maxima = tecnologia_iot
if tecnologia_ia > altura_maxima:
    altura_maxima = tecnologia_ia
if tecnologia_rv_ra > altura_maxima:
    altura_maxima = tecnologia_rv_ra
fila = altura_maxima
while fila > 0:
    linea = ""
    if tecnologia_iot >= fila:
        linea = linea + "🟩 "
    else:
        linea = linea + "  "
    if tecnologia_rv_ra >= fila:
        linea = linea + "🟩 "
    else:
        linea = linea + "  "
    if tecnologia_ia >= fila:
        linea = linea + "🟩  "
    print(linea)
    fila = fila - 1
print("-" * 12)
print ("iot ia rv/ra")


tamaño_grafico = 20 
grafico_lleno = int(tamaño_grafico * porcentaje_total_masculinos / 100)
linea = "M |"
columna = 1
while columna <= tamaño_grafico:
    if columna <= grafico_lleno:
        linea = linea + "🟩 "
    else:
        linea = linea + "🟥 "
    columna = columna + 1
linea = linea + "|"


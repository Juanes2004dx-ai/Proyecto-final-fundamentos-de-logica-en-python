#Estacion 1-Operaciones básicas y una primera idea de enteros------
#Nivel 1----
'''a = float(input("Escribe el primer número: "))
b = float(input("Escribe el segundo número: "))
suma = a + b
print(f"tu suma da:{suma}")
resta = a - b
print(f"tu resta da:{resta}")
multiplicacion = a * b
print(f"tu multiplicacion da:{multiplicacion}")
division = a / b
print(f"tu division da:{division}")'''
#Nivel 2----
'''temp_inicial = float(input("Temperatura inicial (°C): "))
temp_final = float(input("Temperatura final (°C): "))
diferencia = temp_final - temp_inicial
if(diferencia>0):
    print(f"Subió {diferencia} grados" )
elif(diferencia == 0):
    print("Se mantuvo igual")
else:
    print(f"Bajó {abs(diferencia)} grados")'''
#Nivel 3----
'''VALOR_FIJO = 40000
COSTO_POR_HORA = 15000
horas = float(input("¿Cuántas horas duró el mantenimiento?: "))
horas_trabajadas = COSTO_POR_HORA * horas
print(f"Horas en totales trabajadas fueron: {horas_trabajadas}")
costo_total = VALOR_FIJO + horas_trabajadas
print(f"El costo fue de: {costo_total}")'''

#Estacion 2-Enteros, signos y jerarquía de operaciones------
#Nivel 1----
'''operacion_1 = 20 - 3**2 + 5
print(f"tu resultado es: {operacion_1}")
operacion_2 = 2* (5 - 3)**3
print(f"tu resultado es: {operacion_2}")'''
#Nivel 2----
'''saldo_inicial = float(input("Saldo inicial (usa negativo si está en descubierto): "))
deposito = float(input("Valor a depositar: "))
retiro = float(input("Valor a retirar: "))
saldo_final = (saldo_inicial + deposito - retiro)
if(saldo_final>0):
    print(f"su saldo quedo en {saldo_final}, esta en positivo")
else:
    print(f"su saldo quedo en {saldo_final}, esta en descubierto")'''
#Nivel 3----
'''saldo_inicial = float(input("ingrese su saldo: "))
resultado = saldo_inicial
ingreso = float(input("ingrese su consignacion: "))
retiro1 = float(input("ingrese su primer retiro: "))
retiro2 = float(input("ingrese su segundo retiro: "))
movimientos = [ingreso, -retiro1, -retiro2]
for i in movimientos:
    resultado = resultado + i
print(f"Saldo final: {resultado}")'''

#Estacion 3-Fracciones y decimales------
#Nivel 1----
'''numerador = float(input("Numerador: "))
denominador = float(input("Denominador: "))
if(denominador == 0):
    print("denominador inválido")
else:
    resultado = numerador / denominador
    print(f"el resultado de la fraccion es: {resultado:.2f}")'''
#Nivel 2----
'''precio = float(input("Precio del producto: "))
num_desc = float(input("Numerador de la fracción de descuento: "))  
den_desc = float(input("Denominador de la fracción de descuento: "))
if(den_desc == 0):
    print("denominador inválido")
else:
    fraccion = num_desc/den_desc
descuento = precio * fraccion
print(f"precio con descuento: {descuento}")
precio_final = precio - descuento
print(f"precio final: {precio_final}")
if(precio_final<10000):
    print("precio muy bajo, revisar")
else:
    print("precio alto")'''
#Nivel 3----
'''tamanio_mb = float(input("ingrese el tamaño de los mb: "))
numerador = float(input("ingrese el numerador: "))
denominador= float(input("ingrese el denominador: "))
fraccion = numerador/denominador
mb_por_fraccion = tamanio_mb * fraccion
print(f"los MB que representa la fracción son : {mb_por_fraccion:.2f}")
num_servidores = float(input("ingrese el numero de servidores: "))
mb_por_servidor = mb_por_fraccion/num_servidores
print(f"MB por servidor es: {mb_por_servidor:.2f}")'''

#Estacion 4-Porcentajes------
#Nivel 1----
'''precio = float(input("Precio: "))
porcentaje_descuento = float(input("Porcentaje de descuento (por ejemplo 15): "))
descuento = precio * (porcentaje_descuento/100)
print(f"precio con descuento: {descuento}")
precio_final = precio - descuento
print(f"precio final: {precio_final}")'''
#Nivel 2----
'''total_tareas = float(input("Total de tareas: "))
tareas_completadas = float(input("Tareas completadas: "))
porcentaje_avance = (tareas_completadas/total_tareas) * 100
if(porcentaje_avance >= 80):
    print(f"proyecto en un {porcentaje_avance}%, esta casi listo")
elif(porcentaje_avance >= 40):
    print(f"proyecto en un {porcentaje_avance}%, esta en curso")
else:
    print(f"proyecto en un {porcentaje_avance}%, esta en etapa inicial")'''
#Nivel 3----
'''total = float(input("ingrese el total de pruebas: "))
exitosas = float(input("ingrese la cantidad de exitosas: "))
porcentaje = (exitosas/total)*100
print(f"Porcentaje de éxito actual es de un: {porcentaje:.2f}%")
nuevas_exitosas = (porcentaje+10)/100*total
print(f"Pruebas exitosas con 10 puntos adicionales: {nuevas_exitosas:.2f}")'''

#Estacion 5-Potencias y raíces------
#Nivel 1----
'''lado = float(input("Lado del cuadrado (cm): "))
area = lado**2
print(f"El área del cuadrado es de {area}cm")'''
#Nivel 2----
'''import math
area = float(input("Área del terreno (m²): "))
if(area < 0):
    print("área inválida")
else:
    print(f"La área es:{math.sqrt(area):.2f}")'''
#Nivel 3----
'''import math
area_px = float(input("Digite el area por pixles: "))
lado = math.sqrt(area_px)
lado_cubo = (lado)**3
print(f"Lado del ícono: {lado}px")
print(f"Lado al cubo (alta resolución): {lado_cubo}")'''

#Estacion 6-Álgebra básica: variables y ecuaciones------
#Nivel 1----
'''x = float(input("Valor de x: "))
y = float(input("Valor de y: "))
resultado = (2*(x))+(3*(y))-5 
print(f"el resultado de la operacion es: {resultado}")'''
#Nivel 2----
'''b = float(input("Valor de b: "))
c = float(input("Valor de c: "))
x = c - b
print(f"El valor de x es: {x}")
c = x + b
print(f"El resultado de x + b es: {c}")'''
#Nivel 3----
'''a = float(input("Valor de a: "))
b = float(input("Valor de b: "))
c = float(input("Valor de c: "))
if(a == 0):
    print("No se puede resolver: a no puede ser 0")
else:
    ax = c - b
    print(f"El valor de ax es: {ax}")
    x = ax / a
    print(f"El valor de x es: {x}")
    c = a * x + b
    print(f"El valor de c es: {c}")'''

#Estacion 7-Lógica matemática básica: proposiciones y operadores booleanos------
#Nivel 1----
'''numero = float(input("escriba su nuemro: "))
es_par = (numero %2 == 0)
es_mayor_que_10 = numero > 10
print(f"¿el numero es par?:{es_par}")
print(f"¿el numero es mayor que 10?:{es_mayor_que_10}")'''
#Nivel 2----
'''numero = float(input("escriba su número: "))
es_par = (numero %2 == 0)
es_mayor_que_10 = numero > 10
print(f"¿la negación de es_par(Not): {not es_par}")
print(f"¿la conjunción de es_par y es_mayor_que_10 (and)?: {es_par and es_mayor_que_10}")
print(f"¿la disyunción de es_par o es_mayor_que_10 (OR)?: {es_par or es_mayor_que_10}")'''
#Nivel 3----
'''usuario_activo = str(input("¿tu usuario esta activo?(si/no): "))
usuario_activo.lower()
contrasena_correcta = str(input("¿tu contraseña es correcta?(si/no): "))
contrasena_correcta.lower()
if(usuario_activo == "si" and contrasena_correcta == "si"):
    print(True)
else:
    print(False)
tiene_cedula = str(input("¿tienes tu cedula?(si/no): "))
tiene_cedula.lower()
tiene_invitacion = str(input("¿tienes invitacion?(si/no): "))
tiene_invitacion.lower()
if(tiene_cedula == "si" or tiene_invitacion == "si"):
    print(True)
else:
    print(False)'''
#Reto integrador: Calculadora del trimestre-----
'''print("--- Calculadora del trimestre ---")
print("1. Costo de mantenimiento")
print("2. Saldo final de una cuenta")
print("3. Reparto de un archivo entre servidores")
print("4. Resumen de pruebas automatizadas")
print("5. Analizar ícono de una app")
print("6. Resolver una ecuación ax + b = c")
print("7. Verificar acceso (lógica)")
print("0. Salir")
opcion = 0
while(opcion != "0"):
    opcion = int(input("Escriba la opcion que quiere seleccionar: "))
    if(opcion == 1):
        valor_fijo = float(input("Digite el valor fijo: ")) #40000
        costo_por_hora = float(input("Digite el costo por hora: ")) #15000
        horas = float(input("¿Cuántas horas duró el mantenimiento?: "))
        horas_trabajadas = costo_por_hora * horas
        print(f"Horas en totales trabajadas fueron: {horas_trabajadas}")
        costo_total = valor_fijo + horas_trabajadas
        print(f"El costo fue de: {costo_total}")
    if(opcion == 2):
        saldo_inicial = float(input("ingrese su saldo: ")) #-45000
        resultado = saldo_inicial
        ingreso = float(input("ingrese su consignacion: ")) #120000
        retiro1 = float(input("ingrese su primer retiro: ")) #-30000
        retiro2 = float(input("ingrese su segundo retiro: ")) #-20000
        movimientos = [ingreso, retiro1, retiro2]
        for i in movimientos:
            resultado = resultado + i
        print(f"Saldo final: {resultado}")
    if(opcion == 3):
        tamanio_mb = float(input("ingrese el tamaño de los mb: ")) #900
        numerador = float(input("ingrese el numerador: ")) #2
        denominador= float(input("ingrese el denominador: ")) #3
        fraccion = numerador/denominador
        mb_por_fraccion = tamanio_mb * fraccion
        print(f"los MB que representa la fracción son : {mb_por_fraccion:.2f}")
        num_servidores = float(input("ingrese el numero de servidores: ")) #3
        mb_por_servidor = mb_por_fraccion/num_servidores
        print(f"MB por servidor es: {mb_por_servidor:.2f}")
    if(opcion == 4):
        total = float(input("ingrese el total de pruebas: ")) #150
        exitosas = float(input("ingrese la cantidad de exitosas: ")) #108
        porcentaje = (exitosas/total)*100
        print(f"Porcentaje de éxito actual es de un: {porcentaje:.2f}%")
        nuevas_exitosas = (porcentaje+10)/100*total
        print(f"Pruebas exitosas con 10 puntos adicionales: {nuevas_exitosas:.2f}")
    if(opcion == 5):
        import math
        area_px = float(input("Digite el area por pixles: ")) #324
        lado = math.sqrt(area_px)
        lado_cubo = (lado)**3
        print(f"Lado del ícono: {lado}px")
        print(f"Lado al cubo (alta resolución): {lado_cubo}")
    if(opcion == 6):
        a = float(input("Valor de a: ")) #3
        b = float(input("Valor de b: ")) #4
        c = float(input("Valor de c: ")) #19
        if(a == 0):
            print("No se puede resolver: a no puede ser 0")
        else:
            ax = c - b
            print(f"El valor de ax es: {ax}")
            x = ax / a
            print(f"El valor de x es: {x}")
            c = a * x + b
            print(f"El valor de c es: {c}")
    elif(opcion == 7):
        usuario_activo = str(input("¿tu usuario esta activo?(si/no): "))
        usuario_activo.lower()
        contrasena_correcta = str(input("¿tu contraseña es correcta?(si/no): "))
        contrasena_correcta.lower()
        if(usuario_activo == "si" and contrasena_correcta == "si"):
            print(True)
        else:
            print(False)
        tiene_cedula = str(input("¿tienes tu cedula?(si/no): "))
        tiene_cedula.lower()
        tiene_invitacion = str(input("¿tienes invitacion?(si/no): "))
        tiene_invitacion.lower()
        if(tiene_cedula == "si" or tiene_invitacion == "si"):
            print(True)
        else:
            print(False)
    if(opcion == 0):
        print("¡Hasta la próxima!")
    else:
        print("Opción no válida, intenta de nuevo.")'''

#Reto creativo:-----
# Mi problema: Descuento en una tienda.
# Una tienda ofrece un 20% de descuento en una compra si el cliente cumple al menos una de estas condiciones:
# 1. Es cliente habitual.
# 2. La compra es mayor o igual a $10.000.
# Si el cliente tiene un cupón de descuento, recibe un 5% de descuento.
# Crea un programa en Python que:
# 1. Pida el valor de la compra.
# 2.Pregunte si el cliente es estudiante (si o no).
# 3.Pregunte si tiene cupón (si o no).
# 4.Determine mediante operadores lógicos si puede obtener el 20% de descuento.
# 5.Si tiene cupón, aplique el 5% de descuento.
# 6.Que muestre: el valor original, el valor con el descuento aplicado y el valor final a pagar con el cupon.
#
# Temas que usé: Porcentajes y proposiciones, operadores booleanos.
print("-----------------------------------")
print("       TIENDA DE DESCUENTOS")
print("-----------------------------------")
compra = float(input("Ingrese el valor de la compra: $"))
cliente_habitual = str(input("¿Eres un cliente_habitual? (si/no): "))
cliente_habitual = cliente_habitual.lower()
cupon = input("¿Tiene cupón? (si/no): ")
cupon = cupon.lower()
descuento = 0
valor_final = 0
if(compra >= 10000 and cliente_habitual == "si"):
    descuento = compra * 0.20
if(cupon == "si"):
    descuento = descuento + (compra * 0.05)
valor_final = compra - descuento
print("-----------------------------------")
print(f"Valor original: ${compra:.2f}")
print(f"Descuento: ${descuento:.2f}")
print(f"Total a pagar: ${valor_final:.2f}")
print("-----------------------------------")
print("Feliz dia")
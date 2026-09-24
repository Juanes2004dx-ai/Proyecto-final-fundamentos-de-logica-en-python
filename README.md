# Proyecto-final-fundamentos-de-logica-en-python
Trabajo final de todo lo enseñando en la materia durante los 3 meses que dure esta 
# Caso 2 - SPA Móvil para mascotas
mascotas=[]
print("---------------------------------------")
print("!Bienvenido al Spa Móvil para Mascotas¡")
print("---------------------------------------")
cantidad_mascotas = int(input("¿Cuantas mascotas deseas atender el dia de hoy?: "))
total_recaudado = 0
TEXTO = "escriba el número de la opción que deseas: "
#Como este mensaje se repite varias veces se usa un def para que solo sea llamar este funcion
def imprimir_pociones(opcion_a, opcion_b):
    print("¿Que opcion deseas elegir?")
    print(f"Opcion 1. {opcion_a}")
    print(f"Opcion 2. {opcion_b}")
    print("--------------------------")

#Esta parte sirve para aumentar el número de las mascotas dependiendo de la cantidad de mascotas que el usuario coloque
for i in range(cantidad_mascotas):
    i += 1
    print("---------------------")
    print(f"Mascota número {i}")
    print("---------------------")
    nombre = str(input("Digite el nombre de su mascota: "))
    print("--- Tipo de Mascota ---")
    imprimir_pociones("Baño para gatos", "Baño para perros") #Aqui se llama a la funcion definida anteriormente
    opcion_1 = int(input(TEXTO))
    if(opcion_1 == 1):
        print("Baño para Gato escogido, tendrá un valor de $30.000 COP")
        tipo = "Gato" #se crean sub variables para guardar los datos que mas adelante seran utilizados
        tamanio = "Normal"
        precio_banio = int(30000)
    elif(opcion_1 == 2):
        print("--- Tamaño del Perro ---")
        imprimir_pociones("Perro Pequeño o Mediano", "Perro Grande o Gigante")
        opcion_2 = int(input(TEXTO))
        if(opcion_2 == 1):
            print("Perro Pequeño o Mediano escogido, tendrá un valor de $25.000 COP")
            tipo = "Perro"
            tamanio = "Pequeño o Mediano"
            precio_banio = int(25000)
        elif(opcion_2 == 2):
            print("Perro Grande o Gigante escogido, tendrá un valor de $45.000 COP")
            tipo = "Perro"
            tamanio = "Grande o Gigante"
            precio_banio = int(45000)
    print("--- Servico Adicional ---")
    imprimir_pociones("Corte de Uñas", "Limpieza de Oídos")
    opcion_3 = int(input(TEXTO))
    if(opcion_3 == 1):
        print("Corte de Uñas escogido, tendrá un valor de $10.000 COP")
        adicional = "Corte de Uñas"
        precio_adicional = int(10000)
    elif(opcion_3 == 2):
        print("Limpieza de Oídos escogido, tendrá un valor de $5.000 COP")
        adicional = "Limpieza de Oídos"
        precio_adicional = int(5000)
    total = precio_banio + precio_adicional
#Aqui se guardan los diferentes elemento que se han recopilado durante el codigo anterior y estos se guardaran en la lista Mascotas
    mascota = {
                "nombre": nombre,
                "tipo": tipo,
                "tamanio": tamanio,
                "adicional": adicional,
                "total": total
                }
    mascotas.append(mascota) #En la lista mascotas se guardaria todos los diccionarios mascota que se hayan creado
    total_recaudado += total
    print("---------------------------------")
    print("Mascota registrada correctamente.")
    print(f"Total a pagar: ${total} COP")
    print("---------------------------------")
#Una vez que se llenen los datos de la última mascota, aquí se mostraran cuantas mascotas ingreso el usuario y el valor total de los servicios brindados
print("-------------------------------------------------")
print(f"Total de mascotas atendidas: {cantidad_mascotas}")
print(f"Total recaudado: ${total_recaudado} COP")
print("-------------------------------------------------")
respuesta = input("¿Desea ver el detalle de las mascotas?(si/no): ")
respuesta = respuesta.lower()
if(respuesta == "si"):
    print("-----------------------")
    print("Detalle de las Mascotas")
    print("-----------------------")
    for mascota in mascotas: #Este for va contando cuantos indeces se han guardado en el diccionario
        print("-------------------------------------------")
        print(f"Nombre: {mascota["nombre"]}")
        print(f"Tipo: {mascota["tipo"]}")
        print(f"Tamaño: {mascota["tamanio"]}")
        print(f"Servicio adicional: {mascota["adicional"]}")
        print(f"Total pagado: ${mascota["total"]}")
        print("-------------------------------------------")
    print("Feliz Dia y Vuela Pronto :D")
else:
    print("Feliz Dia y Vuela Pronto :D")

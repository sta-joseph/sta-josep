alumnos = []

def grabarDatos():
    print("Bienvenido a Ingresar Persona")
    nombre = input("Ingrese nombre: ")
    edad = int(input("Ingrese edad: "))
    altura = float(input("Ingrese altura: "))

    persona = {
        "nombre": nombre, 
        "edad": edad, 
        "altura": altura,
        "notas": []  # Agregamos un campo para las notas
    }
    
    alumnos.append(persona)  # Agregamos esta persona a la lista de alumnos
# fin funcion grabarDatos

def buscarAlumno(nombre):
    for persona in alumnos:
        if persona["nombre"] == nombre:
            return persona
    return None

def mostrarPersona():
    print("Bienvenido a Buscar Persona")
    nombre = input("Ingrese nombre a buscar: ")
    persona = buscarAlumno(nombre)
    if persona:
        print("Persona encontrada!!!")
        print(f"Nombre de alumno: {persona['nombre']}")
        print(f"Edad de alumno: {persona['edad']}")
        print(f"Altura de alumno: {persona['altura']}")
    else:
        print(f"{nombre} no se encuentra en la lista")
    print("------------------")
# fin funcion mostrarPersona

def ingresarNota():
    print("Bienvenido a Ingresar Nota")
    nombre = input("Ingrese nombre del alumno: ")
    persona = buscarAlumno(nombre)
    if persona:
        while True:
            try:
                ramo = input("Ingresar nombre de ramo: ")
                nota = float(input("Ingrese nota: "))
                persona["notas"].append({"ramo": ramo, "nota": nota})
                break
            except ValueError:
                print("La nota debe ser un número decimal (ej: 7.0)")
    else:
        print("Alumno no existe en la lista")
# fin funcion ingresarNota

def imprimirCertificado():
    print("Bienvenido a Imprimir Certificado")
    nombre = input("Ingrese nombre del alumno: ")
    persona = buscarAlumno(nombre)
    if persona:
        print(f"Certificado de Notas de {persona['nombre']}:")
        for nota in persona["notas"]:
            print(f"Ramo: {nota['ramo']}, Nota: {nota['nota']}")
    else:
        print(f"{nombre} no se encuentra en la lista")
# fin funcion imprimirCertificado

def salir():
    print("Gracias por usar el programa....")
# fin funcion salir del programa

while True:
    # Mostrar menu de opciones
    print(
        """
        1.- Ingresar Datos
        2.- Buscar persona 
        3.- Ingresar Nota
        4.- Imprimir certificado
        5.- Salir
        """
    )
    # Validamos con un try la opcion que sea correcta
    try:
        opcion = int(input("Ingrese valor a operar: "))  # Ingreso de opcion a operar
    except ValueError:
        opcion = 0  # Se cambia opcion a cero para que el ciclo while se repita
    # fin try
    if opcion < 1 or opcion > 5:
        print("Ingrese una opcion valida")
    else:
        if opcion == 1:
            grabarDatos()  # Llamar a funcion de grabar datos
        elif opcion == 2:
            mostrarPersona()  # Llamar a funcion buscar persona
        elif opcion == 3:
            ingresarNota()  # Llamar a funcion ingresar nota
        elif opcion == 4:
            imprimirCertificado()  # Llamar a funcion imprimir certificado
        else:
            salir()  # Llamar a funcion salir
            break
        # fin if
    # fin if
# end while

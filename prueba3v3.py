import csv

notestudiante = []

def menuf():
    print("-------------Menu-------------")
    print("1. Registro de Notas")
    print("2. Buscar Estudiante")
    print("3. Calcular el promedio de un estudiante")
    print("4. Mostrar todos los estudiantes registrados")
    print("5. Eliminar un Estudiante")
    print("6. Salir del programa")
    print("------------------------------")

def calcular_promedio(estudiante):
    total_notas = estudiante["nota matematicas"] + estudiante["nota ciencias"] + estudiante["nota historia"]
    promedio = total_notas / 3
    print(f"El promedio de {estudiante['nombre estudiante']} {estudiante['apellido estudiante']} es: {promedio}")



while True:
    menuf()
    menu = int(input("Elija su respuesta: "))

    if menu == 1:
        nombre = input("Nombre Estudiante: ")
        apellido = input("Apellido Estudiante: ")
        mate = int(input("Nota Matematicas: "))
        ciencia = int(input("Nota Ciencias: "))
        historia = int(input("Nota Historia: "))
        
        


        estudiante = {
            "nombre estudiante": nombre,
            "apellido estudiante": apellido,
            "nota matematicas": mate,
            "nota ciencias": ciencia,
            "nota historia": historia
        }
        total_notas = estudiante["nota matematicas"] + estudiante["nota ciencias"] + estudiante["nota historia"]
        promedio = total_notas / 3

        notestudiante.append(estudiante)

        print("Has ingresado los datos con éxito!")
        calcular_promedio(estudiante)

        with open('Registro de Notas Estudiante.csv', 'a', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            if archivo_csv.tell() == 0:
                escritor_csv.writerow(['Nombre', 'Apellido', 'Nota Matematicas', 'Nota Ciencias', 'Nota Historia','Promedio'])
            escritor_csv.writerow([nombre, apellido, mate, ciencia, historia, promedio])
            escritor_csv.writerow(['------------------------------------------------------'])

    elif menu == 2:
        search = input("Desea buscar por nombre o apellido?: ").lower()
        
        if search == "nombre":
            nomsearch = input("Ingrese el nombre a buscar: ")
            
            for estudiante in notestudiante:
                if nomsearch == estudiante["nombre estudiante"]:
                    print(f"Nombre: {estudiante['nombre estudiante']}, Apellido: {estudiante['apellido estudiante']}, Nota Historia: {estudiante['nota historia']}, Nota Ciencias: {estudiante['nota ciencias']}, Nota Matematicas: {estudiante['nota matematicas']}")
        
        elif search == "apellido":
            catesearch = input("Ingrese el apellido a buscar: ").lower()
            
            for estudiante in notestudiante:
                if estudiante["apellido estudiante"].lower() == catesearch:
                    print(f"Nombre: {estudiante['nombre estudiante']}, Apellido: {estudiante['apellido estudiante']}, Nota Historia: {estudiante['nota historia']}, Nota Ciencias: {estudiante['nota ciencias']}, Nota Matematicas: {estudiante['nota matematicas']}")
        
        else:
            print("Opción de búsqueda no válida.")

    elif menu == 3:
        if len(notestudiante) == 0:
            print("No hay estudiantes registrados.")
        else:
            nomsearch = input("Ingrese el nombre del estudiante para calcular su promedio: ")
            encontrado = False
            for estudiante in notestudiante:
                if nomsearch == estudiante["nombre estudiante"]:
                    calcular_promedio(estudiante)
                    encontrado = True
                    break
            if not encontrado:
                print(f"No se encontró ningún estudiante con el nombre '{nomsearch}'.")

    elif menu == 4:
        if len(notestudiante) == 0:
            print("No hay estudiantes registrados.")
        else:
            print("Estudiantes registrados:")
            for estudiante in notestudiante:
                print(f"Nombre: {estudiante['nombre estudiante']}, Apellido: {estudiante['apellido estudiante']}, Nota Historia: {estudiante['nota historia']}, Nota Ciencias: {estudiante['nota ciencias']}, Nota Matematicas: {estudiante['nota matematicas']},")
                calcular_promedio(estudiante)


    elif menu == 5:

        descripcion_eliminar = input("Ingrese el estudiante a eliminar: ")
        
        encontrado = False
        for estudiante in notestudiante:
            if estudiante["nombre estudiante"] == descripcion_eliminar:
                notestudiante.remove(estudiante)
                print(f"Estudiante '{descripcion_eliminar}' eliminado.")
                encontrado = True
        
        if not encontrado:
            print(f"No se encontró ningún estudiante con la descripción '{descripcion_eliminar}'.")

    elif menu == 6:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Por favor, elija una opción del 1 al 5.")

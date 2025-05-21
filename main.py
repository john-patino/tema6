
# CRUD básico en Python con funciones y listas

# Base de datos simulada usando una lista de diccionarios
database = []

# Create - Crear un nuevo registro
def create(registro):
    # Generamos un ID único basado en la longitud de la base de datos
    id = len(database) + 1
    registro['id'] = id
    database.append(registro)
    return id

# Read - Leer registros
def read(id=None):
    if id is None:
        # Si no se especifica ID, devolver todos los registros
        return database
    else:
        # Buscar registro por ID
        for registro in database:
            if registro['id'] == id:
                return registro
        return None  # Retornar None si no se encuentra el registro

# Update - Actualizar un registro existente
def update(id, datos_actualizados):
    for i, registro in enumerate(database):
        if registro['id'] == id:
            # Actualizamos los datos pero mantenemos el ID
            datos_actualizados['id'] = id
            database[i] = datos_actualizados
            return True
    return False  # Retornar False si no se encuentra el ID

# Delete - Eliminar un registro
def delete(id):
    for i, registro in enumerate(database):
        if registro['id'] == id:
            database.pop(i)
            return True
    return False  # Retornar False si no se encuentra el ID

# Función para mostrar un menú interactivo
def menu():
    while True:
        print("\n--- CRUD con Python ---")
        print("1. Crear registro")
        print("2. Mostrar registros")
        print("3. Buscar registro por ID")
        print("4. Actualizar registro")
        print("5. Eliminar registro")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            email = input("Email: ")
            
            nuevo_registro = {
                "nombre": nombre,
                "edad": edad,
                "email": email
            }
            
            id = create(nuevo_registro)
            print(f"Registro creado con ID: {id}")
            
        elif opcion == "2":
            registros = read()
            if len(registros) == 0:
                print("No hay registros.")
            else:
                print("\nListado de registros:")
                for registro in registros:
                    print(f"ID: {registro['id']}, Nombre: {registro['nombre']}, Edad: {registro['edad']}, Email: {registro['email']}")
                    
        elif opcion == "3":
            id = int(input("Ingrese el ID a buscar: "))
            registro = read(id)
            if registro:
                print(f"Registro encontrado - ID: {registro['id']}, Nombre: {registro['nombre']}, Edad: {registro['edad']}, Email: {registro['email']}")
            else:
                print(f"No se encontró ningún registro con ID: {id}")
                
        elif opcion == "4":
            id = int(input("ID del registro a actualizar: "))
            registro = read(id)
            if registro:
                print("Datos actuales:")
                print(f"Nombre: {registro['nombre']}")
                print(f"Edad: {registro['edad']}")
                print(f"Email: {registro['email']}")
                
                nombre = input("Nuevo nombre (deje en blanco para mantener el actual): ")
                edad_str = input("Nueva edad (deje en blanco para mantener la actual): ")
                email = input("Nuevo email (deje en blanco para mantener el actual): ")
                
                # Usamos los valores actuales si no se proporcionan nuevos
                nombre = nombre if nombre else registro['nombre']
                edad = int(edad_str) if edad_str else registro['edad']
                email = email if email else registro['email']
                
                datos_actualizados = {
                    "nombre": nombre,
                    "edad": edad,
                    "email": email
                }
                
                if update(id, datos_actualizados):
                    print("Registro actualizado exitosamente.")
                else:
                    print(f"No se pudo actualizar el registro con ID: {id}")
            else:
                print(f"No existe un registro con ID: {id}")
                
        elif opcion == "5":
            id = int(input("ID del registro a eliminar: "))
            if delete(id):
                print(f"Registro con ID {id} eliminado exitosamente.")
            else:
                print(f"No se encontró ningún registro con ID: {id}")
                
        elif opcion == "6":
            print("¡Hasta pronto!")
            break
            
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
menu()
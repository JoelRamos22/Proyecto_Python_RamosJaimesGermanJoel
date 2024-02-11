import json
import time 
def Coordinador_Opciones(opcion):
    while True:
        if opcion == 1:
            print(" ============================== ")
            print("")
            print("\n ¿ Que listado desea conocer ?")
            print("")
            print(" ============================== ")
            listado = input (" Trainers / Campers : ")
            print ("")
            print(" ================================= ")
            if listado.lower() == "trainers": 
                Lista_Trainers()
                break
            elif listado.lower() == "campers": 
                Lista_Participantes()
                break
        elif opcion == 2:
            print(" ========================================= ")
            print("|                                        |")
            print("|  Bienvenido a la opción para asignar   |")
            print("|                 notas                  |")
            print("|                                        |")
            print(" ========================================= ")
            print("") 
            AsignarPruebasN()
            break 
        elif opcion == 3:
            print (" Que desea Registrar : ")
            print ("")
            respuestas = input ( " Trainer / Camper : ")
            print ("")
            if respuestas.lower() == "trainer": 
                print(" ========================================= ")
                print("|                                        |")
                print("|  Bienvenido a la opción para registrar |")
                print("|                 Trainers               |")
                print("|                                        |")
                print(" ========================================= ")
                print("") 
                Registrar_Trainers()
                break
            elif respuestas.lower() == "camper":  
                print(" ========================================= ")
                print("|                                        |")
                print("|  Bienvenido a la opción para registrar |")
                print("|                 estudiantes            |")
                print("|                                        |")
                print(" ========================================= ")
                print("") 
                Registrar_Estudiantes()
                break
        elif opcion == 4:
            Registrar_Notas()
        elif opcion == 5:
            Añadir_Rutas()
        elif opcion == 6:
            print("\nSaliendo...")
            break 

def Lista_Participantes():
    print("Entrando a la lista de Estudiantes Inscritos:")
    print("")

    with open('estudiantes.json', 'r') as estudiantes_file:
        estudiantes_data = json.load(estudiantes_file)

    num_estudiantes = len(estudiantes_data[1]["estudiantesInscritos"])
    estudiantes_por_pagina = 5
    num_paginas = (num_estudiantes // estudiantes_por_pagina) + 1

    pagina_actual = 0

    while pagina_actual < num_paginas:
        print(f"Página {pagina_actual + 1}/{num_paginas}:")
        print("╔════════════════════════════════════╗")
        print("║         LISTA DE ESTUDIANTES       ║")
        print("╠════════════════════════════════════╣")
        for estudiante in estudiantes_data[1]["estudiantesInscritos"][pagina_actual * estudiantes_por_pagina:(pagina_actual + 1) * estudiantes_por_pagina]:
            print("║ Nombre:", estudiante["nombres"])
            print("║ Apellidos:", estudiante["apellidos"])
            print("║ Identificación:", estudiante["identificacion"])
            print("║ Dirección:", estudiante["direccion"])
            print("║ Acudiente:", estudiante["acudiente"])
            print("║ Teléfonos:")
            print("║   Celular:", estudiante["telefonos"]["celular"])
            print("║   Fijo:", estudiante["telefonos"]["fijo"])
            print("║ Estado:", estudiante["estado"])
            print("╠════════════════════════════════════╣")

        if pagina_actual == 3:
            respuesta = input("Presione Enter para continuar o escriba 'salir' para regresar al menú anterior: ").lower()
            if respuesta == 'salir':
                break
        else:
            input("Presione Enter para continuar...")
        
        pagina_actual += 1

    # Una vez que se sale del bucle, regresamos al menú principal
    print("¿ Desea ver la lista de estudiantes Cursando el ciclo ?") 
    print ("")
    respuesta = input()
    if respuesta.lower() == "si" : 
        Lista_Participantes_Cursando()
    else : 
        print ("")
        print (" Saliendo...")
        return 
    return
def Lista_Participantes_Cursando():
    print("Entrando a la lista de Estudiantes Cursando el ciclo :")
    print("")

    with open('estudiantes.json', 'r') as estudiantes_file:
        estudiantes_data = json.load(estudiantes_file)

    num_estudiantes = len(estudiantes_data[0]["estudiantesCursados"])
    estudiantes_por_pagina = 5
    num_paginas = (num_estudiantes // estudiantes_por_pagina) + 1

    pagina_actual = 0

    while pagina_actual < num_paginas:
        print(f"Página {pagina_actual + 1}/{num_paginas}:")
        print("╔════════════════════════════════════╗")
        print("║         LISTA DE ESTUDIANTES       ║")
        print("╠════════════════════════════════════╣")
        for estudiante in estudiantes_data[0]["estudiantesCursados"][pagina_actual * estudiantes_por_pagina:(pagina_actual + 1) * estudiantes_por_pagina]:
            print("║ Nombre:", estudiante["nombres"])
            print("║ Apellidos:", estudiante["apellidos"])
            print("║ Identificación:", estudiante["identificacion"])
            print("║ Dirección:", estudiante["direccion"])
            print("║ Acudiente:", estudiante["acudiente"])
            print("║ Teléfonos:")
            print("║   Celular:", estudiante["telefonos"]["celular"])
            print("║   Fijo:", estudiante["telefonos"]["fijo"])
            print("║ Estado:", estudiante["estado"])
            print("╠════════════════════════════════════╣")
            
        if pagina_actual == 3:
            respuesta = input("Presione Enter para continuar o escriba 'salir' para regresar al menú anterior: ").lower()
            if respuesta == 'salir':
                break
        else:
            input("Presione Enter para continuar...")
        pagina_actual += 1 
    return
def Lista_Trainers() : 
    print("Entrando a la lista de Trainers:")
    print("") 
    
    with open('trainers.json', 'r') as trainers_file:
        trainers_data = json.load(trainers_file) 
        
    num_trainers = len(trainers_data)
    trainer_Por_pagina = 2
    num_paginas = (num_trainers // trainer_Por_pagina) + 1
    
    pagina_actual = 0 
    
    while pagina_actual < num_paginas:
        print(f"Página {pagina_actual + 1}/{num_paginas}:")
        print("╔════════════════════════════════════╗")
        print("║         LISTA DE TRAINERS          ║")
        print("╠════════════════════════════════════╣")
        for trainer in trainers_data[pagina_actual * trainer_Por_pagina:(pagina_actual + 1) * trainer_Por_pagina]:
            print("║ Nombre:", trainer["nombre"])
            print("║ Apellidos:", trainer["apellidos"])
            print("║ Identificación:", trainer["identificacion"])
            print("║ Especialidad", trainer["Especialidad"])
            print("║ Celular:", trainer["Celular"])
            print("╠════════════════════════════════════╣")

        if pagina_actual == num_paginas - 1:
            respuesta = input("Presione Enter para continuar o escriba 'salir' para regresar al menú anterior: ").lower()
            if respuesta.lower() == 'salir':
                break
        else:
            input("Presione Enter para continuar...")
        
        pagina_actual += 1
    return
def AsignarPruebasN(): 
    with open('estudiantes.json', 'r') as estudiantes_file: 
        estudiantes_data = json.load(estudiantes_file)
    
    for estudiante in estudiantes_data[1]['estudiantesInscritos'] : 
        print(" ═══════════════════════════════════════════════════════")
        print(f"      Ingrese la nota del estudiante: {estudiante['nombres']}")
        print(" ═══════════════════════════════════════════════════════")
        print ("")
        while True:
            prueba = int(input(" Nota (0-100): "))
            print ("")
            if 0 <= prueba <= 100:
                estudiante['Prueba'] = prueba
                break
            else:
                print(" Por favor, ingrese una nota válida (entre 0 y 100).")
                print("")
        if prueba > 60 : 
            print ("")
            print (" El estudiante ha pasado la prueba de registro ")
            estudiante['estado'] = " Aprobado  "
            
    with open('estudiantes.json', 'w') as estudiantes_file: 
        json.dump(estudiantes_data, estudiantes_file, indent=4)
    print ("")
    print (" Las notas de la prueba han sido añadidas exitosamente ")
    print (" ======================================================")
    return 
def Registrar_Estudiantes() : 
    with open ('estudiantes.json', 'r') as estudiantes_file : 
        data_estudiantes = json.load(estudiantes_file)
    print ("")    
    print (" ¿ Desea añadir algun estudiante ? ")
    print ("")
    print (" ==============================================")
    print ("")
    while True :
        respuesta = input (" si o no : ")
        if respuesta.lower() == "si" : 
            print ("")
            print (" ==============================================")
            print ("")
            print (" Ingrese los datos del estudiante")
            print ("")
            print (" ==============================================")
            print ("")
            Estudiante = {
                'identificacion' : input("identificacion : "),
                'nombres' : input("nombres : "),
                'apellidos' : input("apellidos : "),
                'direccion' : input("direccion : "),
                'acudiente' : input("acudiente : "),
                'telefonos' : { 
                        'celular' : input("celular : "),
                        'fijo' : input("fijo : ")
                        }
                }
            data_estudiantes[1]["estudiantesInscritos"].append(Estudiante) 
            
            with open ('estudiantes.json', 'w') as estudiantes_file :
                json.dump(data_estudiantes, estudiantes_file, indent=4)
            
            print ("") 
            print (" ESTUDIANTE AÑADIDO CON EXITO ")
                
            print ("")
            print (" ==============================================")
            print ("")
            print (" ¿ Desea añadir otro estudiante ?")
            print ("")
        elif respuesta.lower() == "no": 
            print (" Volviendo al menu...")
            break
    return
def Registrar_Trainers(): 
    with open ('trainers.json', 'r') as trainers_file : 
        data_trainers = json.load(trainers_file) 
    
    print ("")    
    print (" ¿ Desea añadir algun Trainer ? ")
    print ("")
    print (" ==============================================")
    print ("")
    while True : 
        respuesta = input (" si o no : ")
        print ("")
        if respuesta.lower() == "si" : 
            nuevo_Trainer = {
                "identificacion" : input (" Identificacion : "),
                "nombre" : input ( " Nombres : "),
                "apellidos" : input (" Apellidos :  "),
                "Especialidad" : input ( " Especialidad : "),
                "horario" : input (" Horario : "),
                "Celular" : input ( " Celular : ")
            }
            data_trainers.append(nuevo_Trainer)
        
            with open ('trainers.json', 'w') as trainers_file : 
                json.dump(data_trainers, trainers_file, indent=4) 
            print ("") 
            print (" TRAINER AÑADIDO CON EXITO ")
            print ("")
            print (" ==============================================")
            print ("")
            print (" ¿ Desea añadir otro Trainer ?")
            print ("")
        elif respuesta.lower() == "no": 
            print (" Volviendo al menu...")
            break  
    return


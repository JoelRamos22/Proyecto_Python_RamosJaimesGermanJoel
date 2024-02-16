import json
import time 
def Coordinador_Opciones(opcion):   
    while True:
        if opcion == 1:
            print("\n ¿ Que listado desea conocer ?".rjust(20))
            print("")
            print ("=====================================".rjust(20))
            print ("")
            listado = input (" Trainers / Campers : ".rjust(20))
            print ("")
            print ("=====================================".rjust(20))
            if listado.lower() == "trainers": 
                Lista_Trainers()
                break
            elif listado.lower() == "campers": 
                Lista_Participantes()
                break
        elif opcion == 3:
            print(" ========================================= ".center(120))
            print("|                                        |".center(120))
            print("|  Bienvenido a la opción para asignar   |".center(120))
            print("|                 notas                  |".center(120))
            print("|                                        |".center(120))
            print(" ========================================= ".center(120))
            print("") 
            AsignarPruebasN()
            break 
        elif opcion == 2:
            print (" Que desea Registrar : ".rjust(20))
            print ("")
            respuestas = input ( " Trainer / Camper : ".rjust(20))
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
            print("  ╔════════════════════════════════════╗  ".center(120))
            print("  ║            MENÚ RUTAS              ║  ".center(120))
            print("  ╠════════════════════════════════════╣  ".center(120))
            print("  ║ 1. Crear Rutas                     ║  ".center(120))
            print("  ║ 2. Asignar Rutas                   ║  ".center(120))
            print("  ║ 3. Ver Rutas                       ║  ".center(120))
            print("  ║ 4. Salir                           ║  ".center(120))
            print("  ╚════════════════════════════════════╝  ".center(120))
            print("") 
            opciones = int(input( " Ingrese la opcion que Desea usar : ".rjust(20)))
            print ("")
            print ("=====================================".rjust(20))
            Rutas(opciones)
            break 
        elif opcion == 5:
            print ("")
            print(" ========================================= ".center(120))
            print("|                                        |".center(120))
            print("|  Bienvenido a la opción de             |".center(120))
            print("|                 Matriculas             |".center(120))
            print("|                                        |".center(120))
            print(" ========================================= ".center(120))
            print("") 
            Matriculas()
            break
        elif opcion == 6:
            print ("")
            print(" Saliendo... ".rjust(20))
            print ("")
            break
        else  : 
            print ("\n Error, ingrese una opcion valida ".rjust(20))
            print ("")
            continue
        


def Lista_Participantes():
    print ("")
    print("Entrando a la lista de Estudiantes Inscritos:".rjust(20))
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
    print ("")
    print("¿ Desea ver la lista de estudiantes Cursando el ciclo ?".rjust(20)) 
    print ("")
    respuesta = input()
    if respuesta.lower() == "si" : 
        Lista_Participantes_Cursando()
    else : 
        print ("")
        print (" Saliendo...".rjust(20))
        return 
    return
def Lista_Participantes_Cursando():
    print ("")
    print("Entrando a la lista de Estudiantes Cursando el ciclo :".rjust(20))
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
    print ("")
    print("Entrando a la lista de Trainers:".rjust(20))
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
        print(" ═══════════════════════════════════════════════════════".rjust(20))
        print(f"      Ingrese la nota del estudiante: {estudiante['nombres']}".rjust(20))
        print(" ═══════════════════════════════════════════════════════".rjust(20))
        print ("")
        while True:
            prueba = int(input(" Nota (0-100): ".rjust(20)))
            print ("")
            if 0 <= prueba <= 100:
                estudiante['Prueba'] = prueba
                break
            else:
                print(" Por favor, ingrese una nota válida (entre 0 y 100):".rjust(20))
                print("")
        if prueba > 60 : 
            print ("")
            print (" El estudiante ha pasado la prueba de registro ".rjust(20))
            estudiante['estado'] = "Aprobado"
            
    with open('estudiantes.json', 'w') as estudiantes_file: 
        json.dump(estudiantes_data, estudiantes_file, indent=4)
    print ("")
    print (" Las notas de la prueba han sido añadidas exitosamente ".rjust(20))
    print ("=====================================".rjust(20))
    return 
def Registrar_Estudiantes() : 
    with open ('estudiantes.json', 'r') as estudiantes_file : 
        data_estudiantes = json.load(estudiantes_file)
    print ("")    
    print (" ¿ Desea añadir algun estudiante ? ".rjust(20))
    print ("")
    print ("=====================================".rjust(20))
    print ("")
    while True :
        respuesta = input (" si o no : ".rjust(20))
        if respuesta.lower() == "si" : 
            print ("")
            print ("=====================================".rjust(20))
            print ("")
            print (" Ingrese los datos del estudiante".rjust(20))
            print ("")
            print ("=====================================".rjust(20))
            print ("")
            Estudiante = {
                'identificacion' : (int(input("identificacion : "))),
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
            print (" ESTUDIANTE AÑADIDO CON EXITO ".rjust(20))
                
            print ("")
            print ("=====================================".rjust(20))
            print ("")
            print (" ¿ Desea añadir otro estudiante ?".rjust(20))
            print ("")
        elif respuesta.lower() == "no": 
            print (" Volviendo al menu...".rjust(20))
            break
    return
def Registrar_Trainers(): 
    with open ('trainers.json', 'r') as trainers_file : 
        data_trainers = json.load(trainers_file) 
    
    print ("")    
    print (" ¿ Desea añadir algun Trainer ? ".rjust(20))
    print ("")
    print ("=====================================".rjust(20))
    print ("")
    while True : 
        respuesta = input (" si o no : ")
        print ("")
        if respuesta.lower() == "si" : 
            nuevo_Trainer = {
                "identificacion" : int(input (" Identificacion : ")),
                "nombre" : input ( " Nombres : "),
                "apellidos" : input (" Apellidos :  "),
                "Especialidad" : input ( " Especialidad : "),
                "horario" : input (" Horario : (diurno, matutino, nocturno) : "),
                "Celular" : input ( " Celular : ")
            }
            data_trainers.append(nuevo_Trainer)
        
            with open ('trainers.json', 'w') as trainers_file : 
                json.dump(data_trainers, trainers_file, indent=4) 
            print ("") 
            print (" TRAINER AÑADIDO CON EXITO ".rjust(20))
            print ("")
            print ("=====================================".rjust(20))
            print ("")
            print (" ¿ Desea añadir otro Trainer ?".rjust(20))
            print ("")
        elif respuesta.lower() == "no": 
            print (" Volviendo al menu...".rjust(20))
            break  
    return
def Rutas(opcion): 
    if opcion == 1 : 
        with open ('Rutas.json', 'r') as rutas_file : 
            data_rutas = json.load(rutas_file) 
        print(" ========================================= ".center(120))
        print("|                                        |".center(120))
        print("|  Bienvenido a la opción para Crear     |".center(120))
        print("|                 Rutas                  |".center(120))
        print("|                                        |".center(120))
        print(" ========================================= ".center(120))
        print("") 
        print(" ¿Desea añadir una nueva Ruta? ".rjust(20))
        print("")
        while True : 
            respuesta = input ( " si o no : ".rjust(20))
            if respuesta.lower() == "si" : 
                print ("")
                print ("=====================================".rjust(20))
                print ("")
                print (" Ingrese el nombre de la nueva Ruta".rjust(20))
                print ("")
                print ("=====================================".rjust(20))
                print ("")
                nombre = input()
                nueva_ruta = {
                    nombre : []
                }
                data_rutas.append(nueva_ruta)
                print ("")
                print ("  NUEVA AÑADIDA EXITO  ".rjust(20))
                print ("")
                print ("=====================================".rjust(20))
                with open ('Rutas.json', 'w') as rutas_file :
                    json.dump(data_rutas, rutas_file, indent=4)
            elif respuesta.lower() == "no": 
                print ("")
                print (" Volviendo al menu...".rjust(20))
                break

    elif opcion == 2:
        with open('Rutas.json', 'r') as rutas_File:
            data_rutas = json.load(rutas_File)
        with open('estudiantes.json','r') as estudiantes_File : 
            data_estudiantes = json.load(estudiantes_File) 
        print(" ========================================= ".center(120))
        print("|                                        |".center(120))
        print("|  Bienvenido a la opción para Asignar   |".center(120))
        print("|                 Rutas                  |".center(120))
        print("|                                        |".center(120))
        print(" ========================================= ".center(120))
        print("") 
        while True:
            print("") 
            print(" ¿Desea añadir un estudiante? ".rjust(20))
            print("") 
            respuesta = input(" si o no: ".rjust(20))
            print ("")
            if respuesta.lower() == "si":
                print(" Estudiantes disponibles : ".rjust(20))
                print ("")
                for estudiante in data_estudiantes[1]['estudiantesInscritos']:
                    if estudiante["estado"] == "Aprobado": 
                        print ("")
                        print("║ Nombre:", estudiante["nombres"])
                        print("║ Apellidos:", estudiante["apellidos"])
                        print("║ Identificación:", estudiante["identificacion"])
                        print("║ Dirección:", estudiante["direccion"])
                        print("║ Acudiente:", estudiante["acudiente"])
                        print("║ Teléfonos:")
                        print("║    Celular:", estudiante["telefonos"]["celular"])
                        print("║    Fijo:", estudiante["telefonos"]["fijo"])
                        print("║ Estado:", estudiante["estado"])
                        print ("")
                print ("=====================================".rjust(20))
                print ("")
                print (" Las rutas disponibles son : ".rjust(20))
                print ("")
                print ("=====================================".rjust(20))
                print ("")
                for ruta in data_rutas : 
                    for key, values in ruta.items() : 
                        print (f" Ruta: {key} ")
                        print ("")
                print ("")
                ruta_Name = input("¿En qué ruta desea añadir el estudiante? : ".rjust(20)).strip()
                print ("")
                estudiante_Id=(int(input("Identificacion del estudiante: ".rjust(20))))
                print ("")
                ruta_Encontrada = False 
                for ruta in data_rutas:
                    if ruta_Name in ruta :
                        print ("=====================================".rjust(20))
                        print ("")
                        print ("      Ruta encontrada ".rjust(20))
                        print ("")
                        print ("=====================================".rjust(20))
                        ruta_Encontrada = True
                        for estudiantes in data_estudiantes[1]['estudiantesInscritos']:
                            if estudiantes['identificacion'] == estudiante_Id: 
                                print ("")
                                print ("   Estudiante encontrado".rjust(20))
                                print ("")
                                print ("=====================================".rjust(20))
                                ruta[ruta_Name].append(estudiantes)
                                print ("")
                                print ("  Estudiante añadido a la ruta ".rjust(20))
                                print ("")
                                print ("=====================================".rjust(20))
                                with open ('Rutas.json', 'w') as rutas_file :
                                    json.dump(data_rutas, rutas_file, indent=4)
                                Trainer_Ruta()
                                break
                        if ruta_Encontrada == False :
                            print ("")
                            print (" Ruta no encontrada ".rjust(20))
            
            elif respuesta.lower() == "no": 
                print ("")
                Trainer_Ruta()
                print ("")
                print (" Volviendo al menu... ".rjust(20))
                print ("")
                break
    
    elif opcion == 3 :          
        with open ('Rutas.json','r') as rutas_file : 
            data_rutas = json.load(rutas_file) 
        
        for ruta in data_rutas:
            for nombre_ruta, estudiantes in ruta.items():
                print(f"Ruta: {nombre_ruta}")
                if not estudiantes:
                    print ("")
                    print("No hay estudiantes asignados a esta ruta.".rjust(20))
                    print ("")
                    print ("========================================".rjust(20))
                else:
                    print("Estudiantes asignados a esta ruta:".rjust(20))
                    print ("")
                    for estudiante in estudiantes:
                        print(f"  - Nombre: {estudiante['nombres']}")
                        print(f"    Apellidos: {estudiante['apellidos']}")
                        print(f"    Identificación: {estudiante['identificacion']}")
                        print(f"    Dirección: {estudiante['direccion']}")
                        print(f"    Acudiente: {estudiante['acudiente']}")
                        print(f"    Teléfonos:")
                        print(f"      Celular: {estudiante['telefonos']['celular']}")
                        print(f"      Fijo: {estudiante['telefonos']['fijo']}")
                        print(f"    Estado: {estudiante['estado']}")
                        print(f"    Prueba: {estudiante['Prueba']}")
                        print ("")
                        print ("=========================================================")
                        break
    elif opcion == 4 : 
        print ("")
        print ("saliendo...".rjust(20))
    return
def Matriculas() :
    with open('estudiantes.json','r') as estudiantes_File : 
        data_estudiantes = json.load(estudiantes_File) 
    with open('rutas.json','r') as rutas_File : 
        data_rutas = json.load(rutas_File)
    with open('Trainers.json','r') as trainers_File :  
        data_trainers = json.load(trainers_File)
    with open('salones.json','r') as salones_File : 
        data_salones = json.load(salones_File)
    while True : 
        print ("")
        print ("=====================================".rjust(20))
        print ("")
        respuesta = input (" ¿ Desea crear un nuevo grupo ? : ".rjust(20))
        print ("")
        print ("=====================================".rjust(20))
        if respuesta.lower() == "si" :
            print ("") 
            print ("=====================================".rjust(20))
            print ("")
            print (" | Ingrese el nombre del grupo  :   |".rjust(20))
            print ("")
            print ("=====================================".rjust(20))
            print ("")
            nuevo_grupo = {
                "nombre" : input("\n Nombre del grupo : "), 
                "horario" : input ("\n Horario del grupo (diurno, matutino, nocturno) : "),
                "Inicio" : input("\n Fecha de inicio de estudios grupo formato --/--/-- : "), 
                "Final" : input ("\n Final de los estudios del grupo formato --/--/-- : "),
                "estudiantes" : []
                
            }
            print ("")
            print (" TRAINERS DISPONIBLES : ".rjust(20) )
            print ("")
            num_trainers = len(data_trainers)
            trainer_Por_pagina = 2
            num_paginas = (num_trainers // trainer_Por_pagina) + 1
            pagina_actual = 0 
    
            while pagina_actual < num_paginas:
                print(f"Página {pagina_actual + 1}/{num_paginas}:")
                print("╔════════════════════════════════════╗")
                print("║         LISTA DE TRAINERS          ║")
                print("╠════════════════════════════════════╣")
                for trainer in data_trainers[pagina_actual * trainer_Por_pagina:(pagina_actual + 1) * trainer_Por_pagina]:
                    print("║ Nombre:", trainer["nombre"])
                    print("║ Apellidos:", trainer["apellidos"])
                    print("║ Identificación:", trainer["identificacion"])
                    print("║ Especialidad:", trainer["Especialidad"])
                    print("║ Horario:", trainer["horario"])
                    print("║ Celular:", trainer["Celular"])
                    print("╠════════════════════════════════════╣")

                if pagina_actual == num_paginas - 1:
                    respuesta = input(" Presione Enter para continuar ").lower()
                    if respuesta.lower() == 'salir':
                        print ("")
                        print ("=====================================".rjust(20))
                        print ("")
                        break
                    else : 
                        print ("")
                        print ("=====================================".rjust(20))
                        print ("")
                else:
                    input(" Presione Enter para continuar... ")
                pagina_actual += 1
                
            TrainerP = (int(input(" Ingrese la identificacion del trainer que sera el encargado del grupo : ".rjust(20))))
            validacion = False
            for trainer in data_trainers : 
                if trainer["identificacion"] == TrainerP and trainer["horario"] == nuevo_grupo['horario']: 
                    nuevo_grupo["trainer"] = trainer
                    print ("")
                    print ("=====================================".rjust(20))
                    print ("")
                    print ("        TRAINER ENCONTRADO           ".rjust(20))
                    print ("")
                    print ("=====================================".rjust(20))
                    validacion = True
                    break
            if(validacion == False): 
                    print ("")
                    print ("=====================================".rjust(20))
                    print ("")
                    print ("        TRAINER NO DISPONIBLE         ".rjust(20))
                    print ("")
                    print ("=====================================".rjust(20))
                    return
            imprimir_Estudiantes = True
            if imprimir_Estudiantes == True :
                num_estudiantes = len(data_estudiantes[1]["estudiantesInscritos"])
                estudiantes_por_pagina = 5
                num_paginas = (num_estudiantes // estudiantes_por_pagina) + 1
                pagina_actual = 0
                while pagina_actual < num_paginas:
                    print(f"Página {pagina_actual + 1}/{num_paginas}:")
                    print("╔════════════════════════════════════╗")
                    print("║         LISTA DE ESTUDIANTES       ║")
                    print("╠════════════════════════════════════╣")
                    for estudiante in data_estudiantes[1]["estudiantesInscritos"][pagina_actual * estudiantes_por_pagina:(pagina_actual + 1) * estudiantes_por_pagina]:
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
                        respuesta = input(" Presione Enter para continuar : ").lower()
                        print ("")
                        if respuesta.lower() == 'salir':
                            print ("")
                            break
                        else : 
                            print ("")
                    else:
                        print ("")
                        input("Presione Enter para continuar...")
                    pagina_actual += 1
            print ("") 
            print ("=======================================".rjust(20))
            print ("")
            print (" ¿Desea añadir un estudiante al  grupo?  :   ".rjust(20))
            print ("")
            print ("=======================================".rjust(20))
            print ("")
            capacidad_salon = 33 
            while True: 
                respuesta1 = input (" si o no : ".rjust(20))
                print ("")
                if respuesta1 == "si": 
                    Estudiante_Id = int(input(" Identificacion del estudiante : "))
                    for estudiante in data_estudiantes[1]["estudiantesInscritos"]: 
                        if Estudiante_Id == estudiante['identificacion'] and estudiante['estado'] == "Aprobado" :
                            nuevo_grupo['estudiantes'].append(estudiante)
                            capacidad_salon = capacidad_salon - 1 
                            print ("")
                            print ("=====================================".rjust(20))
                            print ("")
                            print ("        Estudiante Encontrado         ".rjust(20))
                            print ("")
                            print ("=====================================".rjust(20))
                            print ("")
                            print (f" Capacidad actualizada del salon actualizada : {capacidad_salon}")
                            print ("")
                            print (" ¿ Desea añadir otro estudiante ? ")
                            print ("")
                            print ("=====================================".rjust(20))
                            if capacidad_salon == 0 : 
                                print ("")
                                print ("=====================================".rjust(20))
                                print ("")
                                print ("      CAPACIDAD DEL SALON EXCEDIDA     ".rjust(20))
                                print ("")
                                print ("=====================================".rjust(20))
                                print ("")
                                break
                if respuesta1 == "no": 
                            break
            print ("")
            print ("=====================================".rjust(20))
            print ("")
            print ("¿A que salon desea añadir el nuevo grupo? :  ".rjust(20))
            print ("")
            print ("=====================================".rjust(20))
            print ("")
            print (" Lista De Salones Disponibles : ".rjust(20))
            for salon in data_salones : 
                print ("")
                print (salon["nombre"]) 
            print ("")
            salon_Name = input (" Ingrese el nombre del salon al que quiere agregar el grupo : ".rjust(20))
            for salon in data_salones :
                if salon["nombre"] == salon_Name : 
                    salon["grupos"].append(nuevo_grupo)
                    print ("")
                    print ("=====================================".rjust(20))
                    print ("")
                    print ("        SALON ENCONTRADO           ".rjust(20))
                    print ("")
                    print ("=====================================".rjust(20))
                    print ("")
                    print ( "       NUEVO GRUPO AÑADIDO    ".rjust(20))
                    break
        elif respuesta.lower() == "no" :
            print ("")
            print (" Volviendo al menu... ".rjust(20))
            print ("")
            break
        with open ('Salones.json', 'w') as salones_file : 
            json.dump(data_salones, salones_file, indent=4)
    return

def Trainer_Ruta () : 
    with open ('Trainers.json', 'r') as trainer_file : 
        data_trainer = json.load(trainer_file)
    with open ('Rutas.json', 'r') as rutas_file : 
        data_rutas = json.load(rutas_file) 
        
    while True : 
        print ("")
        respuesta = input(" ¿Desea añadir algun trainer? : ".rjust(20))
        print ("")
        if respuesta.lower() == "si": 
            for ruta in data_rutas : 
                for  key, values in ruta.items() : 
                    print ("")
                    print ( f" Ruta :  {key}".rjust(20))
                    print ("")
            Ruta_Name = input (" Ingrese el nombre de la ruta : ".rjust(20))
            ruta_encontrada = False  
            for ruta in data_rutas : 
                if Ruta_Name in ruta : 
                    print ("")
                    print ("=====================================".rjust(20))
                    print ("")
                    print ("          RUTA ENCONTRADA           ".rjust(20))
                    print ("")
                    print ("=====================================".rjust(20))
                    print ("") 
                    ruta_encontrada = True 
                    trainer_encontrado = False 
                    Id_trainer = int(input(" Ingrese la identificacion del trainer : ".rjust(20)))
                    for trainer in data_trainer : 
                        if Id_trainer == trainer["identificacion"] : 
                            print ("")
                            print ("=====================================".rjust(20))
                            print ("")
                            print ("        TRAINER  ENCONTRADO            ".rjust(20))
                            print ("")
                            print ("=====================================".rjust(20))
                            print ("") 
                            trainer_encontrado = True 
                            nuevo_trainer = {
                                'trainer' : []
                            }
                            nuevo_trainer['trainer'].append(trainer)
                            ruta[Ruta_Name].append(nuevo_trainer)
                            print ("")
                            print (" TRAINER AÑADIDO CON EXITO".rjust(20))
                            print ("")
                            with open ('Rutas.json', 'w') as rutas_file : 
                                json.dump(data_rutas, rutas_file, indent=4)
                    if (trainer_encontrado == False) :
                        print ("")
                        print ("=====================================".rjust(20))
                        print ("")
                        print ("        TRAINER NO DISPONIBLE         ".rjust(20))
                        print ("")
                        print ("=====================================".rjust(20))
                        print ("")
                        break 
            if ruta_encontrada == False :
                print ("")
                print ("=====================================".rjust(20))
                print ("")
                print ("        RUTA NO ENCONTRADA           ".rjust(20))
                print ("")
                print ("=====================================".rjust(20))
                break
        elif respuesta.lower() == "no" :
            print ("")
            print (" Volviendo al menu... ".rjust(20))
            print ("")
            break
    return
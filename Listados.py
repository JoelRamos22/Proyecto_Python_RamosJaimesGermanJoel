import json 
def Listados_Opciones (opcion): 
    while True : 
        try : 
            if opcion == 1 : 
                print ("")
                print (" ================================================================  ".center(120))
                print ("")
                print ("  Bienvenido a la opcion para ver  el listado de campers inscritos ".center(120))
                print ("")
                print (" ================================================================ ".center(120))
                print ("") 
                Lista_Inscritos()
                break 
            elif opcion == 2 : 
                print ("")
                print (" =====================================================================  ".center(120))
                print ("")
                print ("  Bienvenido a la opcion para ver los campers que aprobaron la prueba    ".center(120))
                print ("")                             
                print (" =====================================================================  ".center(120))
                print ("") 
                Mostrar_Prueba()
                break
            elif opcion == 3 : 
                print ("")
                print (" ==================================================================  ".center(120))
                print ("")
                print ("         Bienvenido a la opcion para ver los Trainers Trabajando    ".center(120))
                print ("")
                print (" ================================================================== ".center(120))
                print ("") 
                Mostrar_Trainer()
                break
            elif opcion == 4 :
                print ("")
                print (" ==================================================================  ".center(120))
                print ("")
                print ("   Bienvenido a la opcion para ver los Campers con Bajo Rendimiento   ".center(120))
                print ("")
                print (" ================================================================== ".center(120))
                print ("")
                Bajo_Rendimiento()
                break
            elif opcion == 5 :
                print ("")
                print (" ======================================================================  ".center(120))
                print ("")
                print ("       Bienvenido a la opcion para Listar las Rutas y sus asociados       ".center(120))
                print ("")
                print (" ====================================================================== ".center(120))
                print ("") 
                imprimir_estudiantes_y_entrenadores()
                print ("")
                break
            elif opcion == 6 : 
                print ("")
                print (" ======================================================================  ".center(120))
                print ("")
                print ("     Bienvenido a la opcion para Listar las Estadisticas de los Modulo     ".center(120))
                print ("")
                print (" ====================================================================== ".center(120))
                print ("") 
                Estadisticas_Modulos()
                break
            elif opcion == 7 : 
                print ("")
                print (" ======================================================================  ".center(120))
                print ("")
                print ("   Bienvenido a la opcion para Listar los Campers en estado de riesgo     ".center(120))
                print ("")
                print (" ====================================================================== ".center(120))
                print ("") 
                Estado_Riesgo()
                break
            elif opcion == 8 : 
                print ("")
                print (" Saliendo...")
                break
        except Exception : 
            print ("")
            print (" ERROR INGRESE UNA OPCION VALIDAD " )
            print ("") 
            continue 
    return
def Lista_Inscritos(): 
    with open ('estudiantes.json', 'r') as estudiantes_file : 
        data_estudiantes = json.load(estudiantes_file) 
    while True : 
        print ("")
        respuesta = input(" ¿Desea saber que estudiantes estan inscritos? : ")
        print ("")
        print (" ======================================== ")
        if respuesta.lower() == "si" : 
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
                    respuesta = input("Presione Enter para continuar o escriba 'salir' para regresar al menú anterior: ").lower()
                    if respuesta == 'salir':
                        break
                else:
                    input("Presione Enter para continuar...")
        
                pagina_actual += 1
        elif respuesta.lower() == "no" :
            print ("")
            print (" Volviendo al menu... ")
            print ("")
            break
    return

def Mostrar_Prueba() : 
    with open ('estudiantes.json', 'r') as estudiantes_file : 
        data_estudiantes = json.load(estudiantes_file) 
        
    while True : 
        print ("")
        respuesta = input(" ¿Desea saber que estudiantes que aprobaron el examen inicial? : ")
        print ("")
        print (" ======================================== ")
        if respuesta.lower() == "si" : 
            
            for estudiante in data_estudiantes[1]["estudiantesInscritos"]: 
                if estudiante['estado'] == "Aprobado" : 
                    print ("")
                    print("║ Nombre:", estudiante["nombres"])
                    print("║ Apellidos:", estudiante["apellidos"])
                    print("║ Identificación:", estudiante["identificacion"])
                    print("║ Estado:", estudiante["estado"])
                    print("║ Estado:", estudiante["Prueba"])
                    print("╠════════════════════════════════════")
                    
        elif respuesta.lower() == "no" : 
            print ("")
            print (" Volviendo al menu... ")
            print ("")
            break 
    return 


def Mostrar_Trainer() :
    with open('trainers.json', 'r') as trainers_file:
        trainers_data = json.load(trainers_file) 
    while True : 
        print ("")
        respuesta = input(" ¿Desea saber que trainers trabajan? : ")
        print ("")
        print (" ======================================== ")
        if respuesta.lower() == "si" : 


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
        elif respuesta.lower() == "no" : 
            print ("")
            print (" saliendo... ")
            print ("")
            break 
    return

def Bajo_Rendimiento(): 
    with open ('Notas.json', 'r') as notas_file : 
        data_notas = json.load(notas_file) 
    while True : 
        print ("")
        respuesta = input(" ¿Desea saber que estudiantes cuentan con un bajo rendimiento academico? : ") 
        print ("") 
        if respuesta.lower() == "si": 
            for grupo in data_notas : 
                for estudiante in grupo['estudiantes'] :
                    for modulo in grupo['modulos'] : 
                        for nota in modulo['notas'] : 
                            if nota['NotaF'] < 60 : 
                                print ("")
                                print("║ Nombre:", estudiante["nombres"])
                                print("║ Apellidos:", estudiante["apellidos"])
                                print("║ Identificación:", nota["id_Estudiante"])
                                print("║ Modulo:", modulo["nombre"])
                                print("║ Nota filtro:", nota["NotaF"]) 
                                print ("")
        elif respuesta.lower() == "no" : 
            print ("")
            print (" Volviendo al menu... ")
            print ("")
            break
    return 

def imprimir_estudiantes_y_entrenadores():
    with open ('Rutas.json', 'r') as rutas_file : 
        data_rutas = json.load(rutas_file)
    while True : 
        print ("")
        respuesta = input(" ¿Desea saber qué Campers y Trainers trabajan en cada Ruta? : ")
        print ("")
        if respuesta.lower() == "si": 
            for modulo in data_rutas:
                for nombre_modulo, estudiantes_y_entrenadores in modulo.items():
                    print(f"Estudiantes y entrenadores en el módulo '{nombre_modulo}':")
                if not estudiantes_y_entrenadores:
                    print ("")
                    print("No hay Campers ni Trainers en este módulo.")
                    print ("")
                else:
                    for estudiante_o_entrenador in estudiantes_y_entrenadores:
                        if "identificacion" in estudiante_o_entrenador:
                            print("Estudiante:")
                            print(f"  Nombres: {estudiante_o_entrenador['nombres']}")
                            print(f"  Apellidos: {estudiante_o_entrenador['apellidos']}")
                            print(f"  Dirección: {estudiante_o_entrenador['direccion']}")
                            print(f"  Acudiente: {estudiante_o_entrenador['acudiente']}")
                        elif "trainer" in estudiante_o_entrenador:
                            trainer = estudiante_o_entrenador["trainer"][0]
                            print("Entrenador:")
                            print(f"  Nombre: {trainer['nombre']} {trainer['apellidos']}")
                            print(f"  Especialidad: {trainer['Especialidad']}")
                            print(f"  Horario: {trainer['horario']}")
                            print(f"  Celular: {trainer['Celular']}")
                    print()  
        elif respuesta.lower() == "no" : 
            print ("")
            print (" volviendo al menu... ")
            print ("")
            break 
    return

def Estadisticas_Modulos():
    with open('Notas.json', 'r') as notas_file:
        data_notas = json.load(notas_file)
    
    while True:
        print("")
        respuesta = input("¿Desea saber Cuales son las estadisticas de los Modulos?: ")
        print("")
        if respuesta.lower() == "si":
            # Crear un diccionario para almacenar la cantidad de estudiantes por módulo
            estudiantes_por_modulo = {}

            # Contar la cantidad de estudiantes en cada módulo
            for grupo in data_notas:
                for modulo in grupo['modulos']:
                    nombre_modulo = modulo['nombre']
                    cantidad_estudiantes = len(modulo['notas'])
                    estudiantes_por_modulo[nombre_modulo] = cantidad_estudiantes
            
            # Ordenar los módulos por la cantidad de estudiantes de manera descendente
            modulos_ordenados = sorted(estudiantes_por_modulo.items(), key=lambda x: x[1], reverse=True)

            # Mostrar la información de cada módulo
            for nombre_modulo, cantidad_estudiantes in modulos_ordenados:
                print(f"Módulo: {nombre_modulo}")
                print(f"Cantidad de Estudiantes: {cantidad_estudiantes}")
                print ("")
                for grupo in data_notas:
                    for modulo in grupo['modulos']:
                        if modulo['nombre'] == nombre_modulo:
                            print("Grupo:")
                            print ("")
                            print(f"  Nombre: {grupo['nombre']}")
                            print(f"  Horario: {grupo['horario']}")
                            print(f"  Inicio: {grupo['Inicio']}")
                            print(f"  Final: {grupo['Final']}")
                            print ("")
                            print("Trainer:")
                            print ("")
                            print(f"  Nombre: {grupo['trainer']['nombre']} {grupo['trainer']['apellidos']}")
                            print(f"  Especialidad: {grupo['trainer']['Especialidad']}")
                            print(f"  Horario: {grupo['trainer']['horario']}")
                            print(f"  Celular: {grupo['trainer']['Celular']}")
                            print ("")
                            print("Estudiantes:")
                            print ("")
                            for estudiante in modulo['notas']:
                                print(f"  Nombre: {estudiante['nombre']}")
                                print(f"    Nota Teórica: {estudiante['NotaT']}")
                                print(f"    Nota Práctica: {estudiante['NotaP']}")
                                print(f"    Nota Quizes: {estudiante['NotaQ']}")
                                print(f"    Nota Final: {estudiante['NotaF']}")
                                print ("")
                print("---------------------------------------")
                print ("")

        elif respuesta.lower() == "no":
            print("")
            print("Volviendo al menú principal...")
            break

def Estado_Riesgo():
    with open ('Notas.json', 'r') as notas_file : 
        data_notas = json.load(notas_file)
    for curso in data_notas:
        for estudiante in curso["estudiantes"]:
            estado = estudiante["estado"]
            if estado == "Riesgo (Expulsion)" or estado == "Riesgo (condicional)":
                print (" *********************************** ")
                print(f"\n ID: {estudiante['identificacion']}")
                print(f" Nombres: {estudiante['nombres']}")
                print(f"Apellidos: {estudiante['apellidos']}")
                print ("\n ///////////////////////////////////// ")
                print(f"\n Estado: {estudiante['estado']}")
                print("")

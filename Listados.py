import json 
def Listados_Opciones (opcion): 
    while True : 
        if opcion == 1 : 
            print ("")
            print (" ================================================================  ")
            print ("")
            print ("  Bienvenido a la opcion para ver  el listado de campers inscritos ")
            print ("")
            print (" ================================================================ ")
            print ("") 
            Lista_Inscritos()
            break 
        elif opcion == 2 : 
            print ("")
            print (" =====================================================================  ")
            print ("")
            print ("  Bienvenido a la opcion para ver los campers que aprobaron la prueba ")
            print ("")                             
            print (" =====================================================================  ")
            print ("") 
            Mostrar_Prueba()
            break
        elif opcion == 3 : 
            print ("")
            print (" ==================================================================  ")
            print ("")
            print ("         Bienvenido a la opcion para ver los Trainers Trabajando    ")
            print ("")
            print (" ================================================================== ")
            print ("") 
            Mostrar_Trainer()
            break
        elif opcion == 4 :
            print ("")
            print (" ======================================================================  ")
            print ("")
            print ("  Bienvenido a la opcion para Listar los Campers con bajo Rendimiento ")
            print ("")
            print (" ====================================================================== ")
            print ("") 
            Bajo_Rendimiento()
            break 
        elif opcion == 5 : 
            print ("")
            print (" ==================================================================  ")
            print ("")
            print ("      Bienvenido a la opcion Para listar estadisticas de modulos     ")
            print ("")
            print (" ================================================================== ")
            print ("") 
            Notas()
            break
        elif opcion == 6 : 
            print ("")
            print (" ==================================================================  ")
            print ("")
            print ("       Bienvenido a la opcion para Listar las Rutas y asociados       ")
            print ("")
            print (" ================================================================== ")
            print ("") 
            Notas()
            break
        elif opcion == 7 : 
            print ("")
            print (" Saliendo...")
            print ("")
            break
        else : 
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


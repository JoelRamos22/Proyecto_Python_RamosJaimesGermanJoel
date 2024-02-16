import json 
def Campers_Opciones(opciones) :
    while True : 
        if opciones == 1 : 
            print ("")
            print (" ================================================================  ")
            print ("")
            print ("   Bienvenido a la opcion para ver a que grupo ha sido asignado   ")
            print ("")
            print (" ================================================================ ")
            print ("") 
            Info()
            break 
        elif opciones == 2 : 
            print ("")
            print (" ==================================================================  ")
            print ("")
            print ("              Bienvenido a la opcion para Ver sus notas              ")
            print ("")
            print (" ==================================================================  ")
            print ("") 
            Notas()
            break
        elif opciones == 3 : 
            print ("")
            print (" ==================================================================  ")
            print ("")
            print ("          Bienvenido a la opcion para ver su estado actual           ")
            print ("")
            print (" ================================================================== ")
            print ("") 
            Estado()
            break
        elif opciones == 4 :
            print ("")
            print (" Saliendo...")
            break 
        else : 
            print ("")
            print (" ERROR INGRESE UNA OPCION VALIDAD " )
            print ("") 
            continue 
        
def Info(): 
    with open ('salones.json', 'r') as json_file: 
        data_salones = json.load(json_file)
    while True : 
        print ("")
        respuesta = input(" Hola estudiante, ¿Desea ver en donde esta asignado?: ")
        print ("")
        print (" ======================================== ")
        if respuesta.lower() == "si" : 
            print ("")
            Camper_Encontrado = False
            Id_Camper = int(input(" Ingrese su identificacion : "))
            for salon in data_salones : 
                for grupo in salon['grupos'] : 
                    for estudiante in grupo['estudiantes'] : 
                        if estudiante['identificacion'] == Id_Camper : 
                            Camper_Encontrado = True
                            print ("")
                            print (" ========================================= ")
                            print ("")
                            print (" Nombre : ", estudiante['nombres'] )
                            print (" Identificacion : ", estudiante['identificacion'] ) 
                            print ("")
                            print (" ******************************************* ")
                            print ("")
                            print (" Grupo Asignado -> ", grupo['nombre'])
                            print ("")
                            print (" ******************************************* ")
                            print ("")
                            for key, val  in grupo['trainer'].items() :
                                print (f"{key} : {val}")
                            break  
            if (Camper_Encontrado == False) :
                print ("")
                print (" ======================================= ")
                print ("")
                print ("     Informacion camper No encontrada     ")
                print ("")
                print (" ======================================== ")
                print ("") 
                return
        else : 
            print ("")
            print (" Volviendo al menu... ")
            print ("")
            break
        
def Notas() : 
    with open ('Notas.json', 'r') as notas_json : 
        data_notas = json.load(notas_json) 
    while True : 
        print ("")
        respuesta = input(" Hola estudiante, ¿Desea ver sus notas?: ")
        print ("")
        print (" ================================ ") 
        print ("")
        if respuesta.lower() == "si": 
            for grupo in data_notas: 
                for modulo in grupo['modulos'] : 
                    print ("")
                    print (f" modulo : {modulo['nombre']} ")
                    print ("")
                    print (" *********************************** ")
            print ("")
            modulo_Name = input (" Ingrese el nombre del modulo del que desea saber las notas : ")
            print ("")
            id_Camper = int (input (" Ingrese su identificacion : "))
            camper_encontrado = False 
            for grupo in data_notas: 
                for modulo in grupo['modulos'] : 
                    modulo_encontrado = False
                    if modulo_Name == modulo['nombre'] : 
                        modulo_encontrado = True
                        for nota in modulo['notas']: 
                            if id_Camper == nota['id_Estudiante'] : 
                                camper_encontrado = True 
                                for nota in modulo['notas']:  
                                    print ("")
                                    print (f" nombre : {nota['nombre']} ")
                                    print (f" Idenfiticacion : {nota['id_Estudiante']}")
                                    print ("")
                                    print ( " **************************************** ")
                                    print ("")
                                    print (f" Nota Prueba teorica : {nota['NotaT']} ") 
                                    print (f" Nota Prueba pracitca : {nota['NotaP']} ")
                                    print (f" Nota total Quiz : {nota['NotaQ']} ")
                                    print (f" Nota total Filtro : {nota['NotaF']} ")
                                    print ("") 
                                    print ( " **************************************** ")
                            if camper_encontrado == False: 
                                print ("")
                                print (" ======================================= ")
                                print ("")
                                print ("     Camper No encontrado     ")
                                print ("")
                                print (" ======================================== ")
                                print ("") 
                                return 
                        if (modulo_encontrado == False) : 
                            print ("")
                            print (" ======================================= ")
                            print ("")
                            print ("     Informacion modulo No encontrada     ")
                            print ("")
                            print (" ======================================== ")
                            print ("") 
                            return
        elif respuesta == "no": 
            print ("")
            print (" Volviendo al menu... ")
            print ("")
            break
    return

def Estado ():
    with open ('Notas.json', 'r') as notas_json : 
        data_notas = json.load(notas_json) 
    with open ('estudiantes.json', 'r') as estudiantes_json : 
        data_estudiantes = json.load(estudiantes_json) 
    while True : 
        print ("")
        respuesta = input(" Hola estudiante, ¿Desea conocer su estado actual?: ")
        print ("")
        print (" ================================ ") 
        print ("")
        if respuesta.lower() == "si": 
            pregunta = input ( "¿ Se encuentra usted inscrito, matriculado o cursando ? : ")
            print ("")
            if pregunta.lower() == "inscrito" : 
                estudian_encontrado = False 
                id_estudiante = int(input ( " Identificacion : "))
                for estudiante in data_estudiantes[1]['estudiantesInscritos'] : 
                    if estudiante['identificacion'] == id_estudiante : 
                        estudian_encontrado = True
                        print ("")
                        print (" ========================================= ")
                        print ("")
                        print (" Estado : ", estudiante['estado'])
                        print ("")
                        print (" ========================================= ")
                        print ("")
                        break
                if estudian_encontrado == False: 
                    print ("")
                    print (" ======================================= ")
                    print ("")
                    print ("     Estudiante No encontrado     ")
                    print ("")
                    print (" ======================================== ")
                    print ("") 
                    return 
            elif pregunta.lower() == "matriculado" : 
                curso_name = input ( " Nombre del curso : ")
                print ("")
                id_estudiante = int(input ( " Identificacion : "))  
                estudiante_encontrado = False 
                curso_encontrado = False 
                for grupo in data_notas : 
                    if grupo['nombre'] == curso_name : 
                        curso_encontrado = True
                        for estudiante in grupo['estudiantes'] : 
                            if estudiante['identificacion'] == id_estudiante : 
                                estudiante_encontrado = True
                                print ("")
                                print (" ========================================= ")
                                print ("")
                                print (" Estado : ", estudiante['estado'])
                                print ("")
                                print (" ========================================= ")
                                print ("")
                                break 
                        if estudiante_encontrado == False: 
                            print ("")
                            print (" ======================================= ")
                            print ("")
                            print ("     Estudiante No encontrado     ")
                            print ("")
                            print (" ======================================== ")
                            print ("") 
                            return
                    if curso_encontrado == False: 
                        print ("")
                        print (" ======================================= ")
                        print ("")
                        print ("     Curso No encontrado     ")
                        print ("")
                        print (" ======================================== ")
                        print ("") 
                        return 
            elif pregunta.lower() == "cursando" : 
                print ("")
                estudiantes_encontrado = False 
                id_estudiante = int(input ( " Identificacion : "))
                for estudiante in data_estudiantes[0]['estudiantesCursados'] : 
                    if estudiante['identificacion'] == id_estudiante : 
                        estudiantes_encontrado = True
                        print ("")
                        print (" ========================================= ")
                        print ("")
                        print (" Estado : ", estudiante['estado'])
                        print ("")
                        print (" ========================================= ")
                        print ("")
                        break
                if estudiantes_encontrado == False: 
                    print ("")
                    print (" ======================================= ")
                    print ("")
                    print ("     Estudiante No encontrado     ")
                    print ("")
                    print (" ======================================== ")
                    print ("") 
                    return
        elif respuesta == "no": 
            print ("")
            print (" Volviendo al menu... ")
            print ("")
            break
    return 
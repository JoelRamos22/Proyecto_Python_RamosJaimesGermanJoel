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
            Modulos()
            break
        elif opciones == 3 : 
            print ("")
            print (" ==================================================================  ")
            print ("")
            print ("          Bienvenido a la opcion para ver su estado actual           ")
            print ("")
            print (" ================================================================== ")
            print ("") 
            Notas()
            break
        elif opciones == 4 :
            print ("")
            print (" Saliendo...")
            print ("")
            break 
        else : 
            print ("")
            print (" ERROR INGRESE UNA OPCION VALIDAD " )
            print ("") 
            continue 
        
def Info(): 
    with open ('salones..json', 'r') as json_file: 
        data_salones = json.load(json_file)
    while True : 
        print ("")
        respuesta = input(" ¿ Desea saber la informacion de su curso ? : ")
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
                            print (" Nombre : ", estudiante['nombre'] )
                            print (" Identificacion : ", estudiante['identificacion'] ) 
                            print (" Grupo Asinago :", grupo['nombre'])
                            print (" trainer encargado : ", grupo['trainer'] )
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

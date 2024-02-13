import json 
def Trainer_Opciones (opcion): 
    while True : 
        if opcion == 1 : 
            print ("")
            print (" ================================================================  ")
            print ("")
            print ("   Bienvenido a la opcion para ver la informacion de su curso  ")
            print ("")
            print (" ================================================================ ")
            print ("") 
            Info_Curso()
            break 
        elif opcion == 2 : 
            print ("")
            print (" ==================================================================  ")
            print ("")
            print ("       Bienvenido a la opcion para Agregar modulos a su curso         ")
            print ("")
            print (" ==================================================================  ")
            print ("") 
            Modulos()
        elif opcion == 3 : 
            print ("")
            print (" ==================================================================  ")
            print ("")
            print ("   Bienvenido a la opcion para actualizar las notas de sus campers  ")
            print ("")
            print (" ================================================================== ")
            print ("") 
            Notas()
        elif opcion == 4 :
            print ("")
            print (" Saliendo...")
            print ("")
            break 
        else : 
            print ("")
            print (" ERROR INGRESE UNA OPCION VALIDAD " )
            print ("") 
            continue 

def Info_Curso(): 
    with open ('salones.json', 'r') as salones_file : 
        data_salones = json.load(salones_file) 
    with open ('Trainers.json', 'r') as Trainers_file : 
        data_trainers = json.load(Trainers_file) 
    print ("")
    respuesta = input(" ¿ Desea saber la informacion de su curso ? : ")
    print (" ======================================== ")
    while True : 
        if respuesta.lower() == "si" : 
            print ("")
            Id_Trainer = int(input(" Ingrese su identificacion : "))
            for trainer in data_trainers : 
                if trainer['identificacion'] == Id_Trainer : 
                    print ("")
                    print (" ======================================= ")
                    print ("")
                    print ("     Informacion Trainer Confirmada      ")
                    print ("")
                    print (" ======================================== ")
                    print ("") 
                    print (f" Bienvenido {trainer['nombre']}")
                    print ("")
            salon_name = input (" Ingrese el nombre del salon donde esta asignado su grupo : ")
            for salon in data_salones : 
                if salon['nombre'] == salon_name : 
                    print ("")
                    print (" ======================================= ")
                    print ("")
                    print ("             Salon Encontrado             ")
                    print ("")
                    print (" ======================================== ")
                    print ("")
                    Grupo_Name = input (" Ingrese el nombre de su grupo : ") 
                    for grupo in salon['grupos'] : 
                        if grupo['nombre'] == Grupo_Name : 
                            print ("")
                            print ("  ======================================= ")
                            print ("")
                            print ("            Grupo Encontrado               ")
                            print ("")
                            print ("  ======================================== ")
                            print ("") 
                            for keys, values in grupo : 
                                print (f" {keys} : {values} ")
                            break 
                print ("") 
        else : 
            print ("")
            print (" Volviendo al menu... ")
            print ("")
            break
    return
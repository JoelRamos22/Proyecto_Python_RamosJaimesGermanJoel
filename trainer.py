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
            break
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
    while True : 
        print ("")
        respuesta = input(" ¿ Desea saber la informacion de su curso ? : ")
        print ("")
        print (" ======================================== ")
        if respuesta.lower() == "si" : 
            print ("")
            trainer_encontrado = False
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
                    print (f"              ¡ Bienvenido {trainer['nombre']} !         ")
                    print ("")
                    trainer_encontrado = True
                    break
            if (trainer_encontrado == False) :
                print ("")
                print (" ======================================= ")
                print ("")
                print ("     Informacion Trainer No Encontrada     ")
                print ("")
                print (" ======================================== ")
                print ("") 
                return
            salon_encontrado = False
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
                    salon_encontrado = True
                    grupo_encontrado = False
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
                            grupo_encontrado = True
                            for key, value in grupo.items() : 
                                if key ==  'estudiantes' : 
                                    print (f" {key} : ")
                                    for estudiante in value : 
                                        print ( " =========================================== ")
                                        for k, v in estudiante.items() :
                                            print  (f"  {k.capitalize()}: {v}  ")
                                else : 
                                    print(f" - {key.capitalize()}: {value} ")
                                    print (" ***************************  ")
                            break 
                    if (grupo_encontrado == False) : 
                        print ("")
                        print ("  ======================================= ")
                        print ("")
                        print ("            Grupo No Encontrado              ")
                        print ("")
                        print ("  ======================================== ")
                        print ("")
                        return
            if (salon_encontrado == False) : 
                print ("") 
                print (" ======================================= ") 
                print ("")
                print ("             Salon No Encontrado             ")
                print ("")
                print (" ======================================== ")
                return
        else : 
            print ("")
            print (" Volviendo al menu... ")
            print ("")
            break
    return
def Modulos() : 
    with open ('salones.json', 'r') as salones_json : 
        data_salones = json.load(salones_json) 
    with open ('Notas.json',  'r') as notas_json : 
        data_notas = json.load(notas_json)
    pregunta = input (" nota : ( Si los datos de su grupo ya estan cargados escriba 'continuar' si no presione enter ) : ")
    print ("")
    if pregunta.lower() == "continuar" :
        print ("")
        CrearModulos()
        return
    while True :
        respuesta = input(" ¿ Desea añadir modulos de notas a  su curso ? : ")
        print ("")
        print (" =================================================== ")
        if respuesta.lower() == "si" : 
            print ("")
            print (" ¡ Okey, primero empecemos añadiendo la informacion de todo tu curso para poder empezar a crear los modulos :D ! ")
            print ("")
            salon_name = input (" Ingrese el nombre del salon donde esta asignado su grupo : ")
            salon_encontrado = False
            for salon in data_salones : 
                if salon['nombre'] == salon_name : 
                    print ("")
                    print (" ======================================= ")
                    print ("")
                    print ("             Salon Encontrado             ")
                    print ("")
                    print (" ======================================== ")
                    print ("")
                    salon_encontrado = True
                    grupo_encontrado = False
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
                            grupo_encontrado = True
                            grupo['modulos'] = []
                            data_notas.append(grupo)
                            print (" Los Datos de su grupo han sido añadidos correctamente ")
                            print ("")
                            with open ('Notas.json', 'w') as nota_json : 
                                json.dump(data_notas, nota_json, indent=4)
                            CrearModulos()
                            break
                    if (grupo_encontrado == False) : 
                        print ("")
                        print ("  ======================================= ")
                        print ("")
                        print ("            Grupo No Encontrado              ")
                        print ("")
                        print ("  ======================================== ")
                        print ("")
                        break
            if (salon_encontrado == False) :
                print ("") 
                print (" ========================================= ")
                print ("")
                print ("             Salon No Encontrado            ")
                print ("")
                print (" ========================================= ")
                break
        elif respuesta.lower() == "no" : 
            print ("")
            print (" Volviendo al menu... ")
            print ("")
            break 
    return

def CrearModulos(): 
    with open ('Notas.json', 'r' ) as nota_json :  
        data_notas = json.load(nota_json) 
    while True : 
        print (" ============================================== ")
        print ("")
        respuesta = input ("    ¿ Desea Crear un modulo ? :   ")
        print ("")
        if respuesta == "si" : 
            print ("")
            nombreG = input (" ¿ En que grupo desea crear el nuevo modulo ? : ")
            print ("")
            grupo_encontrado = False
            for nota in data_notas : 
                if nota['nombre'] == nombreG : 
                    print ("")
                    print (" =================================== ")
                    print ("")
                    nombre = input ("  Ingrese el nombre del modulo  :   ")
                    print ("")
                    print (" =================================== ") 
                    print ("")
                    nuevo_modulo = {
                        'nombre' : nombre, 
                        'notas' : []
                    }
                    nota['modulos'].append(nuevo_modulo)
                    print ("")
                    print (" =================================== " )
                    print ("") 
                    print (" Modulo Creado Correctamente ") 
                    print ("")
                    grupo_encontrado = True
                break 
            if (grupo_encontrado == False) :
                print ("")
                print (" =================================== ")
                print ("")
                print ("     | Grupo No Encontrado     |      ")
                print ("")
                print (" =================================== ")
                print ("")
                break
        elif respuesta.lower() == "no" :
            print ("")
            print (" Volviendo a la opcion de notas... ")
            print ("")
            break 
    with open ('Notas.json', 'w') as notas_file : 
        json.dump(data_notas, notas_file, indent=4)
    return
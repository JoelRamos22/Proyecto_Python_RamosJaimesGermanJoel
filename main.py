import menus 
import coordinador

while True: 
    try : 
        opc = menus.Menu_Principal() 
        if opc == 1 : 
            opc_Coordinador = menus.Menu_Coordinador() 
            coordinador.Coordinador_Opciones(opc_Coordinador)
        elif opc == 2 : 
            menus.Menu_Trainer()
        elif opc == 3 : 
            menus.Menu_Estudiantes()
        elif opc == 4 : 
            menus.Matriculas()
        if opc == 5 : 
            print ("\n saliendo...")
            break 
        else : 
            print ("\n Ingrese una opcion valida ")
            print ("")
            continue  
    except Exception : 
        print ("\n Error, ingrese un numero entero ")
        print ("")
        continue
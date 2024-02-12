import menus 
import coordinador

while True: 
        opc = menus.Menu_Principal() 
        if opc == 1 : 
            opc_Coordinador = menus.Menu_Coordinador() 
            coordinador.Coordinador_Opciones(opc_Coordinador)
        elif opc == 2 : 
            menus.Menu_Trainer()
        elif opc == 3 : 
            menus.Menu_Estudiantes()
        if opc == 4 : 
            print ("")
            print (" saliendo...")
            print ("")
            break
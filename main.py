import menus 
import coordinador
import trainer

while True: 
        opc = menus.Menu_Principal() 
        if opc == 1 : 
            opc_Coordinador = menus.Menu_Coordinador() 
            coordinador.Coordinador_Opciones(opc_Coordinador)
        elif opc == 2 : 
            opc_Trainer = menus.Menu_Trainer()
            trainer.Trainer_Opciones(opc_Trainer)
        elif opc == 3 : 
            menus.Menu_Estudiantes()
        elif opc == 4 : 
            print ("")
            print (" saliendo...")
            print ("")
            break
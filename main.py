import menus 
import coordinador
import trainer
import campers

while True: 
        opc = menus.Menu_Principal() 
        if opc == 1 : 
            opc_Coordinador = menus.Menu_Coordinador() 
            coordinador.Coordinador_Opciones(opc_Coordinador)
        elif opc == 2 : 
            opc_Trainer = menus.Menu_Trainer()
            trainer.Trainer_Opciones(opc_Trainer)
        elif opc == 3 : 
            opc_camper  = menus.Menu_Estudiantes()
            campers.Campers_Opciones(opc_camper)
        elif opc == 4 : 
            print ("")
            print (" saliendo...")
            print ("")
            break
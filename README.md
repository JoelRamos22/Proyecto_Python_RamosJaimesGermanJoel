# Proyecto Python German Joel Ramos 
</p> Aquí esta la informacion sobre mi proyecto, junto con instrucciones de como usarlo y una descripcion de su contenido :smile: .
 
------------

## Requerimientos a cumplir :alien::
El programa de seguimiento académico para CampusLands permite registrar la información de los campers inscritos en su programa intensivo de programación. Además, gestiona las rutas de entrenamiento, asigna campers a trainers, registra notas, y genera reportes. Algunas características principales incluyen:

- Registro de campers con información detallada.
- Gestión de rutas de entrenamiento como Ruta NodeJS, Ruta Java, etc.
- Roles de usuario para Camper, Trainer y Coordinador.
- Evaluación de campers con pruebas teóricas y prácticas.
- Identificación de campers en riesgo alto y bajo rendimiento.
- Reportes sobre campers, trainers y resultados por módulo.
- Este programa proporciona una solución completa para el seguimiento y gestión del proceso de formación en CampusLands.


------------

## Desarollo del proyecto:
El trabajo era de punto de vista libre, por lo cual elegí enforcarlo como una plataforma de gestión de notas real, donde hay roles y cada uno tiene sus distintas funciones. Para poder darle este enfoque, fue necesario utilizar varios archivos, los cuales listaré a continuación de forma resumida.

**modulos : **
- Main.py(Nuestro codigo principal donde ejecutaremos todo los programas)
- Menus.py(Las impresiones de nuestros menus, que se mostraran en nuestro codigo main)
- Coordinador.py(Las funciones del coordinador con bastantes de los requerimientos cumplidos)
- Trainer.py(Las funciones que podra cumplir el rol de trainer)
- camper.py(Las funciones que podra cumplir el rol de camper)
**
Archivos Json** :
- Rutas.json
- Salones.json
- Notas.json
- Estudiantes.json
- Trainer.json

###### * Nota :* 
*la permanencia de datos es necesaria para poder mantener un buen funcionamiento del codigo *

------------
### Main.py 
</p> Aqui estara nuestro codigo principal junto con un bucle while, todos los import necesarios. 
Ejemplo : 

```python
while True: 
    try: 
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
            opc_listado = menus.Lista_Reportes()
            Listados.Listados_Opciones(opc_listado)
        elif opc == 5 : 
            print ("") 
            respuesta = input(" ¿Desea salir del sistema? : ")
            if respuesta == "si": 
                print ("") 
                print (" saliendo... ") 
                print ("") 
                break
    except Exception : 
        print ("")
        print (" ERROR INGRESE UNA OPCION VALIDAD " )
        print ("") 
        continue
```


------------

### Menus.py 
Aqui vamos a generar las impresiones que seran importadas al codigo principal, ya que de esta forma garantizamos un mejor orden, solamente imprimimos un mensaje con las opciones. 
Ejemplo : 
```python
def Menu_Principal(): 
    print ("")
    print("╔════════════════════════════════════╗".center(120))
    print("║            MENÚ PRINCIPAL          ║".center(120))
    print("╠════════════════════════════════════╣".center(120))
    print("║ 1. Coordinador                     ║".center(120))
    print("║ 2. Trainer                         ║".center(120))
    print("║ 3. Camper                          ║".center(120))
    print("║ 4. Lista de Reportes               ║".center(120))
    print("║ 5. Salir                           ║".center(120))
    print("╚════════════════════════════════════╝".center(120))
    print ("")
    print ("=====================================".rjust(20))
    opc = int(input("\n Ingrese la opcion que desea usar : ".rjust(20)))
    print ("")
    print ("===================================== ".rjust(20))
    print ("")
    return opc 
```

------------

### Coordinador.py 
Con este modulo se cumpliran la mayoria de requisitos, ya que este contara con la opcion de las matriculas, añadir estudiantes, añadir trainer, registrar notas de la prueba inicial... etc todo esto mediante funciones para poder manejar mas facil su entendimiento, se utiliza un bucle while en casi todas las funciones para no obligar al usuario a salir y volver a entrar a la opcion cada vez que quiera modificar algo. 
Ejemplo : 

```python
def AsignarPruebasN(): 
    with open('estudiantes.json', 'r') as estudiantes_file: 
        estudiantes_data = json.load(estudiantes_file)
    
    for estudiante in estudiantes_data[1]['estudiantesInscritos'] : 
        print(" ═══════════════════════════════════════════════════════".rjust(20))
        print(f"      Ingrese la nota del estudiante: {estudiante['nombres']}".rjust(20))
        print(" ═══════════════════════════════════════════════════════".rjust(20))
        print ("")
        while True:
            prueba = int(input(" Nota (0-100): ".rjust(20)))
            print ("")
            if 0 <= prueba <= 100:
                estudiante['Prueba'] = prueba
                break
            else:
                print(" Por favor, ingrese una nota válida (entre 0 y 100):".rjust(20))
                print("")
        if prueba > 60 : 
            print ("")
            print (" El estudiante ha pasado la prueba de registro ".rjust(20))
            estudiante['estado'] = "Aprobado"
            
    with open('estudiantes.json', 'w') as estudiantes_file: 
        json.dump(estudiantes_data, estudiantes_file, indent=4)
    print ("")
    print (" Las notas de la prueba han sido añadidas exitosamente ".rjust(20))
    print ("=====================================".rjust(20))
    return
```

------------

##### * IMPORTANTE * :crying_cat_face:: 
**</p> * Todas las funciones con los modulos usan la misma estructura para acceder a cada opcion de su menu, esto con un bucle while para poder seleccionar una opcion de salida.* 
ejemplo : 
**
```python

def Campers_Opciones(opciones) :
    while True : 
        if opciones == 1 : 
            print ("")
            print (" ================================================================  ".center(120))
            print ("")
            print ("   Bienvenido a la opcion para ver a que grupo ha sido asignado   ".center(120))
            print ("")
            print (" ================================================================ ".center(120))
            print ("") 
            Info()
            break 
        elif opciones == 2 : 
            print ("")
            print (" ==================================================================  ".center(120))
            print ("")
            print ("              Bienvenido a la opcion para Ver sus notas              ".center(120))
            print ("")
            print (" ==================================================================  ".center(120))
            print ("") 
            Notas()
            break
        elif opciones == 3 : 
            print ("")
            print (" ==================================================================  ".center(120))
            print ("")
            print ("          Bienvenido a la opcion para ver su estado actual           ".center(120))
            print ("")
            print (" ================================================================== ".center(120))
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
```

------------

### Trainers.py 
Este modulo aunque con muchas menos opciones que el modulo de la coordinacion cuenta con unas funciones importantes para poder cumplir los requerimientos del trabajo, en este modulo se podran ver los cursos y estudiantes asignados al trainer, poder crear modulos de notas donde tambien podra tener una funcion para poder añadir notas a cada estudiante. 
Ejemplo : 
```python

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
            print (" Volviendo a la opcion anteior... ")
            print ("")
            break 
    with open ('Notas.json', 'w') as notas_file : 
        json.dump(data_notas, notas_file, indent=4)
    return
```
*Nota: *
</p> * En el modulo de matriculas se crea un grupo al cual se le podra asignar nuevos modulos por el trainer, cada grupo contiene fecha de finalizacion, fecha de inicio, nombre del grupo, trainer, estudiantes y etc...*

------------

### Campers.py 
</p> Los camper no podran modificar ni cambiar ningun valor en el codigo, solamente podran consultar informacion, su estado, sus notas, sus cursos no contaran con mas opciones. 
Ejemplo : 

```python
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
```

------------

## Permanencia de datos JSON :balloon:
</p> Para el correcto funcionamiento del codigo se necesita una permanencia de datos, para esto usaremos archivos json, con una estructura bastante similar pero con distintos cambios cada una, esto para poder manejar de mejor forma los datos en el codigo tomando asi mucho menos tiempo su manipulacion :tw-26a1:.

Un Ejemplo de los json usados podria ser el json para guardar las notas de los grupos creados : 

```python
[
    {
        "nombre": "u3",
        "horario": "diurno",
        "Inicio": "23/06/08",
        "Final": "27/06/11",
        "estudiantes": [
            {
                "identificacion": 1,
                "nombres": "p",
                "apellidos": "i",
                "direccion": "8",
                "acudiente": "o",
                "telefonos": {
                    "celular": "9",
                    "fijo": "4"
                },
                "Prueba": 80,
                "estado": "Riesgo (Expulsion)"
            }
        ],
        "trainer": {
            "identificacion": 12345,
            "nombre": "Juan",
            "apellidos": "mari\u00f1o",
            "Especialidad": "java",
            "horario": "diurno",
            "Celular": "317819"
        },

```

------------

### MUCHAS GRACIAS :dvd::
</p> Espero que esto te haya podido ayudar a comprender mi codigo de una forma mucho mas sencilla, este es mi primer proyecto :coffee: .

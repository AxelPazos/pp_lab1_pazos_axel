import re
import json


                
def leer_archivo(ruta:str)->list[dict]:
    """abre un archivo y lo guarda en una variable llamada diccionario
        admite un dato tipo path
        retorna una copia del arcivo
    """
    with open(ruta,"r") as archivo:
        diccionario = json.load(archivo)
    return diccionario
data = leer_archivo("C:\\Users\\Axel J. Pazos\\Desktop\\cosas para guardad\\Ejercicios python no guias\\dt.json")
lista_jugadores = data["jugadores"]



def ingresar_opcion(opciones:list) -> str:

    """
    solicita una opcion y verifica si esta esta en la lista de opciones
    admite un dato tipo lista de opciones
    retorna la opcion ingresada si es valida
    """
    while True:
        opcion = input(f"Ingresar una de las siguientes opciones: {opciones}").lower()
        if opcion not in opciones:
            print("Opción no válida. Inténtalo de nuevo.")
        else:
            return opcion


def validar_numeros_regex(patron:str)->int:
    """
    solicita un valor y lo valida con un patron de expresion regular
    admite un dato tipo patron con el que se valida el numero
    retorna el numero ingresado en numero entero
    """
    flag = True
    contenido = input("ingrese un valor")
    while flag:
        if re.search(patron,contenido) is None:
            contenido = input("opcion no valida reingrese el valor")
        else:
            flag = False
            return int(contenido)


def mostrar_jugadores_formateado(lista_jugadores:list[dict])->None:
    """
    imprime en pantalla con el formateo "Nombre Jugador : ----- Posicion :
    admite und ato tipo lista de jugadores
    no retorna nada
    """
    for jugador in lista_jugadores:
        print("Nombre Jugador :{0}---Posicion :{1}".format(jugador["nombre"],jugador["posicion"]))


def seleccionar_jugador_por_indice(lista_jugadores:list[dict])->dict:
    """
    La funcion pide un indice de un jugador y muestra en pantalla sus estadisticas
    admite un dato tipo lista de jugadores
    retorna una diccionario del jugador seleccionado y imprime las estadisticas de este"""
   
    mostrar_indice_jugador(lista_jugadores)
    indice_jugador = validar_numeros_regex(r"^[0-9]|1[0-1]$")
         
    if len(lista_jugadores) > 0:

        nombre_jugador = lista_jugadores[indice_jugador]["nombre"]
        #creo una variable con el nombre del jugador en string.
        jugador = lista_jugadores[indice_jugador]
        #guardo en una variable el jugador que voy a retornar para el punto 3.
        acumulador_estadisticas = ("{}\n".format(nombre_jugador))
        #inicializo un acumulador primero con el nombre del jugador uardado.
        estadisticas_dict = lista_jugadores[indice_jugador]["estadisticas"]
        #guardo un diccionario con las estadisticas del jugador seleccionado.  

        for clave,valor in estadisticas_dict.items():
                    #itero en la clave y valor del diccionario de estadisticas.
                    
                    formateo_print =("{0}: {1}\n".format(clave,valor))
                    acumulador_estadisticas += formateo_print
                    #le asigno a la variable formateo print un string formateado con la estadistica 
                    # y su valor al lado y lo voy agregando al 
                    # acumulador de string con un salto de linea                                                      
            
                    
    
        print("----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(acumulador_estadisticas)
        return jugador
    else:
        print("ERROR, lista vacia")


def mostrar_indice_jugador(lista_jugadores:list[dict])->None:
    """
    imprime los jugadores de una lista con su respectivo indice
    admite un dato tipo lista de jugadores
    no retorna nada
    """
    contador = -1
    for jugador in lista_jugadores:
        contador += 1
        print("{0}.{1}".format(contador,jugador["nombre"]))


def genera_texto_formateado(jugador_dict: dict)-> str:
    """
    Esta función toma un diccionario de las estadísticas de un jugador y devuelve una cadena formateada
    que contiene su nombre, posición y estadísticas
    admite un dato tipo diccionario del jugador
    retorna los datos en string para guardar
    """


    
    jugador_estadisticas = jugador_dict["estadisticas"]
    
    
    #agrego primedo nombre y posicion en las dos listas para luego agregar las estadisticas
    lista_claves = ["nombre", "posicion"]
    lista_valores = [jugador_dict["nombre"],jugador_dict["posicion"]]

    #itero en la clave y valor la lista de estadisticas y vos appendeando a la lista correspondieste todo en string
    for clave, valor in jugador_estadisticas.items():
        lista_claves.append(clave)
        lista_valores.append(str(valor))

    #une las dos listas por comas para el csv y deja la lista como str
    claves_str = ",".join(lista_claves)
    valores_str = ",".join(lista_valores)
    #une los dos str uno abao del otro dividido por comas
    datos_formateados_str = "{0}\n{1}".format(claves_str , valores_str)
    return datos_formateados_str


def guardar_archivo(ruta:str , contenido:str)->bool:
    """
    abre el archivo con w+ si no esxiste lo crea en la ruta especificada y escribe el contenido en este
    admite un dato tipo ruta y otro tipo contenido
    retorna True si el achivo fue creado 
    """
    with open(ruta , "w+") as archivo:
         byte = archivo.write(contenido)
    if byte > 0:
         return True
    else:
         print("Error al crear el archivo: {}".format(ruta))


def crear_lista_opciones(lista_jugadores:list,key:str)->list[str]:
    """crea una lista de opciones en string de la lista y key ingresados
    admite dos parametros uno tipo lista de jugadores y otro tipo key
    retorna una lista de opciones con elementos en str"""

    lista_opciones = []  

    for jugador in lista_jugadores:
        lista_opciones.append("{}".format(jugador[key]))  
    
    return lista_opciones


def ingresar_opcion(opciones: list) -> str:
    """pide y valida la opcion ingresada
    admite un dato tipo lista de opciones con el que se valida 
    retorna la opcion ingresada si esta es valida"""


    while True:
        if len(opciones) > 0:
        
            opcion =input("{}\ningrese una de las siguientes opciones:".format("\n".join(opciones))) 
            if opcion not in opciones:
                print("Opción no válida. Inténtalo de nuevo.")
            else:
                return opcion
        else:
            print("\nError, lista vacia\n")
            break


def mostrar_logros_jugador(lista_jugadores:list[dict])->float:
    """
    muestra los logros  del jugador seleccionado
    admite un dato tipo lista de jugadores   
    """
    
        
    opcion = ingresar_opcion(crear_lista_opciones(lista_jugadores,"nombre"))
    #valida que ingrese una de las opciones
    strig_logros = "\nLogros :\n"
    for jugador in lista_jugadores:
        if jugador["nombre"] == opcion:
            for logros in jugador["logros"]:
                strig_logros += f"{logros}\n"
    return strig_logros 
         

def calcular_promedio_en_estadisticas(lista_jugadores:list[dict],key:str)->float:
    """esta funcion calcula el promedio de valores en una lista con un diccionario con estadisticas 
        admite un parametro tipo lista y otro tipo key que que contiene los valores
        retorna un dato float que contiene el promedio total"""
    acumulador = 0
    contador = 0
    
    for jugador in lista_jugadores:       
            for clave,valor in jugador["estadisticas"].items():
                if clave == key:
            
                    acumulador += valor
                    contador += 1

        
    return acumulador/contador
            

def imprimir_datos_estadisticos_jugadores(lista_jugadores:list[dict],key:str)->None:
    """
    El codigo imprime en pantalla los datos estadisticos de los jugadores en la lista ingresada
    admite un dato tipo lista de jugadores y una key que sera la estadistica a imprimir
    no retorna nada imprime en pantalla
    """
    if len(lista_jugadores) > 0:
        print("Jugadores mayores valor ingresado :")
        for jugador in lista_jugadores:
            print("{0}, {1} : {2}".format(jugador["nombre"],key.replace("_"," "),jugador["estadisticas"][key],))

            
    else:
        print("ERROR, lista vacia")


def mostrar_salon_de_la_fama(lista_jugadores:list[dict]):
    """
    Solcita el nobre de un jugador y verifica si dicho jugador pertenece al miembro del salon de la fama de baloncesto
    admite un dato tipo lista de jugadores
    no retorna nada imprime en pantalla si el jugador pertenece o no al salon de la fama de baloncesto
    """
    
    opcion = ingresar_opcion(crear_lista_opciones(lista_jugadores,"nombre"))
    for jugador in lista_jugadores:
        if opcion == jugador["nombre"]:
            salon_fama = jugador["logros"][-1]
            if re.search(r"Miembro del Salon de la Fama del Baloncesto$",salon_fama) is not None:
                    print("------------------\n{0} Es miembro del salon de la fama\n------------------".format(jugador["nombre"]))
            else:
                     print("--------------\n{0} No es miembro del salon de la fama\n---------------".format(jugador["nombre"]))  
                   

def calcular_max_min_estadisticas(lista_jugadores:list,key:str,max_or_min:True)->str:
        """
        Calcula e impime el maximo o el minimo de una estadistica de los jugadores
        admite 3 datos uno tipo lista de jugador, otro tipo key:str el cual es la estadistica a calcular y un boolean para calcular maximo o minimo
        retorna el nombre del jugador maximo o minimo
        """
        valor_key_maximo = 0
        valor_key_minimo = float("inf")
        if len(lista_jugadores) > 0:
            if max_or_min == True:
                for jugador in lista_jugadores:
                    for clave,valor in jugador["estadisticas"].items():
                        if clave == key and valor > valor_key_maximo:
                            valor_key_maximo = valor
                            nombre_maximo = jugador["nombre"]
                print("\nEl jugador {1} tiene la mayor cantidad de {0} con un total de {2}\n".format(key.replace("_"," "), nombre_maximo, valor_key_maximo))

                return nombre_maximo

            elif max_or_min == False:
                for jugador in lista_jugadores:
                    for clave,valor in jugador["estadisticas"].items():
                        if clave == key and valor < valor_key_minimo:
                            valor_key_minimo = valor
                            nombre_minimo = jugador["nombre"]
                print("\nEl jugador {1} tiene la menor cantidad de {0} con un total de {2}\n".format(key.replace("_"," "), nombre_minimo, valor_key_minimo)) 
            
                return nombre_minimo
                    
            
                    

        else:
            print("ERROR, La lista esta vacia")


def filtrar_lista_mayor_que_un_valor(lista_jugadores:list,key:str)->list[dict]:
    """
    El código verifica si un valor dado ingresado por el usuario es un número, y si lo es, lo convierte en un número entero luego compara el valor dado con las estadisticas de los jugadores si lo superan (True) o estan debajo (False)
    admite 3 parametros, uno tipo lista de jugadores, otro la key o estadistica a comparar y el ultimo una bandera que indica supera el valor ingresado o no supera
    retorna una lista con los jugadores, nada imprime en pantalla aquellos jugadores validos""",
    if len(lista_jugadores) > 0:
           valor_ingresada = validar_numeros_regex(r"[0-9]+")
        
           lista_aux = []

           for jugador in lista_jugadores:
               for clave,valor in jugador["estadisticas"].items():
                    if clave == key and valor > valor_ingresada:
                        lista_aux.append(jugador)
                       

    
           return lista_aux     
                   


        
    else:
        print("ERROR, lista vacia")


def calcula_promedio_ignorando_al_peor(lista_jugadores:list,key:str)->None:
    """
    El código crea una nueva lista llamada "lista_aux" y luego elimina al jugador con el rendimiento más bajo en una estadística específica de la lista original de jugadores. Luego calcula el promedio de esa estadística para los jugadores restantes en la lista e imprime el resultado.
    Admite 2 parametros, uno tipo lista de jugadores y otro tipo key que es la estadistica a promediar
    No retorna nada imprime en pantalla el jugador ignorado, y el promedio calculado
    """
    lista_aux =[]
    print("Se ignorara al jugador con menor desempeño en (..{}..) a la hora de promediar".format(key.replace("_"," ")))
    nombre_menor  = calcular_max_min_estadisticas(lista_jugadores,key,False)
    for jugadores in lista_jugadores:
        if jugadores["nombre"] != nombre_menor:
            lista_aux.append(jugadores)
    print("El promedio total de {1} es {0}".format(calcular_promedio_en_estadisticas(lista_aux, key),key.replace("_"," ")))


def calcula_jugador_mas_logros(lista_jugadores:list)->str:
        """El código busca al jugador con más logros en una lista de jugadores y devuelve un string que indica el nombre del jugador con más logros.
        admite un dato tipo lista de jugadores
        retorna el nobre del jugador con mas logros
        """    
        logros_maximo = 0
        if len(lista_jugadores) > 0:
            for jugador in lista_jugadores:
                if len(jugador["logros"]) > logros_maximo:
                    logros_maximo = len(jugador["logros"])
                    nombre_maximo = jugador["nombre"]
            jugador_mas_logros = "El jugador con mas logros es {0}".format(nombre_maximo)
            return jugador_mas_logros


        else:
            print("ERROR, Lista vacia")


def nuevo_ordenar_equipo_por_posicion_nombre(lista_jugadores:list,nombre_o_posicio:str)->list[dict]:
    '''
    Ordena una lista de jugadores según la posicion o el nombre alfabeticamente
    Recibe una lista de jugadores y una key que evalua por que dato ordena
    Devuelve la lista ordenada
    '''
    rango_a = len(lista_jugadores)
    flag_swap = True
    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1
        for indice_A in range(rango_a):
                if  lista_jugadores[indice_A][nombre_o_posicio] > lista_jugadores[indice_A+1][nombre_o_posicio]:
                    lista_jugadores[indice_A],lista_jugadores[indice_A+1] = lista_jugadores[indice_A+1],lista_jugadores[indice_A]
                    flag_swap = True
    return lista_jugadores  


def main():
    jugador_encontrado = {}

    while True:
        print("Menú de opciones:")
        print("1. Mostrar lista de jugadores del Dream Team. ")
        print("2. Ver estadísticas completas de un jugador seleccionado ")
        print("3. Guardar estadísticas de un jugador en un archivo ")
        print("4. Buscar un jugador por nombre y mostrar sus logros ")
        print("5. Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre ")
        print("6. Verificar si un jugador es miembro del Salón de la Fama del Baloncesto ")
        print("7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales. ")
        print("8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo ")
        print("9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales ")
        print("10. Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.")
        print("11. Mostrar jugadores que promediaron más rebotes por partido que un valor dado. ")
        print("12. Mostrar jugadores que promediaron más asistencias por partido que un valor dado. ")
        print("13. Calcular y mostrar el jugador con la mayor cantidad de robos totales. ")
        print("14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales. ")
        print("15. Mostrar jugadores con un porcentaje de tiros libres superior a un valor dado ")
        print("16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido. ")
        print("17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos ")
        print("18. Mostrar jugadores con un porcentaje de tiros triples superior a un valor dado. ")
        print("19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas. ")
        print("20. Mostrar jugadores ordenados por posición en la cancha con un porcentaje de tiros de campo superior a un valor dado. ")
        print("21. BONUS ")
        print("22.exit")

        opcion = validar_numeros_regex(r"[1-9]|1[0-9]|2[0-2]")
        match opcion:
            case 1:
                mostrar_jugadores_formateado(lista_jugadores)
            case 2:
                 jugador_encontrado = (seleccionar_jugador_por_indice(lista_jugadores))               
            case 3:
                if jugador_encontrado:
                   #flag para que entre al punto 2 antes
                   texto_generado = genera_texto_formateado(jugador_encontrado)
                   #guarda el texto para guardar archivo                 
                   archivo_creado =guardar_archivo("jugador_estadistica.csv",texto_generado)
                   if archivo_creado:
                       print("\nEl archivo fue creado\n")
                else:
                    print("Primero debe entrar al punto 2")
            case 4:
                
                print(mostrar_logros_jugador(lista_jugadores))
            case 5:
                print("\nNOMBRES ORDENADOS ASCENDENTEMENTE:\n")
                lista_ordenada_nombres =(nuevo_ordenar_equipo_por_posicion_nombre(lista_jugadores,"nombre"))
                mostrar_indice_jugador(lista_ordenada_nombres)
        
                
                print("\nEl promedio total de los puntos por partido de cada jugador es {}:\n".format(calcular_promedio_en_estadisticas(lista_jugadores,"promedio_puntos_por_partido")))

            case 6:
                
                mostrar_salon_de_la_fama(lista_jugadores)
            case 7:
                calcular_max_min_estadisticas(lista_jugadores,"rebotes_totales",True)
            case 8:
                calcular_max_min_estadisticas(lista_jugadores,"porcentaje_tiros_de_campo",True)
            case 9:
                calcular_max_min_estadisticas(lista_jugadores, "asistencias_totales" ,True)
            case 10:
                lista_filtrada_puntos = filtrar_lista_mayor_que_un_valor(lista_jugadores,"promedio_puntos_por_partido")
                imprimir_datos_estadisticos_jugadores(lista_filtrada_puntos,"promedio_puntos_por_partido")
            case 11:
                 lista_filtrada_rebotes = filtrar_lista_mayor_que_un_valor(lista_jugadores,"promedio_rebotes_por_partido")
                 imprimir_datos_estadisticos_jugadores(lista_filtrada_rebotes,"promedio_rebotes_por_partido")
            case 12:
                lista_filtrada_asistencia =filtrar_lista_mayor_que_un_valor(lista_jugadores,"promedio_asistencias_por_partido")
                imprimir_datos_estadisticos_jugadores(lista_filtrada_asistencia,"promedio_asistencias_por_partido" )

            
            case 13:
                calcular_max_min_estadisticas(lista_jugadores,"robos_totales",True)
            case 14:
                calcular_max_min_estadisticas(lista_jugadores,"bloqueos_totales",True)
            case 15:
                 lista_filtrada_tiros_libre=filtrar_lista_mayor_que_un_valor(lista_jugadores,"porcentaje_tiros_libres")
                 imprimir_datos_estadisticos_jugadores(lista_filtrada_tiros_libre,"porcentaje_tiros_libres" )
            case 16:
                calcula_promedio_ignorando_al_peor(lista_jugadores,"promedio_puntos_por_partido")
            case 17:
                print(calcula_jugador_mas_logros(lista_jugadores))
            case 18:
                lista_filtrada_triples =filtrar_lista_mayor_que_un_valor(lista_jugadores,"porcentaje_tiros_triples")
                imprimir_datos_estadisticos_jugadores(lista_filtrada_triples ,"porcentaje_tiros_triples") 
            case 19:
                calcular_max_min_estadisticas(lista_jugadores,"temporadas",True)
            case 20:
                lista_filtrada_tiros_campo = filtrar_lista_mayor_que_un_valor(lista_jugadores,"porcentaje_tiros_de_campo")
                lista_ordenada             = nuevo_ordenar_equipo_por_posicion_nombre(lista_filtrada_tiros_campo,"posicion")
                mostrar_jugadores_formateado(lista_ordenada)               
                                                      
            case 21:
                print("Ejercicio sin hacer")
            case 22:
                print("Salida...")
                break




      
          

        
        
#Invocar al menu
main()







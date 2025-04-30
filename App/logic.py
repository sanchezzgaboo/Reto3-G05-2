import time
import os
import csv
import datetime
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.List import array_list as arr
from DataStructures.List import single_linked_list as sll
from DataStructures.Tree import bst_node as node

from DataStructures.Map import map_linear_probing as lp

data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {'all_crimes': None,
                'tree_by_date': None,
                'tree_by_age': None,
                "tree_by_area": None
                }
    catalog['all_crimes'] = arr.new_list()
    catalog['tree_by_date'] = bst.new_map()
    catalog['tree_by_age'] = bst.new_map()
    catalog["tree_by_area"] = bst.new_map()

    return catalog
# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    crimesfile = data_dir + filename
    input_file = csv.DictReader(open(crimesfile, encoding="utf-8"),
                                delimiter=",")
    time = 0
    start = get_time()
    for crime in input_file:
        add_crime(catalog, crime)
        #TODO MIRAR SI SON PRIMERAS 5 FECHAS y ULTIMAS OOO
    end = get_time()
    time = round(delta_time(start, end),3)
    return catalog["all_crimes"], time

# Añadir crimen al catalogo

def add_crime(catalog, crime):
    date = datetime.datetime.strptime(crime['DATE OCC'][:10], '%m/%d/%Y')
    area = crime["AREA NAME"].lower()

    arr.add_last(catalog['all_crimes'], crime)
    #TODO ANALIZAR SI SE DEBE HACER OTRO ARBOL PARA ORGANIZAR POR EDAD
    #TODO añadir al arbol y mirar como se añade el crimen, 
    # probablemente con llave Fecha y Valor hashtable (tipo de crimen -> crimenes_de_ese_tipo) tipo de crimen
    value_tree = bst.get(catalog['tree_by_date'], date)
    age_tree = bst.get(catalog['tree_by_age'], int(crime['Vict Age']))
    if value_tree:
        list_of_crimes_by_classification = lp.get(value_tree, crime['Part 1-2'])
        if list_of_crimes_by_classification:
            arr.add_last(list_of_crimes_by_classification, crime)
        else:
            list_of_crimes_by_classification = arr.new_list()
            arr.add_last(list_of_crimes_by_classification, crime)
            lp.put(value_tree, crime['Part 1-2'], list_of_crimes_by_classification)
    if not value_tree:
        value_tree = lp.new_map(1, 0.7)
        list_of_crimes_by_classification = arr.new_list()
        arr.add_last(list_of_crimes_by_classification, crime)
        lp.put(value_tree, crime['Part 1-2'], list_of_crimes_by_classification)
        bst.put(catalog['tree_by_date'], date, value_tree)
    if age_tree:
        list_of_crimes_by_classification = lp.get(age_tree, crime['Part 1-2'])
        if list_of_crimes_by_classification:
            arr.add_last(list_of_crimes_by_classification, crime)
        else:
            list_of_crimes_by_classification = arr.new_list()
            arr.add_last(list_of_crimes_by_classification, crime)
            lp.put(age_tree, crime['Part 1-2'], list_of_crimes_by_classification)
    if not age_tree:
        age_tree = lp.new_map(1, 0.7)
        list_of_crimes_by_classification = arr.new_list()
        arr.add_last(list_of_crimes_by_classification, crime)
        lp.put(age_tree, crime['Part 1-2'], list_of_crimes_by_classification)
        bst.put(catalog['tree_by_age'], int(crime['Vict Age']), age_tree)
    value_area_tree = bst.get(catalog["tree_by_area"], area)
    if value_area_tree != None:
        arr.add_last(value_area_tree, crime)
    else:
        value_area_tree = arr.new_list()
        arr.add_last(value_area_tree, crime)
        bst.put(catalog["tree_by_area"], area, value_area_tree)

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass
def sort_criteria_crimeFecha(element_1, element_2):
    '''Función de comparación por defecto para ordenar elementos.

    Compara dos elementos y retorna True si el primer elemento es 
    menor que el segundo y False en caso contrario.

    :param any element_1: Primer elemento a comparar.
    :param any element_2: Segundo elemento a comparar.
    :return bool: True si el primer elemento es menor que el segundo, False en caso contrario.
    '''
    is_sorted = False
    time1 = ""
    if len(element_1['TIME OCC']) == 1:
        time1 = f"00:0{element_1['TIME OCC']}:00"
    if len(element_1['TIME OCC']) == 2:
        time1 = f"00:{element_1['TIME OCC']}:00"
    if len(element_1['TIME OCC']) == 3:
        time1 = f"0{element_1['TIME OCC'][0]}:{element_1['TIME OCC'][1:3]}:00"
    if len(element_1['TIME OCC']) == 4:
        time1 = f"{element_1['TIME OCC'][0:2]}:{element_1['TIME OCC'][2:4]}:00"
    time2 = ""
    if len(element_2['TIME OCC']) == 1:
        time2 = f"00:0{element_2['TIME OCC']}:00"
    if len(element_2['TIME OCC']) == 2:
        time2 = f"00:{element_2['TIME OCC']}:00"
    if len(element_2['TIME OCC']) == 3:
        time2 = f"0{element_2['TIME OCC'][0]}:{element_2['TIME OCC'][1:3]}:00"
    if len(element_2['TIME OCC']) == 4:
        time2 = f"{element_2['TIME OCC'][0:2]}:{element_2['TIME OCC'][2:4]}:00"
    if datetime.datetime.strptime(f"{element_1['DATE OCC'][:10]} {time1}", '%m/%d/%Y %H:%M:%S') > datetime.datetime.strptime(f"{element_2['DATE OCC'][:10]} {time2}", '%m/%d/%Y %H:%M:%S'):
        is_sorted = True
    if datetime.datetime.strptime(f"{element_1['DATE OCC'][:10]} {time1}", '%m/%d/%Y %H:%M:%S') == datetime.datetime.strptime(f"{element_2['DATE OCC'][:10]} {time2}", '%m/%d/%Y %H:%M:%S'):
        if element_1['AREA'] <= element_2['AREA']:
            is_sorted = True
    return is_sorted

def req_1(catalog, fecha_inicial, fecha_final):
    """
    Listar los crímenes ocurridos entre dos fechas 
    Los parámetros de entrada de este requerimiento son: 
    • La fecha inicial del periodo a consultar (con formato "%Y-%m-%d"). 
    • La fecha final del periodo a consultar (con formato "%Y-%m-%d"). 
    """
    time = 0
    start = get_time()
    inicial = datetime.datetime.strptime(fecha_inicial, "%Y-%m-%d")
    
    final = datetime.datetime.strptime(fecha_final, "%Y-%m-%d")

    mapcrimes = bst.values(catalog['tree_by_date'], inicial, final)
    total = arr.new_list()
    for mapcrimesindex in range(arr.size(mapcrimes)):
        graves = lp.get(arr.get_element(mapcrimes, mapcrimesindex), "1")
        not_graves= lp.get(arr.get_element(mapcrimes, mapcrimesindex), "2")
        if graves:
            for index_crime in range(arr.size(graves)):
                arr.add_last(total, arr.get_element(graves, index_crime))
        if not_graves:
            for index_crime in range(arr.size(not_graves)):
                arr.add_last(total, arr.get_element(not_graves, index_crime))
    total = arr.shell_sort(total, sort_criteria_crimeFecha)
    end = get_time()
    time = round(delta_time(start, end),3)
    return total, time


def req_2(catalog, fecha_inicial, fecha_final):
    """
    Listar los crímenes graves resueltos, que fueron reportados 
    en un rango de fechas. 
    Los parámetros de entrada de este requerimiento son: 
    • La fecha inicial del periodo a consultar (con formato "%Y-%m-%d"). 
    • La fecha final del periodo a consultar (con formato "%Y-%m-%d"). 
    """
    time = 0
    start = get_time()
    inicial = datetime.datetime.strptime(fecha_inicial, "%Y-%m-%d")
    
    final = datetime.datetime.strptime(fecha_final, "%Y-%m-%d")
    
    mapcrimes = bst.values(catalog['tree_by_date'], inicial, final)
    total = arr.new_list()
    for mapcrimesindex in range(arr.size(mapcrimes)):
        graves = lp.get(arr.get_element(mapcrimes, mapcrimesindex), "1")
        not_graves = lp.get(arr.get_element(mapcrimes, mapcrimesindex), "2")
        if graves:
            for index_crime in range(arr.size(graves)):
                crime = arr.get_element(graves, index_crime)
                if crime["Status Desc"] != "Invest Cont":
                    arr.add_last(total, crime)
        if not_graves:
            for index_crime in range(arr.size(not_graves)):
                crime = arr.get_element(not_graves, index_crime)
                if crime["Status Desc"] != "Invest Cont":
                    arr.add_last(total, crime)
    #TODO ARREGLAR SORT TIEMPOS
    total = arr.shell_sort(total, sort_criteria_crimeFecha)
    end = get_time()
    time = round(delta_time(start, end),3)
    return total, time

def req_3(catalog, n, area):
    """
    Retorna el resultado del requerimiento 3
    """
    time = 0
    start = get_time()
    arbol_areas = catalog["tree_by_area"]
    crimenes = bst.get(arbol_areas, area)
    if crimenes != None:
        n = arr.size(crimenes)
        resultados = arr.merge_sort(crimenes, sort_by_reported) #Crear sort descendente reportados
    end = get_time()
    time = round(delta_time(start, end),3)
    return resultados, int(n), time
 
def sort_by_reported(element1, element2):
    rpt1 = datetime.datetime.strptime(element1['Date Rptd'], '%m/%d/%Y %H:%M:%S %p')
    rpt2 = datetime.datetime.strptime(element2['Date Rptd'], '%m/%d/%Y %H:%M:%S %p') 
    is_sorted = False
    if rpt1 > rpt2:
        is_sorted = True
    return is_sorted

def sort_criteria_crimeAge(element_1, element_2):
    '''Función de comparación por defecto para ordenar elementos.

    Compara dos elementos y retorna True si el primer elemento es 
    menor que el segundo y False en caso contrario.

    :param any element_1: Primer elemento a comparar.
    :param any element_2: Segundo elemento a comparar.
    :return bool: True si el primer elemento es menor que el segundo, False en caso contrario.
    '''
    is_sorted = False
    if element_1["Vict Age"] > element_2["Vict Age"]:
        is_sorted = True
    elif element_1["Vict Age"] == element_2["Vict Age"]:
        time1 = ""
        if len(element_1['TIME OCC']) == 1:
            time1 = f"00:0{element_1['TIME OCC']}:00"
        if len(element_1['TIME OCC']) == 2:
            time1 = f"00:{element_1['TIME OCC']}:00"
        if len(element_1['TIME OCC']) == 3:
            time1 = f"0{element_1['TIME OCC'][0]}:{element_1['TIME OCC'][1:3]}:00"
        if len(element_1['TIME OCC']) == 4:
            time1 = f"{element_1['TIME OCC'][0:2]}:{element_1['TIME OCC'][2:4]}:00"
        time2 = ""
        if len(element_2['TIME OCC']) == 1:
            time2 = f"00:0{element_2['TIME OCC']}:00"
        if len(element_2['TIME OCC']) == 2:
            time2 = f"00:{element_2['TIME OCC']}:00"
        if len(element_2['TIME OCC']) == 3:
            time2 = f"0{element_2['TIME OCC'][0]}:{element_2['TIME OCC'][1:3]}:00"
        if len(element_2['TIME OCC']) == 4:
            time2 = f"{element_2['TIME OCC'][0:2]}:{element_2['TIME OCC'][2:4]}:00"
        if datetime.datetime.strptime(f"{element_1['DATE OCC'][:10]} {time1}", '%m/%d/%Y %H:%M:%S') >= datetime.datetime.strptime(f"{element_2['DATE OCC'][:10]} {time2}", '%m/%d/%Y %H:%M:%S'):
            is_sorted = True
        
    return is_sorted
def req_4(catalog, num_a_consultar, edad_inicial, edad_final):
    """
    Consultar los N crímenes con víctimas en un rango de 
    edad dado y clasificarlos por gravedad (“Part 1-2") 
    Los parámetros de entrada de este requerimiento son: 
    • El número (N) de crímenes a consultar 
    • Edad inicial del rango a consultar (con formato entero en años) 
    • Edad final del rango a consultar (con formato entero en años) 
    """
    time = 0
    start = get_time()
    mapcrimes = bst.values(catalog['tree_by_age'], edad_inicial, edad_final)
    
    mapcrimesindex = arr.size(mapcrimes) - 1
    totalGrave = arr.new_list()
    
    #TODO MIRAR SI SE PUEDE COMPARAR RESULTADOS DE ARBOL FECHA CON RESULTADOS DE ARBOL EDAD PARA ORDENAR EN CASO DE EMPATE
    while mapcrimesindex >= 0:
        graves = lp.get(arr.get_element(mapcrimes, mapcrimesindex), "1")
        if graves:
            for index_crime in range(arr.size(graves)):
                crime = arr.get_element(graves, index_crime)
                arr.add_last(totalGrave, crime)
        mapcrimesindex-=1
    
    totalGrave = arr.shell_sort(totalGrave, sort_criteria_crimeAge) 
    totalNoGrave = arr.new_list()
        
    mapcrimesindex = arr.size(mapcrimes) - 1
    while mapcrimesindex >= 0:
        not_graves = lp.get(arr.get_element(mapcrimes, mapcrimesindex), "2")
        if not_graves:
            for index_crime in range(arr.size(not_graves)):
                crime = arr.get_element(not_graves, index_crime)
                arr.add_last(totalNoGrave, crime)
        mapcrimesindex -=1
    
    totalNoGrave = arr.shell_sort(totalNoGrave, sort_criteria_crimeAge) 
    
    for i in range(arr.size(totalNoGrave)):
        elemento = arr.get_element(totalNoGrave, i)
        arr.add_last(totalGrave, elemento)
    end = get_time()
    time = round(delta_time(start, end),3)
    return totalGrave, time
       
    


def req_5(catalog, num_a_consultar, fecha_inicial, fecha_final):
    """
    Consultar las N áreas con mayor cantidad de crímenes 
    no resueltos ocurridos en un rango de fechas 
    Los parámetros de entrada de este requerimiento son: 
    • La cantidad N de áreas a consultar 
    • La fecha inicial del periodo a consultar (con formato "%Y-%m-%d"). 
    • La fecha final del periodo a consultar (con formato "%Y-%m-%d").
    """
    inicial = datetime.datetime.strptime(fecha_inicial, "%Y-%m-%d")
    final = datetime.datetime.strptime(fecha_final, "%Y-%m-%d")
    all_dates = bst.keys(catalog['tree_by_date'], inicial, final)
    all_dates_values = bst.values(catalog['tree_by_date'], inicial, final)
    mapareas = lp.new_map(10, 0.7)
    asociacion_area_nombre = lp.new_map(10, 0.7) 
    total = 0
    for i in range(arr.size(all_dates)):
        valor_mes = arr.get_element(all_dates_values,i)
        no_resueltos = lp.get(valor_mes, "IC")
        if no_resueltos:
            for index_crime in range(arr.size(no_resueltos)):
                crime = arr.get_element(no_resueltos, index_crime)
                total += 1
                lista_area = lp.get(mapareas, crime['AREA'])
                if lista_area:
                    arr.add_last(lista_area, crime)
                else:
                    lista_area = arr.new_list()
                    arr.add_last(lista_area, crime)
                    lp.put(mapareas, crime['AREA'], lista_area)
                nombre = lp.get(asociacion_area_nombre, crime['AREA'])
                if not nombre:
                    lp.put(asociacion_area_nombre, crime['AREA'], crime['AREA NAME'])                     
    codigos_areas = lp.key_set(mapareas)
    listas_areas = lp.value_set(mapareas)
    lista_ordenar = arr.new_list()
    
    for i in range(arr.size(codigos_areas)):
        arr.add_last(lista_ordenar, {arr.get_element(codigos_areas, i): arr.get_element(listas_areas, i), "size": arr.size(arr.get_element(listas_areas, i)), "nombre": lp.get(asociacion_area_nombre, arr.get_element(codigos_areas, i))})
    
    lista_ordenar = arr.shell_sort(lista_ordenar, sort_criteria_crimeCode)                       
    return total, lista_ordenar

def req_6(catalog, num_a_consultar, sexo, mes):
    """
    Consultar las N áreas más seguras para un sexo, en un mes 
    específico del año 
    Los parámetros de entrada de este requerimiento son: 
    • El número N de áreas a consultar. 
    • El sexo por consultar 
    • El mes del año para realizar la consulta (como un entero)
    """
    time = 0
    start = get_time()
    inicial = datetime.datetime.strptime("2020-01-01", "%Y-%m-%d")
    final = datetime.datetime.strptime("2021-12-31", "%Y-%m-%d")
    all_dates = bst.keys(catalog['tree_by_date'], inicial, final)
    all_dates_values = bst.values(catalog['tree_by_date'], inicial, final)
    
    mapareas = lp.new_map(10, 0.7)
    asociacion_area_nombre = lp.new_map(10, 0.7) 
    anios = lp.new_map(2, 0.7) 
    total = 0
    for i in range(arr.size(all_dates)):
        fecha = arr.get_element(all_dates, i)
        month = fecha.month
        if month == int(mes):
            
            valor_mes = arr.get_element(all_dates_values,i)
            graves = lp.get(valor_mes, "1")
            not_graves = lp.get(valor_mes, "2")
            if graves:
                for index_crime in range(arr.size(graves)):
                    crime = arr.get_element(graves, index_crime)
                    if crime["Vict Sex"] == sexo:
                        total += 1
                        lista_area = lp.get(mapareas, crime['AREA'])
                       
                        if lista_area:
                            arr.add_last(lista_area, crime)
                        else:
                            lista_area = arr.new_list()
                            arr.add_last(lista_area, crime)
                            lp.put(mapareas, crime['AREA'], lista_area)
                        nombre = lp.get(asociacion_area_nombre, crime['AREA'])
                        if not nombre:
                            lp.put(asociacion_area_nombre, crime['AREA'], crime['AREA NAME'])
                        lista_fecha = lp.get(anios, crime['DATE OCC'][6:10])
                        if lista_fecha:
                            arr.add_last(lista_fecha, crime)
                        else:
                            lista_fecha = arr.new_list()
                            arr.add_last(lista_fecha, crime)
                            lp.put(anios, crime['DATE OCC'][6:10], lista_fecha)
            if not_graves:
                for index_crime in range(arr.size(not_graves)):
                    crime = arr.get_element(not_graves, index_crime)
                    if crime["Vict Sex"] == sexo:
                        total += 1
                        lista_area = lp.get(mapareas, crime['AREA'])
                        if lista_area:
                            arr.add_last(lista_area, crime)
                        else:
                            lista_area = arr.new_list()
                            arr.add_last(lista_area, crime)
                            lp.put(mapareas, crime['AREA'], lista_area)
                        nombre = lp.get(asociacion_area_nombre, crime['AREA'])
                        if not nombre:
                            lp.put(asociacion_area_nombre, crime['AREA'], crime['AREA NAME'])
                        lista_fecha = lp.get(anios, crime['DATE OCC'][6:10])
                        if lista_fecha:
                            arr.add_last(lista_fecha, crime)
                        else:
                            lista_fecha = arr.new_list()
                            arr.add_last(lista_fecha, crime)
                            lp.put(anios, crime['DATE OCC'][6:10], lista_fecha)
                            
    codigos_areas = lp.key_set(mapareas)
    listas_areas = lp.value_set(mapareas)
    lista_ordenar = arr.new_list()
    
    for i in range(arr.size(codigos_areas)):
        arr.add_last(lista_ordenar, {arr.get_element(codigos_areas, i): arr.get_element(listas_areas, i), "size": arr.size(arr.get_element(listas_areas, i)), "nombre": lp.get(asociacion_area_nombre, arr.get_element(codigos_areas, i))})
    
    lista_ordenar = arr.shell_sort(lista_ordenar, sort_criteria_crimeCode)  
    end = get_time()
    time = round(delta_time(start, end),3)                     
    return total, lista_ordenar, anios, time
    

def sort_criteria_crimeCode(element_1, element_2):
    '''Función de comparación por defecto para ordenar elementos.

    Compara dos elementos y retorna True si el primer elemento es 
    menor que el segundo y False en caso contrario.

    :param any element_1: Primer elemento a comparar.
    :param any element_2: Segundo elemento a comparar.
    :return bool: True si el primer elemento es menor que el segundo, False en caso contrario.
    '''
    is_sorted = False
    if element_1["size"] > element_2["size"]:
        is_sorted = True
    return is_sorted

def req_7(catalog, num_a_calcular, sexo, edad_inicial, edad_final):
    """
    Determinar los crímenes más comunes para las víctimas de 
    un sexo en un rango de edad dado 
    Los parámetros de entrada de este requerimiento son: 
    • El número N de los crímenes más comunes a calcular 
    • El sexo de la víctima 
    • Edad inicial del rango a consultar (con formato entero en años) 
    • Edad final del rango a consultar (con formato entero en años) 
    """
    time = 0
    start = get_time()
    mapcrimes = bst.values(catalog['tree_by_age'], edad_inicial, edad_final)
    mapcrimeskeys = bst.keys(catalog['tree_by_age'], edad_inicial, edad_final)
    
    
    mapcrimesindex = arr.size(mapcrimes) - 1
    crimenes = lp.new_map(10, 0.7)
    anios = lp.new_map(2, 0.7)
    total = 0
    
    while mapcrimesindex >= 0:
        graves = lp.get(arr.get_element(mapcrimes, mapcrimesindex), "1")
        if graves:
            for index_crime in range(arr.size(graves)):
                crime = arr.get_element(graves, index_crime)
                if crime["Vict Sex"] == sexo:
                    lista_crimenes = lp.get(crimenes, crime['Crm Cd'])
                    if lista_crimenes:
                        arr.add_last(lista_crimenes, crime)
                    else:
                        lista_crimenes = arr.new_list()
                        arr.add_last(lista_crimenes, crime)
                        lp.put(crimenes, crime['Crm Cd'], lista_crimenes)
                    lista_fecha = lp.get(anios, crime['DATE OCC'][6:10])
                    if lista_fecha:
                        arr.add_last(lista_fecha, crime)
                    else:
                        lista_fecha = arr.new_list()
                        arr.add_last(lista_fecha, crime)
                        lp.put(anios, crime['DATE OCC'][6:10], lista_fecha)
                    total += 1
        mapcrimesindex-=1
        
    mapcrimesindex = arr.size(mapcrimes) - 1
    while mapcrimesindex >= 0:
        not_graves = lp.get(arr.get_element(mapcrimes, mapcrimesindex), "2")
        if not_graves:
            for index_crime in range(arr.size(not_graves)):
                crime = arr.get_element(not_graves, index_crime)
                if crime["Vict Sex"] == sexo:
                    lista_crimenes = lp.get(crimenes, crime['Crm Cd'])
                    if lista_crimenes:
                        arr.add_last(lista_crimenes, crime)
                    else:
                        lista_crimenes = arr.new_list()
                        arr.add_last(lista_crimenes, crime)
                        lp.put(crimenes, crime['Crm Cd'], lista_crimenes)
                    lista_fecha = lp.get(anios, crime['DATE OCC'][6:10])
                    if lista_fecha:
                        arr.add_last(lista_fecha, crime)
                    else:
                        lista_fecha = arr.new_list()
                        arr.add_last(lista_fecha, crime)
                        lp.put(anios, crime['DATE OCC'][6:10], lista_fecha)
                    total += 1
                    
        mapcrimesindex -=1
    
    #FIND MAX
    listas_crimenes = lp.value_set(crimenes)
    codigos_crimenes = lp.key_set(crimenes)
    lista_ordenar = arr.new_list()
    
    for i in range(arr.size(codigos_crimenes)):
        arr.add_last(lista_ordenar, {arr.get_element(codigos_crimenes, i): arr.get_element(listas_crimenes, i), "size": arr.size(arr.get_element(listas_crimenes, i))})
    
    lista_ordenar = arr.shell_sort(lista_ordenar, sort_criteria_crimeCode)
    
    
    #TODO MIRAR SI ARREGLAR LOS MAPCRIMES PORQUE INCLUYEN EL OTRO SEXO
    end = get_time()
    time = round(delta_time(start, end),3)
    return total,mapcrimes, mapcrimeskeys,lista_ordenar,anios, time


def req_8(catalog, num_a_consultar, area, tipo):
    """
    Determinar los N crímenes más cercanos y lejanos 
    del mismo tipo que ocurren en otras áreas a partir de un área de interés. 
    Los parámetros de entrada de este requerimiento son: 
    • El número (N) de crímenes a consultar. 
    • Nombre del área de interés inicial. 
    • Tipo de crimen a consultar
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

import sys
from App import logic
from tabulate import tabulate

from DataStructures.Tree import binary_search_tree as bst
from DataStructures.List import array_list as arr
from DataStructures.List import single_linked_list as sll
from DataStructures.Tree import bst_node as node

from DataStructures.Map import map_linear_probing as lp

def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

#Imprimir N-registros
def print_data (cant_registros, resultado, DR_NO, Date_Rptd, DATE_OCC, TIME_OCC, AREA, AREA_NAME, Rpt_Dist_No, Part_12, Crm_Cd, Crm_Cd_Desc, Vict_Age, Vict_Sex, Vict_Descent, Premis_Cd, Premis_Desc, Status, Status_Desc, LOCATION, LAT, LON):
    variables = []
    headers = ["#"]
    
    if DR_NO == 1:
        headers.append("ID")
        variables.append("DR_NO")
    if Date_Rptd == 1:
        headers.append("Fecha Reportada Crimen")
        variables.append("Date Rptd")
    if DATE_OCC == 1:
        headers.append("Fecha Crimen")
        variables.append("DATE OCC")
    if TIME_OCC == 1:
        headers.append("Hora Crimen")
        variables.append("TIME OCC")
    if AREA == 1:
        headers.append("Nº Area")
        variables.append("AREA")
    if AREA_NAME == 1:
        headers.append("Nombre del Area")
        variables.append("AREA NAME")
    if Rpt_Dist_No == 1:
        headers.append("Subárea")
        variables.append("Rpt Dist No")
    if Part_12 == 1:
        headers.append("Class Crimen")
        variables.append("Part 1-2")
    if Crm_Cd == 1:
        headers.append("Código del Crimen")
        variables.append("Crm Cd")
    if Crm_Cd_Desc == 1:
        headers.append("Descripcioón Crimen")
        variables.append("Crm Cd Desc")
    if Vict_Age == 1:
        headers.append("Edad Víct.")
        variables.append("Vict Age")
    if Vict_Sex == 1:
        headers.append("Sexo Víct.")
        variables.append("Vict Sex")
    if Vict_Descent == 1:
        headers.append("Origen Étnico Víctima")
        variables.append("Vict Descent")
    if Premis_Cd == 1:
        headers.append("Código Estructura")
        variables.append("Premis Cd")
    if Premis_Desc == 1:
        headers.append("Descripción Lugar Crimen")
        variables.append("Premis Desc")
    if Status == 1:
        headers.append("Cd. Estado")
        variables.append("Status")
    if Status_Desc == 1:
        headers.append("Desc. Estado ")
        variables.append("Status Desc")
    if LOCATION == 1:
        headers.append("Dir. Crimen")
        variables.append("LOCATION")
    if LAT == 1:
        headers.append("Latitud")
        variables.append("LAT") 
    if LON == 1:
        headers.append("Longitud")
        variables.append("LON")   
    
    table = []
    cuenta = 0
    for i in range(0,cant_registros):
        reg = arr.get_element(resultado,i)
        cuenta += 1
        fila = [cuenta]
        for variable in variables:
            fila.append(reg[variable])
        table.append(fila)
    print(tabulate(table, headers, tablefmt="rounded_grid"))

#Funcion que solo imprime 5 registros con #registro
def print_multiple_data (inicio_cuenta, resultado, DR_NO, Date_Rptd, DATE_OCC, TIME_OCC, AREA, AREA_NAME, Rpt_Dist_No, Part_12, Crm_Cd, Crm_Cd_Desc, Vict_Age, Vict_Sex, Vict_Descent, Premis_Cd, Premis_Desc, Status, Status_Desc, LOCATION, LAT, LON):
    variables = []
    headers = ["#"]
    
    if DR_NO == 1:
        headers.append("ID")
        variables.append("DR_NO")
    if Date_Rptd == 1:
        headers.append("Fecha Reportada Crimen")
        variables.append("Date Rptd")
    if DATE_OCC == 1:
        headers.append("Fecha Crimen")
        variables.append("DATE OCC")
    if TIME_OCC == 1:
        headers.append("Hora Crimen")
        variables.append("TIME OCC")
    if AREA == 1:
        headers.append("Nº Area")
        variables.append("AREA")
    if AREA_NAME == 1:
        headers.append("Nombre del Area")
        variables.append("AREA NAME")
    if Rpt_Dist_No == 1:
        headers.append("Subárea")
        variables.append("Rpt Dist No")
    if Part_12 == 1:
        headers.append("Class Crimen")
        variables.append("Part 1-2")
    if Crm_Cd == 1:
        headers.append("Código del Crimen")
        variables.append("Crm Cd")
    if Crm_Cd_Desc == 1:
        headers.append("Descripcioón Crimen")
        variables.append("Crm Cd Desc")
    if Vict_Age == 1:
        headers.append("Edad Víct.")
        variables.append("Vict Age")
    if Vict_Sex == 1:
        headers.append("Sexo Víct.")
        variables.append("Vict Sex")
    if Vict_Descent == 1:
        headers.append("Origen Étnico Víctima")
        variables.append("Vict Descent")
    if Premis_Cd == 1:
        headers.append("Código Estructura")
        variables.append("Premis Cd")
    if Premis_Desc == 1:
        headers.append("Descripción Lugar Crimen")
        variables.append("Premis Desc")
    if Status == 1:
        headers.append("Cd. Estado")
        variables.append("Status")
    if Status_Desc == 1:
        headers.append("Desc. Estado ")
        variables.append("Status Desc")
    if LOCATION == 1:
        headers.append("Dir. Crimen")
        variables.append("LOCATION")
    if LAT == 1:
        headers.append("Latitud")
        variables.append("LAT") 
    if LON == 1:
        headers.append("Longitud")
        variables.append("LON")  
    
    table = []
    cuenta = inicio_cuenta - 1
    for i in range(0,5):
        reg = arr.get_element(resultado,i)
        cuenta += 1
        fila = [cuenta]
        for variable in variables:
            fila.append(reg[variable])
        table.append(fila)
    print(tabulate(table, headers, tablefmt="rounded_grid"))


def load_data(control, filename):
    """
    Carga los datos
    """
    #TODO ARREGLAR ESTO
    total, time = logic.load_data(control, filename)
    print("Total de reportes: ", arr.size(total))
    print("Primeros 5 registros: ")
    print_multiple_data(1, total, 1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0)
    print("\n...\n")
    print("Últimos 5 Registros: ")
    ult_registro = arr.sub_list(total, arr.size(total)-5, 5)
    print_multiple_data(arr.size(total)-4, ult_registro, 1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0)
    print("Tiempo que se demoro en cargar: ", time)
    
    

def print_req_1(control, inicial, final):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    total, time = logic.req_1(control, inicial, final)
    print("Tiempo que se demoro en cargar: ", time)
    print("Crimenes totales: ", arr.size(total))
    if arr.size(total) > 20:
        print("Primeros 5 registros: ")
        print_multiple_data(1, total, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0)
        print("\n...\n")
        print("Últimos 5 Registros: ")
        ult_registro = arr.sub_list(total, arr.size(total)-5, 5)
        print_multiple_data(arr.size(total)-4, ult_registro,  1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0)
    else:
        print_data(20, total, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0)

def print_req_2(control, inicial, final):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    total, time = logic.req_2(control, inicial, final)
    print("Tiempo que se demoro en cargar: ", time)
    print("Crimenes totales: ", arr.size(total))
    if arr.size(total) > 10:
        print("Primeros 5 registros: ")
        print_multiple_data(1, total, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0)
        print("\n...\n")
        print("Últimos 5 Registros: ")
        ult_registro = arr.sub_list(total, arr.size(total)-5, 5)
        print_multiple_data(arr.size(total)-4, ult_registro,  1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0)
    else:
        print_data(10, total, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0)
    


def print_req_3(control, n, area):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    registros, totales, time = logic.req_3(control, n, area)
    print("Tiempo que se demoro en cargar: ", time)
    if registros != None:
        print(f'El número de registros que pasaron el filtro fueron: {totales}')
        print_data(int(n), registros, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0)  
    else:
        print(f"No se encontraron registros con {area}")


def print_req_4(control, num, inicial, final):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    total, time = logic.req_4(control, num, inicial, final)
    print("Tiempo que se demoro en cargar: ", time)
    print("Crimenes totales: ", arr.size(total))
    if num > arr.size(total):
        num = arr.size(total)
    print_data(num, total, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0)
    
    


def print_req_5(control, num_a_consultar, fecha_inicial, fecha_final):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    total, maparea= logic.req_5(control, num_a_consultar, fecha_inicial, fecha_final)
    print(f"Crimenes occuridos para el rango de fechas dado:", total)
    table = []
    headers = ["#", "Area", "Nombre", "# Crimenes", "Primera Fecha", "Ultima Fecha"]
    cuenta = 0
    if num_a_consultar > total:
        num_a_consultar = total
    for i in range(0,num_a_consultar):
        crimen = list(arr.get_element(maparea,i).keys())[0]
        cuenta += 1
        fila = [cuenta]
        fila.append(crimen)
        fila.append(arr.get_element(maparea,i)['nombre'])    
        fila.append(arr.get_element(maparea,i)['size'])
        primera_fecha= arr.get_element(maparea,i)[0]
        fila.append(primera_fecha)    
        ultima_fecha= arr.get_element(maparea,i)[arr.size(arr.get_element(maparea,i))-1]
        fila.append(ultima_fecha)
        table.append(fila)
    print(tabulate(table, headers, tablefmt="rounded_grid"))


def print_req_6(control, num, sexo, mes):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    total, maparea, mapfechas, time = logic.req_6(control, num, sexo, mes)
    print("Tiempo que se demoro en cargar: ", time)
    print(f"Crimenes occuridos para el mes {mes}: ", total)
    if num > total:
        num = total
        
    table = []
    headers = ["#", "Area", "Nombre", "# Crimenes"]
    cuenta = 0
    for i in range(0,num):
        crimen = list(arr.get_element(maparea,i).keys())[0]
        cuenta += 1
        fila = [cuenta]
        fila.append(crimen)
        fila.append(arr.get_element(maparea,i)['nombre'])    
        fila.append(arr.get_element(maparea,i)['size'])    
        table.append(fila)
    print(tabulate(table, headers, tablefmt="rounded_grid"))
    
    print("YEARS")
    table = []
    headers = ["#", "Year", "# Crimenes"]
    cuenta = 0
    anios = lp.key_set(mapfechas)
    lista_anios = lp.value_set(mapfechas)
    for i in range(arr.size(anios)):
        fecha = arr.get_element(anios,i)
        cuenta += 1
        fila = [cuenta]
        fila.append(fecha)
        fila.append(arr.size(arr.get_element(lista_anios,i))) 
        table.append(fila)
    print(tabulate(table, headers, tablefmt="rounded_grid"))


def print_req_7(control, num, sexo, inicial, final):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    total, edad_values, edad_keys, ordenado, fechas, time = logic.req_7(control, num, sexo, inicial, final)
    print("Tiempo que se demoro en cargar: ", time)
    print("Crimenes totales cometidos: ", total)
    print("Diferentes Crimenes cometidos: ", arr.size(ordenado))
    
    if num > arr.size(ordenado):
        num = arr.size(ordenado)

    table = []
    headers = ["#", "Cd. Crimen", "# Crimenes"]
    cuenta = 0
    for i in range(0,num):
        crimen = list(arr.get_element(ordenado,i).keys())[0]
        cuenta += 1
        fila = [cuenta]
        fila.append(crimen)
        fila.append(arr.get_element(ordenado,i)['size'])    
        table.append(fila)
    print(tabulate(table, headers, tablefmt="rounded_grid"))
    
    print("EDADES")
    table = []
    headers = ["#", "Edad", "# Crimenes"]
    cuenta = 0
    for i in range(0,final-inicial+1):
        edad = arr.get_element(edad_keys,i)
        mapa = arr.get_element(edad_values,i)
        grave = lp.get(mapa, "1")
        nograve = lp.get(mapa, "2")
        suma = 0
        if grave:
            suma += arr.size(grave)
        if nograve:
            suma += arr.size(nograve)
        cuenta += 1
        fila = [cuenta]
        fila.append(edad)
        fila.append(suma) 
        table.append(fila)
    print(tabulate(table, headers, tablefmt="rounded_grid"))
    
    print("YEARS")
    table = []
    headers = ["#", "Year", "# Crimenes"]
    cuenta = 0
    anios = lp.key_set(fechas)
    lista_anios = lp.value_set(fechas)
    for i in range(arr.size(anios)):
        fecha = arr.get_element(anios,i)
        cuenta += 1
        fila = [cuenta]
        fila.append(fecha)
        fila.append(arr.size(arr.get_element(lista_anios,i))) 
        table.append(fila)
    print(tabulate(table, headers, tablefmt="rounded_grid"))



def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            load_data(control, "Crime_in_LA_20.csv")
        elif int(inputs) == 2:
            inicial = input('Seleccione una fecha inicial (con formato "%Y-%m-%d"): ')
            final = input('Seleccione una fecha final (con formato "%Y-%m-%d"): ')
            print_req_1(control, inicial, final)

        elif int(inputs) == 3:
            inicial = input('Seleccione una fecha inicial (con formato "%Y-%m-%d"): ')
            final = input('Seleccione una fecha final (con formato "%Y-%m-%d"): ')
            print_req_2(control, inicial, final)

        elif int(inputs) == 4:
            n = input("Ingrese el numero de crimenes a reportar: ")
            area = input("Ingrese el area: ").lower()
            print_req_3(control, n, area)

        elif int(inputs) == 5:
            inicial = int(input('Seleccione una edad inicial: '))
            final = int(input('Seleccione una edad final: '))
            num = int(input("Ingrese el numero de elementos a mostrar: "))
            print_req_4(control, num, inicial, final)

        elif int(inputs) == 6:
            num = int(input("Ingrese el numero de elementos a mostrar: "))
            inicial = input('Seleccione una fecha inicial (con formato "%Y-%m-%d"): ')
            final = input('Seleccione una fecha final (con formato "%Y-%m-%d"): ')
            print_req_5(control, num, inicial, final)

        elif int(inputs) == 7:
            mes = input('Seleccione el mes: ')
            sexo = input('Seleccione el sexo de la victima: ').upper()
            num = int(input("Ingrese el numero de elementos a mostrar: "))
            print_req_6(control, num, sexo, mes)

        elif int(inputs) == 8:
            inicial = int(input('Seleccione una edad inicial: '))
            final = int(input('Seleccione una edad final: '))
            sexo = input('Seleccione el sexo de la victima: ')
            num = int(input("Ingrese el numero de elementos a mostrar: "))
            print_req_7(control, num, sexo.upper(), inicial, final)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

def new_list():
    new_list = {
        "elements": [],
        "size": 0
    }
    return new_list

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def is_empty(my_list):
    
    return my_list["size"] == 0

def size(my_list):
    
    return my_list["size"]

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def first_element(my_list):
    
    if my_list["size"] == 0:
        raise Exception ("IndexError: list index out of range")
    else:
        return my_list["elements"][0]
    
def last_element(my_list):
    
    if is_empty(my_list):
        raise Exception ("IndexError: list index out of range")
    else:
        return my_list["elements"][-1]

def get_element(my_list, pos):
    
    if 0<= pos < size(my_list) and size(my_list) != 0:
        return my_list["elements"][pos]
    else:
        raise Exception ("IndexError: list index out of range")

def delete_element(my_list, pos):
    
    if 0<= pos < size(my_list):
        my_list["elements"].pop(pos)
        my_list["size"] -= 1
    else:
        raise Exception ("IndexError: list index out of range")
    return my_list

def remove_first(my_list):
    
    if size(my_list) == 0:
        raise Exception ("IndexError: list index out of range")
    else:
        my_list["size"] -= 1 
        return my_list["elements"].pop(0)

def remove_last(my_list):
    
    if size(my_list) == 0:
        raise Exception ("IndexError: list out of range")
    else:
        my_list["size"] -= 1 
        return my_list["elements"].pop(-1)

    
def insert_element(my_list, element, pos):
    
    if 0 <= pos <= size(my_list):
        my_list["elements"].insert(pos, element)
        my_list["size"] += 1    
        return my_list
    else:
        raise Exception ("IndexError: list out of range")

def cmp_function(element_1, element_2):

   if element_1 > element_2:
      return 1
   elif element_1 < element_2:
      return -1
   return 0

def change_info (my_list, pos, new_info):
    
    if 0 <= pos < size(my_list):
        my_list["elements"][pos] = new_info
        
    else:
        raise Exception ("IndexError: list index out of range")
    return my_list

def exchange(my_list, pos_1, pos_2):
    
    if 0 <= pos_1 < size(my_list) and 0 <= pos_2 < size(my_list):
        info_1 = my_list["elements"][pos_1]
        info_2 = my_list["elements"][pos_2]
        
        my_list["elements"][pos_1] = info_2
        my_list["elements"][pos_2] = info_1
    else:
        raise Exception ("IndexError: list index out of range")
    return my_list

def sub_list(my_list,pos_i, num_elements):
    
    copia = new_list()
    
    if 0 <= pos_i < size(my_list):
        copia["size"] = num_elements
        for i in range (pos_i, num_elements + pos_i):
            copia["elements"].append(my_list["elements"][i])
        return copia
    else:
        raise Exception ("IndexError: list index out of range") 
    
def default_sort_criteria(element_1, element_2):
    '''Función de comparación por defecto para ordenar elementos.

    Compara dos elementos y retorna True si el primer elemento es 
    menor que el segundo y False en caso contrario.

    :param any element_1: Primer elemento a comparar.
    :param any element_2: Segundo elemento a comparar.
    :return bool: True si el primer elemento es menor que el segundo, False en caso contrario.
    '''
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    return is_sorted

def default_sort_criteria_dict(element_1, element_2, parameter):
    '''Función de comparación por defecto para ordenar elementos.

    Compara dos elementos y retorna True si el primer elemento es 
    menor que el segundo y False en caso contrario.

    :param any element_1: Primer elemento a comparar.
    :param any element_2: Segundo elemento a comparar.
    :return bool: True si el primer elemento es menor que el segundo, False en caso contrario.
    '''
    is_sorted = False
    if element_1[parameter] < element_2[parameter]:
        is_sorted = True
    return is_sorted

def selection_sort (my_list, default_sort_criteria):
    """
    Ordena una lista en orden ascendente utilizando el algoritmo Selection Sort.
    
    :param arr: Lista de elementos a ordenar.
    :type arr: list
    
    :return: Lista ordenada en orden ascendente.
    :rtype: list
    """
    tamanio = size(my_list)
    for i in range(tamanio -1):
        indice_min = i
        for j in range(i+1, tamanio):
            elemento_min = get_element(my_list, indice_min)
            elemento_j = get_element(my_list, j)
            if default_sort_criteria(elemento_j, elemento_min):
                indice_min = j
            if indice_min != i:
                exchange(my_list, indice_min, i)
    return my_list

def insertion_sort(my_list, default_sort_criteria):
    """
    Ordena una lista en orden ascendente utilizando el algoritmo Insertion Sort.
    
    :param arr: Lista de elementos a ordenar.
    :type arr: list
    
    :return: Lista ordenada en orden ascendente.
    :rtype: list
    """
    tamanio = size(my_list)
    for i in range(1, tamanio):
        llave = get_element(my_list,i)
        j = i - 1
        while j >= 0 and default_sort_criteria(llave, get_element(my_list, j)):
            change_info(my_list, j+1, get_element(my_list, j))
            j -= 1
        change_info(my_list, j+1, llave)
    return my_list

def shell_sort(my_list, default_sort_criteria):
    """
    Ordena una lista en orden ascendente utilizando el algoritmo Shell Sort 
    con la secuencia de Knuth.
    
    :param arr: Lista de elementos a ordenar.
    :type arr: list
    
    :return: Lista ordenada en orden ascendente.
    :rtype: list
    """
    tamanio = size(my_list)
    h = 1
    while h < tamanio // 3:
        h = 3 * h + 1
    
    while h > 0:
        for i in range(h, tamanio):
            llave = get_element(my_list, i)
            j = i
            while j >= h and default_sort_criteria(llave,get_element(my_list, j-h)):
                change_info(my_list, j, get_element(my_list, j-h))
                j -= h
            change_info(my_list, j, llave)
        h //= 3
    return my_list

def quick_sort(my_list, default_sort_criteria, low = 0, high = None):
    """
    Ordena una lista en orden ascendente utilizando el algoritmo 
    Quick Sort in-place.
    
    :param arr: Lista de elementos a ordenar.
    :type arr: list
    :param low: Índice inferior de la partición actual.
    :type low: int
    :param high: Índice superior de la partición actual.
    :type high: int
    """
    if high is None:
        high = size(my_list) - 1
        
    def partition(my_list, low, high):
        pivot = get_element(my_list, high)
        i = low
        for j in range(low, high):
            if default_sort_criteria(get_element(my_list, j), pivot):
                exchange(my_list, j, i)
                i += 1
        exchange(my_list, i, high)
        return i
    
    if low < high:
        pivot_index = partition(my_list, low, high)
        quick_sort(my_list, default_sort_criteria, low, pivot_index - 1)
        quick_sort(my_list, default_sort_criteria, pivot_index +1, high)
    return my_list

def merge(left, right, default_sort_criteria):
    """
    Mezcla dos listas ordenadas en una sola lista ordenada
    """
    sorted_list = new_list()
    i = j = 0
    
    while i < size(left) and j < size(right):
        if default_sort_criteria(get_element(left, i), get_element(right, j)) or get_element(left, i)== get_element(right, j):
            add_last(sorted_list, get_element(left, i))
            i += 1
        else:
            add_last(sorted_list, get_element(right, j))
            j+= 1
    for k in range(i, size(left)):
        add_last(sorted_list, get_element(left, k))
    for l in range(j, size(right)):
        add_last(sorted_list, get_element(right, l))
    return sorted_list

def merge_sort(my_list, default_sort_criteria):
    """
    Ordena una lista en orden ascendente utilizando el algoritmo Merge Sort.

    :param arr: Lista de elementos a ordenar.
    :type arr: list
    
    :return: Lista ordenada en orden ascendente.
    :rtype: list
    """
    tamanio = size(my_list)
    if tamanio <= 1:
        return my_list

    mid = tamanio // 2
    left = merge_sort(sub_list(my_list, 0, mid), default_sort_criteria)
    right = merge_sort(sub_list(my_list, mid, tamanio-mid), default_sort_criteria)
    return merge(left, right, default_sort_criteria)
from DataStructures.List import list_node as ln

def new_list():
    newlist = {
        "first": None,
        "last": None, 
        "size": 0
    }
    return newlist

def get_element(my_list, pos):
    if my_list["first"] is not None and 0<= pos < size(my_list):
        searchpos = 0
        node = my_list["first"]
        while searchpos < pos:
            node = node["next"]
            searchpos += 1
        return node["info"]

def is_present(my_list, element, cmp_fucntion):
    """_summary_

    Args:
        my_list (_type_): _description_
        element (_type_): _description_
        cmp_fucntion (_type_): _description_

    Returns:
        _type_: _description_
    """
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_fucntion(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    
    if not is_in_array:
        count = -1
    return count

def is_empty(my_list):
    
    return my_list["size"] == 0

def size(my_list):
    
    return my_list["size"]

def add_first(my_list, element):
    new_node = ln.new_single_node(element)
    if size(my_list) == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        temp = my_list["first"]["next"]
        my_list["first"] = new_node
        my_list["first"]["next"] = temp
    
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    new_node = ln.new_single_node(element)
    if size(my_list) == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node
    my_list["size"] += 1
    return my_list

def first_element(my_list):
    if is_empty(my_list):
        raise Exception ("IndexError: list index out of range")
    else:
        return my_list["first"]["info"]

def last_element(my_list):
    if is_empty(my_list):
        raise Exception ("IndexError: list index out of range")
    else:
        return my_list["last"]["info"]
    
def delete_element(my_list, pos):
    if 0 <= pos < size(my_list):
        if pos == 0:
            remove_first(my_list)
        elif pos == size(my_list) -1:
            remove_last(my_list)
        else:
            node = my_list["first"]
            for _ in range(1, pos):
                node = node["next"]
            nodos_a_conectar = node["next"]["next"] #nodos restantes
            node["next"] = nodos_a_conectar #conecta nodos restantes con el anterior
            
            # if node["next"] == None: #si el nodo a eliminar es el último
            #     my_list["last"] = node
            
            my_list["size"] -= 1
        return my_list
    else:
        raise Exception ("IndexError: list index out of range")

def remove_first(my_list):
    if size(my_list) == 0:
        raise Exception ("IndexError: list index out of range")
    else:
        if size(my_list) == 1:
            my_list["last"] = None
        removed_info = my_list["first"]["info"]
        temp = my_list["first"]["next"]
        my_list["first"] = temp
        my_list["size"] -= 1
        return removed_info
        
def remove_last(my_list):
    if not is_empty(my_list):
        if size(my_list) == 1:
            removed_info = remove_first(my_list)
            return removed_info
        else:
            node = my_list["first"]
            for _ in range(1, size(my_list)-1):
                node = node["next"]
            removed_info = my_list["last"]["info"]
            my_list["last"] = node
            my_list["last"]["next"] = None
            my_list["size"] -= 1
            return removed_info
    else:
        raise Exception ("IndexError: lits index out of range")

def insert_element(my_list, element, pos):
    if 0 <= pos <= size(my_list):
        if pos == 0:
            add_first(my_list, element)
        elif my_list["size"] == 0 or pos == size(my_list):
            add_last(my_list, element)
        else:
            node = my_list["first"]
            for _ in range (1, pos):
                node = node["next"]
            temp = node["next"]
            nuevo_nodo = ln.new_single_node(element)
            nuevo_nodo["next"] = temp
            node["next"] = nuevo_nodo
        my_list["size"] += 1
        return my_list
    else:
        raise Exception ("IndexError: list index out of range")
    
def cmp_fucntion(elemen_1, element_2):

   if elemen_1 > element_2:
      return 1
   elif elemen_1 < element_2:
      return -1
   return 0

def change_info(my_list, pos, new_info):
    if 0 <= pos < size(my_list):
        if pos == 0:
            my_list["first"]["info"] = new_info
            return my_list
        elif pos == size(my_list) -1:
            my_list["last"]["info"] = new_info
            return my_list
        else:
            node = my_list["first"]
            for _ in range(1, pos):
                node = node["next"]
            node["info"] = new_info
            return my_list
    else:
        raise Exception ("IndexError: list index out of range")
    
def exchange(my_list, pos_1, pos_2):
    if 0 <= pos_1 < size(my_list) and 0 <= pos_2 < size(my_list):
        node1 = my_list["first"]
        for _ in range(pos_1):
            node1 = node1["next"]
        
        node2 = my_list["first"]
        for _ in range (pos_2):
            node2 = node2["next"]
        
        info1 = node1["info"]
        info2 = node2["info"]
        
        node2["info"] = info1
        node1["info"] = info2
        
        return my_list
    else:
        raise Exception ("IndexError: list index out of range")

def sub_list(my_list, pos, num_elements):
    if 0 <= pos < size(my_list):
        
        sublista = new_list()
        
        node = my_list["first"]
        for _ in range(pos):
            node = node["next"]
        
        for _ in range(num_elements):
            add_last(sublista, node["info"])
            node = node["next"]
        return sublista
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
        if default_sort_criteria(get_element(left, i), get_element(right, j)) or get_element(left, i) == get_element(right, j):
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
    right = merge_sort(sub_list(my_list, mid, tamanio - mid), default_sort_criteria)
    return merge(left, right, default_sort_criteria)
from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
from DataStructures.List import array_list as arr
import random

def new_map(num_elements, load_factor, prime=109345121):
    capacidad = num_elements/load_factor
    capacidad = mf.next_prime(capacidad)
    
    table = arr.new_list()
    for i in range (capacidad):
        arr.add_last(table, me.new_map_entry(None, None))
    
    mapa = {
        "prime": prime,
        "capacity": capacidad,
        "scale": random.randint(1, prime - 1), 
        "shift": random.randint(0, prime - 1), 
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
    }
    return mapa

def put(my_map, key, value):
    hash_value = mf.hash_value(my_map, key)
    table = my_map["table"]
    ocupado, posicion = find_slot(my_map, key, hash_value)
    if ocupado: #si la llave ya existe dentro del mapa
        my_entry = arr.get_element(table, posicion)
        me.set_value(my_entry, value)
    else: #si la llave no existe
        my_entry = arr.get_element(table, posicion)
        me.set_key(my_entry, key)
        me.set_value(my_entry, value)
        my_map["size"] += 1
        my_map["current_factor"] = size(my_map) / arr.size(table)
        
    if my_map["current_factor"] > my_map["limit_factor"]:
        my_map = rehash(my_map)    
    return my_map

def contains(my_map, key):
    encontrado = False
    table = my_map["table"]
    hash_value = mf.hash_value(my_map, key)
    
    if my_map["size"] != 0:
        if key == me.get_key(arr.get_element(table, hash_value)):
            encontrado = True #si encuentra en pos de hash
        else:
            i = hash_value + 1
            vuelta = False
            while not encontrado and i <= arr.size(table) and not vuelta: #itera hasta final
                if i == arr.size(table):
                    i = 0
                    vuelta = True
                elif key == me.get_key(arr.get_element(table, i)):
                    encontrado = True
                i += 1
            
            while not encontrado and vuelta and i < hash_value: #itera inicio hasta hash_value - 1
                if key == me.get_key(arr.get_element(table, i)):
                    encontrado = True
                i += 1
            #en el peor caso itera ambos pero en promedio no itera todo
    return encontrado

def remove(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    table = my_map["table"]
    
    ocupado, posicion = find_slot(my_map, key, hash_value)
    
    if ocupado:
        my_entry = arr.get_element(table, posicion)
        me.set_key(my_entry, "__EMPTY__")
        me.set_value(my_entry, "__EMPTY__")
        my_map["size"] -= 1
        my_map["current_factor"] = size(my_map) / arr.size(table)
    return my_map

def get(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    table = my_map["table"]
    value = None
    ocupado, posicion = find_slot(my_map, key, hash_value)
    
    if ocupado:
        value = me.get_value(arr.get_element(table, posicion))
    return value

def rehash(my_map):
    new_cap = mf.next_prime(my_map["capacity"] * 2)
    key_list = key_set(my_map)
    value_list = value_set(my_map)
    new_table = arr.new_list()
    for i in range(new_cap):
        arr.add_last(new_table, me.new_map_entry(None, None))
    
    my_map["capacity"] = new_cap
    my_map["table"] = new_table
    my_map["size"] = 0
    my_map["current_factor"] = 0
    
    for i in range(arr.size(key_list)):
        key = arr.get_element(key_list, i)
        value = arr.get_element(value_list, i)
        put(my_map, key, value)
    return my_map

def key_set(my_map):
    key_list = arr.new_list()
    table = my_map["table"]
    if not is_empty(my_map):
        for i in range(arr.size(table)):
            my_entry = arr.get_element(table, i)
            if me.get_key(my_entry) != "__EMPTY__" and me.get_key(my_entry) != None:
                arr.add_last(key_list, me.get_key(my_entry))
    return key_list

def value_set(my_map):
    key_list = arr.new_list()
    table = my_map["table"]
    if not is_empty(my_map):
        for i in range(arr.size(table)):
            my_entry = arr.get_element(table, i)
            if me.get_key(my_entry) != "__EMPTY__" and me.get_key(my_entry) != None:
                arr.add_last(key_list, me.get_value(my_entry))
    return key_list

def default_compare(key, entry):
    if key == me.get_key(entry):
        return 0
    elif key > me.get_key(entry):
        return 1
    return -1

def is_available(table, pos):
    entry = arr.get_element(table, pos)
    if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
        return True
    return False

def find_slot(my_map, key, hash_value):
    occupied = False
    posicion = hash_value
    table = my_map["table"]
    
    if contains(my_map, key): #si la llave existe
        occupied = True
        if default_compare(key, arr.get_element(table, posicion)) != 0: #si no esta en el hash_value producido
            my_entry = arr.get_element(table, posicion)
            while me.get_key(my_entry) != key: #itera hasta encontrar donde esta la llave
                posicion += 1
                if posicion >= arr.size(table):
                    posicion = 0
                my_entry = arr.get_element(table, posicion)
    else: #si la llave no existe
        found = False
        while not found: #itera hasta encontrar una posicion para insertar
            if posicion >= arr.size(table):
                posicion = 0
            if not is_available(table, posicion):
                posicion += 1
            else:
                found = True
    return occupied, posicion

def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    return size(my_map) == 0


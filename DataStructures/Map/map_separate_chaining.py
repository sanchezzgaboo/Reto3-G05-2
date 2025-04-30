from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
from DataStructures.List import single_linked_list as sll
from DataStructures.List import array_list as arr 
import random

def new_map(num_elements, load_factor, prime=109345121):
    capacidad = num_elements/load_factor
    capacidad = mf.next_prime(capacidad)
    
    table = arr.new_list()
    for i in range (capacidad):
        bucket = sll.new_list()
        arr.add_last(table, bucket)
    
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
    bucket = arr.get_element(table, hash_value)
    
    if contains(my_map, key): #si la llave existe 
        node = bucket["first"]
        cambiado = False
        while node != None and not cambiado: #mientras no sea None y no haya cambiado nada
            if me.get_key(node["info"]) == key: 
                me.set_value(node["info"], value) #cambia valor si llaves son iguales
                cambiado = True #detiene loop
            node = node["next"]
    else: 
        my_entry = me.new_map_entry(key, value)
        sll.add_last(bucket, my_entry)
        my_map["size"] += 1
        my_map["current_factor"] = size(my_map) / arr.size(table)
        
    if my_map["current_factor"] > my_map["limit_factor"]:
        my_map = rehash(my_map)    
    return my_map

def contains(my_map, key):
    encontrado = False
    table = my_map["table"]
    hash_value = mf.hash_value(my_map, key)
    bucket = arr.get_element(table, hash_value)
    
    if not sll.is_empty(bucket):
        node = bucket["first"]
        while node != None and not encontrado: #mientras no sea None nodo
            if me.get_key(node["info"]) == key: #compara llaves
                encontrado = True
            node = node["next"]
    return encontrado

def remove(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    table = my_map["table"]
    bucket = arr.get_element(table, hash_value)
    
    if contains(my_map, key):
        node = bucket["first"]
        posicion = 0 #posicion dentro de bucket
        eliminado = False
        while node != None and not eliminado:
            if me.get_key(node["info"]) == key:
                sll.delete_element(bucket, posicion)
                my_map["size"] -= 1
                my_map["current_factor"] = size(my_map) / arr.size(table)
                eliminado = True
            posicion += 1 
            node = node["next"]
    return my_map

def get(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    table = my_map["table"]
    value = None
    bucket = arr.get_element(table, hash_value)
    
    if contains(my_map, key):
        node = bucket["first"]
        encontrado = False
        while node != None and not encontrado:
            if me.get_key(node["info"]) == key: #compara llaves
                value = me.get_value(node["info"])
                encontrado = True
            node = node["next"]
    return value

def rehash(my_map):
    new_cap = mf.next_prime(my_map["capacity"] * 2)
    key_list = key_set(my_map)
    value_list = value_set(my_map)
    new_table = arr.new_list()
    for i in range(new_cap):
        bucket = sll.new_list()
        arr.add_last(new_table, bucket)
    
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
        for i in range(arr.size(table)): #recorre cada bucket
            bucket = arr.get_element(table, i)
            node = bucket["first"]
            while node != None: #mientras no este vacío busca
                llave = me.get_key(node["info"])
                if llave != None and llave != "__EMPTY__": #si no hay nada
                    arr.add_last(key_list, llave)
                node = node["next"]
    return key_list

def value_set(my_map):
    value_list = arr.new_list()
    table = my_map["table"]
    
    if not is_empty(my_map):
        for i in range(arr.size(table)): #recorre cada bucket
            bucket = arr.get_element(table, i)
            node = bucket["first"]
            while node != None: #mientras no este vacío busca
                llave = me.get_key(node["info"])
                if llave != None and llave != "__EMPTY__": #si no hay nada
                    value = me.get_value(node["info"])
                    arr.add_last(value_list, value)
                node = node["next"]
    return value_list

def default_compare(key, element):

   if (key == me.get_key(element)):
      return 0
   elif (key > me.get_key(element)):
      return 1
   return -1

def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    return size(my_map) == 0



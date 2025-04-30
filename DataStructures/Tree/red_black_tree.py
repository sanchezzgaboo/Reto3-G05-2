import random
import math
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sll
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.Tree import rbt_node as rbt_node

def new_map():
    rbt ={"root": None}
    return rbt

def put(my_rbt, key, value):
    if not my_rbt["root"]:
        my_rbt["root"] = rbt_node.new_node(key, value)
        return my_rbt    
    else:
        my_rbt["root"] = insert_node(my_rbt["root"], key, value)
        return my_rbt

def insert_node(root, key, value):
    if root is None:
        return rbt_node.new_node(key, value)
    if root["key"]==key:
        root["value"] = value
    elif root["key"]>key:
        if not root["left"]:
            root["left"] = rbt_node.new_node(key,value)
        else:
            root["left"] = insert_node (root["left"], key, value)
    elif root["key"]<key:
        if not root["right"]:
            root["right"] = rbt_node.new_node(key,value)
        else:
            root["right"] = insert_node (root["right"], key, value)
    
    if root["left"]:
        left_size = root["left"]["size"]
    else:
        left_size = 0
    if root["right"]:
        right_size = root["right"]["size"]
    else:
        right_size = 0
    
    root["size"] = 1 + left_size + right_size
    
    root = balance(root)
    
    return root
    
def get(my_rbt, key):
    root = get_node(my_rbt["root"], key)
    if root is not None:
        return rbt_node.get_value(root)
    return None

def get_node(root, key):
    if not root:
        return None
    elif root["key"] == key:
        return root
    elif key < root["key"]:
        return get_node(root["left"], key)
    else:
        return get_node(root["right"], key)

#Solo implementar si es necesario o quieren...
def remove(my_rbt, key):
    if contains(my_rbt, key):
        my_rbt["root"] = remove_node(my_rbt["root"],key)
    return my_rbt

#Solo implementar si es necesario o quieren...
def remove_node(root, key):
    if not root:
        return None
    if key < root["key"]:
        root["left"] = remove_node(root["left"], key)
    elif key > root["key"]:
        root["right"] = remove_node(root["right"], key)
    else:
        if not root["left"]:
            return root["right"]
        if not root["right"]:
            return root["left"]
        temp = get_max_node(root["left"])
        root["left"] = delete_max_node(root["left"])
        root["key"] = temp["key"]
        root["value"] = temp["value"]
    
    if root["left"]:
        left_size = root["left"]["size"]
    else:
        left_size = 0
    if root["right"]:
        right_size = root["right"]["size"]
    else:
        right_size = 0
    root["size"] = 1 + left_size + right_size

    return root

def contains(my_rbt, key):
    return bool(get(my_rbt, key))

def size(my_rbt):
    return size_tree(my_rbt["root"])

def is_empty(my_rbt):
    return not my_rbt or my_rbt["root"] is None

def key_set(my_rbt):
    key_list = sll.new_list()
    return key_set_tree(my_rbt["root"], key_list)

def key_set_tree(root, key_list):
    if root is not None:
        key_set_tree(root["left"], key_list)
        sll.add_last(key_list, root["key"])
        key_set_tree(root["right"], key_list)
    return key_list    
    
def value_set(my_rbt):
    value_list = sll.new_list()
    return value_set_tree(my_rbt["root"], value_list)

def value_set_tree(root, value_list): 
    if root is not None:
        value_set_tree(root["left"], value_list)
        sll.add_last(value_list, root["value"])
        value_set_tree(root["right"], value_list)
    return value_list

def get_min(my_rbt):
    if is_empty(my_rbt):
        return None
    return rbt_node.get_key(get_min_node(my_rbt["root"]))
    

def get_min_node(root):
    if root["left"] is not None:
        return get_min_node(root["left"])
    return root

def get_max(my_rbt):
    if is_empty(my_rbt):
        return None
    return rbt_node.get_key(get_max_node(my_rbt["root"]))

def get_max_node(root):
    if root["right"] is not None:
        return get_max_node(root["right"])
    return root

#Solo implementar si es necesario o quieren...
def delete_min(my_rbt):
    if not my_rbt["root"]:
        return my_rbt["root"] 
    else:
        my_rbt["root"] = delete_min_node(my_rbt["root"])
        if my_rbt["root"]:
            my_rbt["root"]["color"] = 1
        return my_rbt
    
#Solo implementar si es necesario o quieren...
def delete_min_node(root):
    if not root["left"]:
        return root["right"]
    
    if root["left"]["left"] and not rbt_node.is_red(root["left"]["left"]) and not rbt_node.is_red(root["left"]):
        root = move_red_left(root)
        
    if root["left"] is not None:
        root["left"] = delete_min_node(root["left"])
    
    return balance(root)
    
#Solo implementar si es necesario o quieren...
def delete_max(my_rbt):
    if my_rbt["root"]:
        my_rbt["root"] = delete_max_node(my_rbt["root"])
        if my_rbt["root"]:
            my_rbt["root"]["color"] = 1
    
    return my_rbt
    
    
#Solo implementar si es necesario o quieren...
def delete_max_node(root):
    if root is None:
        return None
    
    if root["right"] is None:
        return root["left"]
    
    if (root["right"] and not rbt_node.is_red(root["right"])) and \
   (root["right"] and root["right"]["right"] and not rbt_node.is_red(root["right"]["right"])):
        root = move_red_right(root)
        
    root["right"] = delete_max_node(root["right"])
    
    return balance(root)

def floor(my_bst, key):
    
    root = my_bst["root"]

    while contains(my_bst, key) is False:
        key = key - 1
    
        if key < 0:
            break
    
    if key >= 0:
        return floor_key(root, key)
    else:
        return None         
          
def floor_key(root, key):
    
    if key == root["key"]:
        return root["key"]
    else:
        if key > root["key"]:
            root = root["right"]
            return floor_key(root, key)
            
        elif key < root["key"]:
            root = root["left"]
            return floor_key(root, key)              
        
def ceiling(my_bst, key):
    
    root = my_bst["root"]
    return ceiling_key(root, key)
        

def ceiling_key(root, key):
    if root is None:
        return None

    if key == root["key"]:
        return root["key"]
    
    if key < root["key"]:
        left_ceiling = ceiling_key(root["left"], key)
        return left_ceiling if left_ceiling is not None else root["key"]
    return ceiling_key(root["right"], key)
               
    
def select(my_bst, pos):
    
    root = my_bst["root"]
    
    
    return select_key(root, pos)
    
def select_key(root, pos):
    
    in_order_list = sll.new_list()
    
    def in_order(root, in_order_list):
        if root is not None:
            in_order(root["left"], in_order_list)
            sll.add_last(in_order_list, root["key"])
            in_order(root["right"], in_order_list)
    
    in_order(root, in_order_list)
    
    if pos < 0 or pos >= sll.size(in_order_list):
        return None
    
    return sll.get_element(in_order_list, pos) 


def rank(my_bst, key):
    root = my_bst["root"]
    lista = rank_keys(root, key)
    count = 0
    
    node = lista["first"]
    
    while node is not None:
        if node["info"] < key:
            count += 1
        node = node["next"]
    return count   
    
def rank_keys(root, key):
    
    in_order_list = sll.new_list()
    
    def in_order(root, in_order_list):
        
        if root is not None:
            in_order(root["left"], in_order_list)
            #in_order_list.append(root["key"])
            sll.add_last(in_order_list, root["key"])
            in_order(root["right"], in_order_list)
    
    in_order(root, in_order_list)

    return in_order_list


def height(my_brt):
    
    root = my_brt["root"]
    lista = height_tree(root)
    
    if lista["elements"][0] == -1:
        return 0
    else:
    
        return max(lista["elements"])  


def height_tree(root):
    
    count_list = al.new_list()
    counta = 0
    
    
    def counter(count_list, root, counta):
        if root is None:
            counta -=1
            al.add_last(count_list, counta)
        else:
            counter(count_list, root["right"], counta +1)
            counter(count_list, root["left"], counta +1)
    
    counter(count_list, root, counta)
    
    return count_list



def keys(my_rbt, key_initial, key_final):
    list_key = sll.new_list()
    return keys_range(my_rbt["root"], key_initial, key_final, list_key)

def keys_range(root, key_initial, key_final, list_key):

    if root is None:
        return list_key
    
    if key_initial <= root["key"]:
        keys_range(root["left"], key_initial, key_final, list_key)
    if key_initial <= root["key"] <= key_final:
        sll.add_last(list_key, root["key"])
    if key_final >= root["key"]:
        keys_range(root["right"], key_initial, key_final, list_key)
        
    return list_key
    
def values(my_rbt, key_initial, key_final):
    
    root = my_rbt["root"]
    value_list = sll.new_list()
    lst = values_range(root, key_initial, key_final, value_list)
    
    nodo = lst["first"]
    
    rst = sll.new_list()
    
    while nodo is not None:
        sll.add_last(rst, nodo["info"])
        nodo = nodo["next"]
        
    return rst
    
def values_range(root, key_initial, key_final, value_list):
    if root is None:
        return value_list
    
    if key_initial <= root["key"]:
        values_range(root["left"], key_initial, key_final, value_list)
    if key_initial <= root["key"] <= key_final:
        sll.add_last(value_list, root["value"])
    if key_final >= root["key"]:
        values_range(root["right"], key_initial, key_final, value_list)
        
    return value_list


def rotate_left(nodo_rbt):
    hijo_der = nodo_rbt["right"]
    nodo_rbt["right"] = hijo_der["left"]
    hijo_der["left"] = nodo_rbt

    hijo_der["color"] = nodo_rbt["color"]
    nodo_rbt["color"] = 0

    nodo_rbt["size"] = 1 + size_tree(nodo_rbt["left"]) + size_tree(nodo_rbt["right"])
    hijo_der["size"] = 1 + size_tree(hijo_der["left"]) + size_tree(hijo_der["right"])

    return hijo_der


def rotate_right(nodo_rbt):
    hijo_izq = nodo_rbt["left"]
    nodo_rbt["left"] = hijo_izq["right"]
    hijo_izq["right"] = nodo_rbt

    hijo_izq["color"] = nodo_rbt["color"]
    nodo_rbt["color"] = 0

    nodo_rbt["size"] = 1 + size_tree(nodo_rbt["left"]) + size_tree(nodo_rbt["right"])
    hijo_izq["size"] = 1 + size_tree(hijo_izq["left"]) + size_tree(hijo_izq["right"])

    return hijo_izq
    

    
def flip_colours(node_rbt):
    node_rbt["color"] = 0
    if node_rbt["left"]:
        node_rbt["left"]["color"] = 1
    if node_rbt["right"]:
        node_rbt["right"]["color"] = 1    
    
    
def size_tree(root):
    if root:
        return 1 + size_tree(root["left"]) + size_tree(root["right"])
    return 0

#Solo implementar si es necesario o quieren...
def move_red_right(root):
    
    flip_colours(root)
    if root["left"] and root["left"]["left"] and \
    rbt_node.is_red(root["left"]) and rbt_node.is_red(root["left"]["left"]):
        root = rotate_right(root)
        flip_colours(root)
    return root

#Solo implementar si es necesario o quieren...
def move_red_left(root):
    
    flip_colours(root)
    if (root["right"] is not None and root["right"]["left"] is not None and rbt_node.is_red(root["right"]["left"])): 
        root["right"] = rotate_right(root["right"])
        root = rotate_left(root)
        flip_colours(root)
    return root

   
def balance(root):
    if root["right"] and rbt_node.is_red(root["right"]) and (root["left"] is None or not rbt_node.is_red(root["left"])):
        root = rotate_left(root)
    if root["left"] and rbt_node.is_red(root["left"]) and root["left"]["left"] and rbt_node.is_red(root["left"]["left"]):
        root = rotate_right(root)
    if root["left"] and root["right"] and rbt_node.is_red(root["left"]) and rbt_node.is_red(root["right"]):
        flip_colours(root)
    return root

def default_compare(key, element):
    
    if key == rbt_node.get_key(element):
        return 0
    elif key > rbt_node.get_key(element):
        return 1
    return -1

    
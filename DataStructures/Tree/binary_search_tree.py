import doctest
import sys
from DataStructures.List import single_linked_list as sll
from DataStructures.List import array_list as arr

from DataStructures.Tree import tree_traversal as traverse
sys.setrecursionlimit(10000)
from DataStructures.Tree import bst_node as node

def new_map():
    
    return {
        "root": None,
        "type": "BST"    
            }

def size_tree(root):
    return 0 if root is None else root["size"]    
def size(my_bst):
    return size_tree(my_bst["root"])

def insert_node(root, key, value):
    '''_summary_

    :param _type_ root: _description_
    :param _type_ key: _description_
    :param _type_ value: _description_
    

    '''
    
    if root == None:
        root = node.new_node(key, value)
    elif key == node.get_key(root):
        root['value'] = value
    else:
        key_root = node.get_key(root)
        if key < key_root:
            root["left"] = insert_node(root['left'], key, value)          
        else:
            root["right"] = insert_node(root['right'], key, value)
            
        root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    
    return root

def put(my_bst, key, value):
    '''_summary_

    :param _type_ my_bst: _description_
    :param _type_ key: _description_
    :param _type_ value: _description_
    
    >>> tree = new_map()
    >>> put(tree, 5, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 3, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 6, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 1, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 8, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 7, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': {'key': 7, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 7, 10)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': {'key': 7, 'value': 10, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    
    '''
    my_bst["root"] = insert_node(my_bst["root"], key, value)

    return my_bst

#doctest.run_docstring_examples(put, globs=globals(), verbose=True)
        

def get_node(root, key):
    if root is not None:
        if key < node.get_key(root):
            root = get_node(root['left'], key)
        elif key > node.get_key(root):
            root = get_node(root['right'], key)
        else:
            root = root
    return root    
def get(my_bst, key):
    '''_summary_

    :param _type_ my_bst: _description_
    :param _type_ key: _description_
    :return _type_: _description_
    
    >>> tree = new_map()
    >>> put(tree, 5, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 3, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 6, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 1, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 8, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 7, 10)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': {'key': 7, 'value': 10, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    
    >>> get(tree, 7)
    10
    >>> get(tree, 1)
    1
    >>> get(tree, 11)
    
    '''
    return get_node(my_bst['root'], key)['value'] if get_node(my_bst['root'], key) is not None else None
#doctest.run_docstring_examples(get, globs=globals(), verbose=True)

def contains(my_bst, key):
    '''_summary_

    :param _type_ my_bst: _description_
    :param _type_ key: _description_
    :return _type_: _description_
    >>> tree = new_map()
    >>> put(tree, 5, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 3, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 6, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 1, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 8, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 7, 10)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': {'key': 7, 'value': 10, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    
    >>> contains(tree, 7)
    True
    '''
    if get(my_bst, key) != None:
        return True
    else:
        return False
#doctest.run_docstring_examples(contains, globs=globals(), verbose=True)

def is_empty(my_bst):
    vacio = False
    if my_bst["root"] == None:
        vacio = True
    return vacio

def key_set(my_bst):
    '''_summary_

    :param _type_ my_bst: _description_
    :return _type_: _description_
    '''
    keyset = sll.new_list()
    keys = traverse.inorder(my_bst)
    for i in range(sll.size(keys)):
        sll.add_last(keyset, node.get_key(sll.get_element(keys, i)))
    return keyset
def value_set(my_bst):
    '''_summary_

    :param _type_ my_bst: _description_
    :return _type_: _description_
    '''
    keyset = sll.new_list()
    keys = traverse.inorder(my_bst)
    for i in range(sll.size(keys)):
        sll.add_last(keyset, sll.get_element(keys, i)['value'])
    return keyset
def get_min_node(root):
    if root is None:
        return None
    elif root['left'] is None:
        return root
    return get_min_node(root['left'])

def get_min(my_bst):
    '''_summary_

    :param _type_ my_bst: _description_
    :return _type_: _description_
    >>> tree = new_map()
    >>> put(tree, 5, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 3, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 6, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 1, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 8, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 7, 10)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': {'key': 7, 'value': 10, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    
    >>> get_min(tree)['key']
    1
    '''
    return node.get_key(get_min_node(my_bst['root']))
#doctest.run_docstring_examples(get_min, globs=globals(), verbose=True)

def get_max_node(root):
    if root is None:
        return None
    elif root['right'] is None:
        return root
    return get_min_node(root['right'])
def get_max(my_bst):
    '''_summary_

    :param _type_ my_bst: _description_
    :return _type_: _description_
    >>> tree = new_map()
    >>> put(tree, 5, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 3, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 6, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 1, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 8, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 7, 10)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': {'key': 7, 'value': 10, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    
    >>> get_max(tree)
    
    '''
    return node.get_key(get_max_node(my_bst['root']))
#doctest.run_docstring_examples(get_max, globs=globals(), verbose=True)


def remove_node(root, key):
    if root is not None:
        
        key_root = node.get_key(root)

        if key < key_root:
            root["left"] = remove_node(root["left"], key)
        elif key > key_root:
            root["right"] = remove_node(root["right"], key)
        else:
            # Casos Hoja y Rama
            if root["left"] is None and root["right"] is None:
               return None
            if root["left"] is None:
               return root["right"]
            elif root["right"] is None:
               return root["left"]
            else:
                # Node con 2 hojas
                min_larger_node = get_min_node(root["right"])
                
                # Copy the successor's data to this node
                root["key"] = node.get_key(min_larger_node)
                root["value"] = node.get_value(min_larger_node)
                
                # Delete the successor
                root["right"] = remove_node(root["right"], min_larger_node["key"])
            root["size"] = size_tree(root["left"]) + size_tree(root["right"])
    return root
def remove(my_bst, key):
    '''_summary_

    :param _type_ my_bst: _description_
    :param _type_ key: _description_
    :return _type_: _description_
    
    >>> tree = new_map()
    >>> put(tree, 5, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 3, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 6, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 1, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 8, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 7, 10)
    {'root': {'key': 5, 'value': 1, 'size': 6, 'left': {'key': 3, 'value': 1, 'size': 2, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 3, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 2, 'left': {'key': 7, 'value': 10, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> remove(tree, 7)
    {'root': {'key': 5, 'value': 1, 'size': 5, 'left': {'key': 3, 'value': 1, 'size': 2, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 2, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> remove(tree, 5)
    {'root': {'key': 6, 'value': 1, 'size': 4, 'left': {'key': 3, 'value': 1, 'size': 2, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    
    '''
    my_bst['root']= remove_node(my_bst['root'], key)
    return my_bst
#doctest.run_docstring_examples(remove, globs=globals(), verbose=True)


def delete_min_tree(root):
    if root is not None:
        if root['left'] != None:
            root['left'] = delete_min_tree(root['left'])
        else:
            root = remove_node(root, node.get_key(root))
    return root 
def delete_min(my_bst):
    '''_summary_

    :param _type_ my_bst: _description_
    :return _type_: _description_
    
    >>> tree = new_map()
    >>> put(tree, 5, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 3, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 6, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 1, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 8, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 7, 10)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': {'key': 7, 'value': 10, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    
    >>> delete_min(tree)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': {'key': 7, 'value': 10, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}

    '''
    return delete_min_tree(my_bst['root'])
#doctest.run_docstring_examples(delete_min, globs=globals(), verbose=True)

def delete_max_tree(root):
    if root is not None:
        if root['right'] != None:
            root['right'] = delete_max_tree(root['right'])
        else:
            root = remove_node(root, node.get_key(root))
    return root    
def delete_max(my_bst):
    '''_summary_

    :param _type_ my_bst: _description_
    :return _type_: _description_
    
    >>> tree = new_map()
    >>> put(tree, 5, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 3, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 6, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 1, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 8, 1)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> put(tree, 7, 10)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 1, 'left': {'key': 7, 'value': 10, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    
    >>> delete_max(tree)
    {'root': {'key': 5, 'value': 1, 'size': 1, 'left': {'key': 3, 'value': 1, 'size': 1, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 1, 'left': None, 'right': {'key': 7, 'value': 10, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}

    '''
    return delete_max_tree(my_bst['root'])
#doctest.run_docstring_examples(delete_max, globs=globals(), verbose=True)
def floor_key(root, key):
    if root is None:
        return None

    key_root = node.get_key(root)

    if key == key_root:
        return root

    if key < key_root:
        return floor_key(root['left'], key)

    # key > key_root
    # Floor might be in the right subtree, but if not, root is the floor
    right_candidate = floor_key(root['right'], key)
    return right_candidate if right_candidate is not None else root
def floor(my_bst, key):
    '''_summary_

    :param _type_ my_bst: _description_
    :param _type_ key: _description_
    :return _type_: _description_
    
    
    >>> tree = new_map()
    >>> put(tree, 5, 1)
    >>> put(tree, 3, 1)
    >>> put(tree, 6, 1)
    >>> put(tree, 1, 1)
    >>> put(tree, 8, 1)
    >>> put(tree, 7, 10)
    {'root': {'key': 5, 'value': 1, 'size': 6, 'left': {'key': 3, 'value': 1, 'size': 2, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 3, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 2, 'left': {'key': 7, 'value': 10, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    >>> floor(tree, 5)
    5
    >>> floor(tree, 0)
    
    >>> floor(tree, 2)
    1
    >>> floor(tree, 4)
    3
    >>> floor(tree, 9)
    8
    >>> floor(tree, 11)
    8
    '''
    return node.get_key(floor_key(my_bst['root'], key)) if floor_key(my_bst['root'], key) is not None else None
#doctest.run_docstring_examples(floor, globs=globals(), verbose=True)

def ceiling_key(root, key):
    if root is None:
        return None
    key_root = node.get_key(root)
    if key == key_root:
        return root
    if key > key_root:
        #Buscar en el subarbol derecho si la llave es mayor
        return ceiling_key(root['right'], key)
    # key < key_root
    left_candidate = ceiling_key(root['left'], key)
    return left_candidate if left_candidate is not None else root
def ceiling(my_bst, key):
    '''_summary_

    :param _type_ my_bst: _description_
    :param _type_ key: _description_
    :return _type_: _description_
    
    
    >>> tree = new_map()
    >>> put(tree, 5, 1)
    >>> put(tree, 3, 1)
    >>> put(tree, 6, 1)
    >>> put(tree, 1, 1)
    >>> put(tree, 8, 1)
    >>> put(tree, 7, 10)
    {'root': {'key': 5, 'value': 1, 'size': 6, 'left': {'key': 3, 'value': 1, 'size': 2, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 3, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 2, 'left': {'key': 7, 'value': 10, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    
    >>> ceiling(tree, 5)
    5
    >>> ceiling(tree, 11)
    
    >>> ceiling(tree, 2)
    3
    >>> ceiling(tree, 4)
    5
    '''
    return node.get_key(ceiling_key(my_bst['root'], key)) if ceiling_key(my_bst['root'], key) is not None else None
#doctest.run_docstring_examples(ceiling, globs=globals(), verbose=True)


def select(my_bst, pos):
    #TODO
    pass
def select_key(root, key):
    #TODO
    pass



def rank_keys(root, key):
    root_key = node.get_key(root)
    if root is not None:   
        if key > root_key:
            #TODO QUE HACER SI ES MAYOR
            return root['size']
        else:
            return rank_keys(root['left'], key)
    else:
        return 0

def rank(my_bst, key):
    '''_summary_

    :param _type_ my_bst: _description_
    :param _type_ key: _description_
    :return _type_: _description_
    
    >>> tree = new_map()
    >>> put(tree, 5, 1)
    >>> put(tree, 3, 1)
    >>> put(tree, 6, 1)
    >>> put(tree, 1, 1)
    >>> put(tree, 8, 1)
    >>> put(tree, 7, 10)
    {'root': {'key': 5, 'value': 1, 'size': 6, 'left': {'key': 3, 'value': 1, 'size': 2, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 3, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 2, 'left': {'key': 7, 'value': 10, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    
    >>> rank(tree, 5)
    2
    >>> rank(tree, 2)
    1
    >>> rank(tree, 1)
    0
    
    >>> rank(tree, 8)
    5
    >>> rank(tree, 7)
    4
    '''
    return rank_keys(my_bst['root'], key)
#doctest.run_docstring_examples(rank, globs=globals(), verbose=True)

def find_max(tipe1, tipe2):
    if tipe1 >= tipe2:
        return tipe1
    else:
        return tipe2

def height_tree(root):
    if root is None:
        return 0
    left_height = height_tree(root['left'])
    right_height = height_tree(root['right'])
    
    return 1+find_max(left_height, right_height)
            
            
        
def height(my_bst):
    '''_summary_

    :param _type_ my_bst: _description_
    :return _type_: _description_
    
    >>> tree = new_map()
    >>> put(tree, 5, 1)
    >>> put(tree, 3, 1)
    >>> put(tree, 6, 1)
    >>> put(tree, 1, 1)
    >>> put(tree, 8, 1)
    >>> put(tree, 7, 10)
    {'root': {'key': 5, 'value': 1, 'size': 6, 'left': {'key': 3, 'value': 1, 'size': 2, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 3, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 2, 'left': {'key': 7, 'value': 10, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    
    >>> height(tree)
    3
    >>> remove(tree, 7)
    >>> height(tree)
    2
    '''
    return height_tree(my_bst['root'])
#doctest.run_docstring_examples(height, globs=globals(), verbose=True)


def keys_range(root, key_initial, key_final, list_key):
    if root is not None:
        if key_initial <= node.get_key(root) <= key_final: 
            keys_range(root["left"], key_initial, key_final, list_key)  # 1. Visit left subtree
            arr.add_last(list_key, node.get_key(root))
            keys_range(root["right"], key_initial, key_final,list_key)  # 3. Visit right subtree
        else:
            if key_initial < node.get_key(root):
                keys_range(root["left"], key_initial, key_final, list_key)
            if node.get_key(root) < key_final:
                keys_range(root["right"], key_initial, key_final,list_key)  # 3. Visit right subtree
                
    return list_key 

def keys(my_bst, key_initial, key_final):
    '''_summary_

    :param _type_ my_bst: _description_
    :param _type_ key_initial: _description_
    :param _type_ key_final: _description_
    :return _type_: _description_
    >>> tree = new_map()
    >>> put(tree, 5, 1)
    >>> put(tree, 3, 1)
    >>> put(tree, 6, 1)
    >>> put(tree, 1, 1)
    >>> put(tree, 8, 1)
    >>> put(tree, 7, 10)
    {'root': {'key': 5, 'value': 1, 'size': 6, 'left': {'key': 3, 'value': 1, 'size': 2, 'left': {'key': 1, 'value': 1, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'right': {'key': 6, 'value': 1, 'size': 3, 'left': None, 'right': {'key': 8, 'value': 1, 'size': 2, 'left': {'key': 7, 'value': 10, 'size': 1, 'left': None, 'right': None, 'type': 'BST'}, 'right': None, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}, 'type': 'BST'}
    
    >>> result = keys(tree, 1, 5)
    
    >>> for i in range(sll.size(result)):
    ...     print(sll.get_element(result, i))
    1
    3
    5
    
    >>> result = keys(tree, 1, 9)
    
    >>> for i in range(sll.size(result)):
    ...     print(sll.get_element(result, i))
    1
    3
    5
    6
    7
    8
    
    >>> result = keys(tree, 1, 3)
    
    >>> for i in range(sll.size(result)):
    ...     print(sll.get_element(result, i))
    1
    3
    
    >>> result = keys(tree, 1, 1)
    
    >>> for i in range(sll.size(result)):
    ...     print(sll.get_element(result, i))
    1
    
    >>> result = keys(tree, -1, 0)
    
    >>> for i in range(sll.size(result)):
    ...     print(sll.get_element(result, i))
    
    '''
    return_list = arr.new_list()
    return keys_range(my_bst['root'], key_initial, key_final, return_list)
#doctest.run_docstring_examples(keys, globs=globals(), verbose=True)

def values_range(root, key_lo, key_hi, list_values):
    if root is not None:
        if key_lo <= node.get_key(root) <= key_hi: 
            values_range(root["left"], key_lo, key_hi, list_values)  # 1. Visit left subtree
            arr.add_last(list_values, node.get_value(root))
            values_range(root["right"], key_lo, key_hi,list_values)  # 3. Visit right subtree
        else:
            if key_lo < node.get_key(root):
                values_range(root["left"], key_lo, key_hi, list_values)
            if node.get_key(root) < key_hi:
                values_range(root["right"], key_lo, key_hi,list_values)  # 3. Visit right subtree
                
    return list_values

def values(my_bst, key_initial, key_final):
    #TODO HAY BUG EN VALUES
    result_list = arr.new_list()
    return values_range(my_bst['root'], key_initial, key_final, result_list)
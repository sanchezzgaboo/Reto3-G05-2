import doctest
from DataStructures.List import single_linked_list as sll
def inorder_tree(root, node_list):
    if root is not None:
        inorder_tree(root["left"], node_list)  # 1. Visit left subtree
        sll.add_last(node_list, root)
        inorder_tree(root["right"], node_list)  # 3. Visit right subtree
    return node_list 
def inorder(my_order_map):
    '''_summary_

    :param _type_ my_order_map: _description_
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
    
    >>> inorder(tree)
    
    '''
    inorder_result = sll.new_list()
    return inorder_tree(my_order_map['root'], inorder_result)
#doctest.run_docstring_examples(inorder, globs=globals(), verbose=True)

def preorder_tree(root, node_list):
    if root is not None:
        sll.add_last(node_list, root)
        preorder_tree(root["left"], node_list)  # 1. Visit left subtree
        preorder_tree(root["right"], node_list)  # 3. Visit right subtree
    return node_list 
def preorder(my_order_map):
    '''_summary_

    :param _type_ my_order_map: _description_
    :return _type_: _description_
    
    >>> tree = new_map()
    >>> put(tree, 10, 1)
    >>> put(tree, 5, 1)
    >>> put(tree, 15, 1)
    >>> put(tree, 3, 1)
    >>> put(tree, 7, 1)
    >>> put(tree, 14, 10)
    >>> put(tree, 17, 10)
    >>> put(tree, 1, 10)
    >>> put(tree, 4, 10)
    >>> put(tree, 9, 10)
    >>> put(tree, 16, 10)
    >>> put(tree, 20, 10)
     
    >>> result = preorder(tree)
    
    >>> for i in range(sll.size(result)):
    ...     print(sll.get_element(result, i)['key'])
    
    '''
    preorder_result = sll.new_list()
    return preorder_tree(my_order_map['root'], preorder_result)
#doctest.run_docstring_examples(preorder, globs=globals(), verbose=True)

def postorder_tree(root, node_list):
    if root is not None:
        postorder_tree(root["left"], node_list)  # 1. Visit left subtree
        postorder_tree(root["right"], node_list)  # 3. Visit right subtree
        sll.add_last(node_list, root)
    return node_list 
def postorder(my_order_map):
    '''_summary_

    :param _type_ my_order_map: _description_
    :return _type_: _description_
    
    >>> tree = new_map()
    >>> put(tree, 10, 1)
    >>> put(tree, 5, 1)
    >>> put(tree, 15, 1)
    >>> put(tree, 3, 1)
    >>> put(tree, 7, 1)
    >>> put(tree, 14, 10)
    >>> put(tree, 17, 10)
    >>> put(tree, 1, 10)
    >>> put(tree, 4, 10)
    >>> put(tree, 9, 10)
    >>> put(tree, 16, 10)
    >>> put(tree, 20, 10)
     
    >>> result = postorder(tree)
    
    >>> for i in range(sll.size(result)):
    ...     print(sll.get_element(result, i)['key'])
    
    '''
    postorder_result = sll.new_list()
    return postorder_tree(my_order_map['root'], postorder_result)
#doctest.run_docstring_examples(postorder, globs=globals(), verbose=True)


from DataStructures.List import single_linked_list as sll
def new_stack():
    return sll.new_list()

def push(my_stack, element):
    return sll.add_last(my_stack, element)

def pop(my_stack):
    if size(my_stack) == 0:
        raise Exception ("EmptyStructureError: stack is empty")
    else:
        return sll.remove_last(my_stack)

def is_empty(my_stack):
    return sll.is_empty(my_stack)

def top(my_stack):
    if size(my_stack) == 0:
        raise Exception ("EmptyStructureError: stack is empty")
    return sll.last_element(my_stack)

def size(my_stack):
    return sll.size(my_stack)

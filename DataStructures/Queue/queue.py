from DataStructures.List import array_list as arr
def new_queue ():
    return arr.new_list()

def enqueue(my_queue, element):
    return arr.add_last(my_queue, element)

def dequeue(my_queue):
    if size(my_queue) == 0:
        raise Exception ("EmptyStructureError: queue is empty")
    else:
        return arr.remove_first(my_queue)

def peek(my_queue):
    if size(my_queue) == 0:
        raise Exception ("EmptyStructureError: queue is empty")
    else:
        return arr.first_element(my_queue)

def is_empty(my_queue):
    return arr.is_empty(my_queue)

def size(my_queue):
    return arr.size(my_queue)
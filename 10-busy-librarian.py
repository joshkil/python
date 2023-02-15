#
# There exists a busy librarian with a bad knee. When patrons arrive 
# at his counter, they request a magazine. They immediately read it 
# and return it before he helps the next patron. Behind his counter 
# there is a shelf where he can store N magazines for quick access, 
# but if the magaine requested by the patron is not on the shelf behind 
# him, he needs to step away from the desk and walk down long corridors 
# searching the stacks for the magazine requested. He needs to make 
# the best use of his temporary storage shelf possible.
#
# Your job is to write a function that computes the number of 
# trips your librarian needs to make to the stacks while processing
# an iterator of requests. Your function receives an iterator that  
# returns integers representing unique magazine id's, and N, the max
# number of magazines the librarian can keep on the shelf
# behind his counter. Your function can't look ahead and know future 
# requests. Based on the incoming requests, make use of the temporary 
# storage shelf behind the counter to reduce trips to the stacks. 
#
# Example: 
# N = 3
# Requests = [1, 2, 3, 1, 4, 2, 5]
# Answer: One answer is 6 
# Trip #    Self Contents
# 1         [1]
# 2         [1,2]
# 3         [1,2,3]
# 4         [3,1,4]
# 5         [1,4,2]
# 6         [4,2,5]

# TODO: Consider adding an implementation with objects and pointers that won't 
#       require ordered dict to get optimal performance. 

import collections

# self_size   : the number of magazines the librarian can keep 
#               on their shelf
# request_itr : a Python iterator object that can iterate over
#               the requests
def compute_trips(shelf_size, request_itr):
    shelf = collections.deque()
    shelf_index = set()
    num_stack_trips = 0

    for r in request_itr:
        if r in shelf_index: # O(1)
            # we can serve this request from the shelf
            # adjust the location of this item on the shelf to 
            # reflect it was recently used.
            shelf.remove(r)  # O(n) operation to find item
            shelf.append(r)  # O(1)
        else:
            # we need to visit the stacks
            num_stack_trips += 1
            if len(shelf) == shelf_size: 
                # we need to remove something from the shelf 
                # remove least recently used item
                removed = shelf.popleft()   #O(1) for deque
                shelf_index.remove(removed) #O(1) for set
            shelf.append(r)    #O(1)
            shelf_index.add(r) #O(1)

    return num_stack_trips

# This second version uses OrderedDict to be more efficient
# self_size   : the number of magazines the librarian can keep 
#               on their shelf
# request_itr : a Python iterator object that can iterate over
#               the requests
def compute_trips_2(shelf_size, request_itr):
    shelf = collections.OrderedDict()
    num_stack_trips = 0

    for r in request_itr:
        if r in shelf: # O(1)
            # we can serve this request from the shelf
            # adjust the location of this item on the shelf to 
            # reflect it was recently used.
            shelf.move_to_end(r, last=True)  # O(1) operation to move to front of list
        else:
            # we need to visit the stacks
            num_stack_trips += 1
            if len(shelf) == shelf_size: 
                # we need to remove something from the shelf 
                # remove least recently used item
                shelf.popitem(last=False)  #O(1) for deque
            shelf[r] = 0    #O(1)

    return num_stack_trips

requests = [1, 2, 3, 1, 4, 2, 5]
print(compute_trips(4, iter(requests)))
print(compute_trips_2(4, iter(requests)))
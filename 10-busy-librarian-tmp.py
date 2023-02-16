#
# There exists a busy librarian with a bad knee. When customers arrive 
# at his counter, they request a magazine. They immediately read it 
# and return it before he helps the next customer. Behind his counter 
# there is a shelf where he can store N magazines for quick access, 
# but if the magaine requested by the customer is not on the shelf behind 
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
# Req #     Trip #    Self Contents
# 1          1         [1]
# 2          2         [1,2]
# 3          3         [1,2,3]
# 4          -          ^
# 5          4         [3,1,4]
# 6          5         [1,4,2]
# 7          6         [4,2,5]


# self_size   : the number of magazines the librarian can keep 
#               on their shelf
# request_itr : a Python iterator object that can iterate over
#               the requests
def compute_trips(shelf_size, request_itr):
    return 0

requests = [1, 2, 3, 1, 4, 2, 5]
print(compute_trips(3, iter(requests)))
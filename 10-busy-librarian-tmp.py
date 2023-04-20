#
# There exists a busy librarian. When customers arrive 
# at his counter, they request a magazine. They immediately read it 
# and return it before he helps the next customer. Behind his counter 
# there is a shelf where he can store N magazines for quick access, 
# but if the magazine requested by the customer is not on the shelf behind 
# him, he needs to step away from the desk and walk down long corridors 
# searching the stacks for the magazine requested. He needs to make 
# the best use of his temporary storage shelf possible.
#
# Your job is to write an algorithm to manage the shelf behind the counter.
# Then write a function that computes the number of trips the librarian needs 
# to make to the stacks using your algorithm while processing an iterator of 
# requests. Your function receives an iterator that  
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


# The example below has 500 requests for 7 unique magazines. The request
# stream has the following distribution 
#
#    numbers:         0   1   2   3   4   5   6
#    distribution = [10, 20,  5, 20, 15,  5, 25]
# 
# 10% of the requests are for 0, 20% of requests are for 1
# I get 78 cache misses. 
requests = [0, 1, 4, 1, 4, 2, 6, 1, 1, 2, 2, 3, 4, 6, 3, 1, 6, 2, 4, 4, 1, 6, 4, 3, 5, 4, 3, 4, 5, 3, 4, 6, 4, 4, 6, 3, 6, 3, 3, 1, 6, 1, 4, 3, 0, 3, 3, 4, 4, 0, 6, 6, 3, 1, 1, 0, 6, 3, 6, 1, 6, 0, 6, 3, 6, 6, 3, 6, 4, 4, 4, 1, 0, 0, 1, 4, 1, 3, 1, 3, 6, 6, 1, 5, 3, 0, 4, 0, 2, 4, 6, 6, 6, 4, 6, 6, 6, 1, 6, 3, 1, 3, 3, 2, 0, 4, 0, 1, 1, 6, 1, 0, 3, 3, 3, 2, 3, 6, 4, 1, 4, 0, 4, 6, 1, 6, 6, 4, 0, 4, 6, 3, 6, 1, 6, 4, 6, 3, 6, 4, 6, 6, 4, 4, 3, 0, 6, 6, 1, 3, 6, 6, 4, 0, 0, 6, 3, 4, 6, 6, 3, 6, 4, 3, 1, 6, 3, 3, 1, 0, 1, 1, 1, 3, 1, 3, 1, 5, 2, 6, 2, 3, 4, 1, 6, 3, 0, 6, 6, 3, 6, 3, 3, 6, 6, 3, 6, 6, 1, 2, 3, 3, 6, 6, 6, 2, 1, 6, 2, 3, 1, 3, 6, 6, 6, 1, 6, 6, 3, 4, 1, 6, 6, 2, 1, 1, 0, 5, 4, 1, 1, 4, 3, 6, 1, 4, 6, 4, 1, 3, 0, 6, 1, 5, 1, 6, 3, 4, 6, 6, 3, 0, 6, 6, 6, 6, 6, 4, 0, 4, 0, 6, 4, 6, 3, 1, 1, 6, 6, 1, 3, 3, 1, 6, 1, 1, 5, 3, 3, 0, 1, 3, 3, 1, 1, 4, 3, 2, 3, 6, 1, 3, 4, 6, 1, 6, 6, 6, 6, 3, 3, 6, 0, 0, 3, 6, 3, 4, 2, 4, 4, 1, 6, 1, 6, 1, 4, 3, 1, 3, 6, 6, 6, 6, 1, 2, 0, 6, 1, 6, 1, 6, 6, 4, 6, 5, 6, 3, 1, 6, 6, 3, 1, 4, 6, 2, 6, 6, 3, 2, 1, 1, 4, 1, 4, 2, 3, 2, 3, 0, 5, 0, 6, 6, 3, 0, 0, 3, 6, 6, 4, 0, 5, 6, 1, 0, 3, 3, 0, 3, 6, 4, 3, 6, 0, 1, 3, 6, 4, 1, 3, 4, 6, 1, 3, 1, 1, 0, 1, 0, 3, 3, 1, 3, 6, 3, 4, 3, 3, 6, 3, 1, 6, 1, 4, 4, 4, 0, 6, 3, 5, 5, 4, 3, 5, 0, 3, 3, 3, 6, 4, 1, 1, 1, 6, 6, 6, 5, 0, 6, 0, 0, 3, 5, 0, 6, 0, 3, 1, 2, 4, 6, 3, 4, 3, 0, 3, 5, 3, 1, 1, 1, 6, 6, 4, 1, 3, 4, 4, 4, 1, 3, 3, 6, 6, 6, 3, 1, 2, 3, 1, 1, 0, 4, 1, 3, 3, 6, 2, 4, 6, 6, 1, 4, 4, 6, 6, 2, 1, 6]
print(compute_trips(5, iter(requests)))
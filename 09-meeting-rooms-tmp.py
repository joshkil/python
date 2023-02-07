#
# Given a list of time intervals return the minimum number of meeting rooms needed 
# for each time interval to get its own meeting room
#  
# ex. 
# [[2,3], [2,4], [4,6], [2,5]] -> 3
#

def rooms_needed(meetings):
        return 0

meetings = [[2,3], [2,4], [4,6], [2,5]]
print("{} exect: 3".format(rooms_needed(meetings)))

# Use to test the code
meetings = [
    [0, 1], [1, 3], [6, 8], [10, 12], [13, 15], [15, 17], [18, 19],
    [0, 1], [1, 2], [3, 5], [6, 7], [8, 10], [12, 14], [14, 15], [15, 17],
    [0, 2], [3, 5], [7, 8], [10, 12], [13, 15], [16, 18],
    [1, 3], [6, 7], [9, 11], [12, 14], [14, 16], [16, 17],
    [1, 2], [4, 6], [7, 9], [11, 12], [14, 16], [17, 19],
    [1, 2], [5, 7], [9, 11], [12, 13], [14, 15], [16, 17],
    [1, 3], [6, 7], [10, 12], [14, 15], [16, 18],
    [1, 2], [5, 7], [10, 11], [12, 14], [14, 16], [18, 19]
]
print("{} exect: 8".format(rooms_needed(meetings)))
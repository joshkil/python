import heapq
import random
import collections

#
# Given a list of time intervals return the minimum number of meeting rooms needed 
# for each time interval to get its own meeting room
#  
# ex. 
# [[2,3], [2,4], [4,6], [2,5]] -> 3
#
# [
#   [0, 1], [1, 3], [6, 8], [10, 12], [13, 15], [15, 17], [18, 19],
#   [0, 1], [1, 2], [3, 5], [6, 7], [8, 10], [12, 14], [14, 15], [15, 17],
#   [0, 2], [3, 5], [7, 8], [10, 12], [13, 15], [16, 18],
#   [1, 3], [6, 7], [9, 11], [12, 14], [14, 16], [16, 17],
#   [1, 2], [4, 6], [7, 9], [11, 12], [14, 16], [17, 19],
#   [1, 2], [5, 7], [9, 11], [12, 13], [14, 15], [16, 17],
#   [1, 3], [6, 7], [10, 12], [14, 15], [16, 18],
#   [1, 2], [5, 7], [10, 11], [12, 14], [14, 16], [18, 19]
# ] ->8
#

def rooms_needed(meetings):
    if len(meetings) == 0:
        return 0
    
    # Sort the array of arrays by the first element of each sub array.
    # The first element of each sub array is the meeting start time.
    meetings.sort(key=lambda i: i[0])

    # Create a list to hold meeting rooms. We will manage this as a 
    # min-heap so the meeting with the earliest ending time is on top. 
    active_meetings = list()
    max_rooms = 0

    # walk through each meeting in starting order
    for m in meetings:
        start = m[0]
        end = m[1]
        if len(active_meetings) != 0 and active_meetings[0] <= start:
            # We already have meeting rooms in use. But the meeting
            # with the earliest finish time ends before this next
            # meeting starts. We can re-use it's room. Pop it off 
            # the heap. 
            heapq.heappop(active_meetings)

        # Push the current meeting's end time onto the heap   
        heapq.heappush(active_meetings, end)
        max_rooms = max(max_rooms, len(active_meetings))
    
    return max_rooms

def generate_schedule(meetings):
    if len(meetings) == 0:
        return 0
    
    # Sort the array of arrays by the first element of each sub array.
    # The first element of each sub array is the meeting start time.
    meetings.sort(key=lambda i: i[0])

    # Create a list to hold meeting rooms. We will manage this as a 
    # min-heap so the meeting with the earliest ending time is on top. 
    active_meetings = list()
    room_schedule = collections.defaultdict(list)

    # walk through each meeting in starting order
    for m in meetings:
        start = m[0]
        end = m[1]
        if len(active_meetings) != 0 and active_meetings[0][0] <= start:
            # We already have meeting rooms in use. But the meeting
            # with the earliest finish time ends before this next
            # meeting starts. We can re-use it's room. Pop it off 
            # the heap. 
            popped_meeting = heapq.heappop(active_meetings)
            room_num = popped_meeting[1]
            room_schedule[room_num].append(m)
            # Push the current meeting's end time onto the heap along with
            # the assigned room number
            heapq.heappush(active_meetings, (end, room_num))
        else:
            room_num = len(active_meetings) + 1
            room_schedule[room_num].append(m)
            heapq.heappush(active_meetings, (end, room_num))
    
    return room_schedule

meetings = [[2,3], [2,4], [4,6], [2,5]]
print("{} exect: 3".format(rooms_needed(meetings)))

# Imagine this calendar that 1 room can satisfy
# R1: [1,2], [3,4], [4,6]
meetings = [[1, 2], [3, 4], [4, 6]]
print("{} exect: 1".format(rooms_needed(meetings)))

# Imagine this calendar that 3 rooms can satisfy
# R1: [1,2], [3,4], [4,6], [6,8]
# R2: [1,4], [4,5], [5,6]
# R3: [2,4], [5,6] 
meetings = [[1,2], [3,4], [4,6], [6,8], [1,4], [4,5], [5,6], [2,4], [5,6]]
print("{} exect: 3".format(rooms_needed(meetings)))

# Test some extreme cases
meetings = []
print("{} exect: 0".format(rooms_needed(meetings)))

meetings = [[1,2]]
print("{} exect: 1".format(rooms_needed(meetings)))

# Let's get random
random.seed()
meetings.clear()
for i in range(50):
    start = random.randint(0, 18)
    end = start + random.randint(1, 2)
    meetings.append([start,end])

print("{} Rooms Needed".format(rooms_needed(meetings)))
room_schedules = generate_schedule(meetings)

for k,v in room_schedules.items():
    print("R{}: {}".format(k, v))

#
# Given an array of intervals, merge the intervals so that any two intervals
# that overlap, are combined. Two intervals, a and b, over lap if 
# b[0] <= a[1] or a[0] <= b[1], that is, if one interval starts before or on
# the same value that another interval ends, they can be merged. 
# 
# Examples: 
# input = [[1,2], [3,4], [5, 6]]
# output = [[1,2], [3,4], [5, 6]]
#
# input = [[1,2], [2,4], [5, 6]]
# output = [[1,4],  [5, 6]]
#
# input = [[1,4], [2,3], [5, 6]]
# output = [[1,4],  [5, 6]]
#


def merge_intervals(intervals):
    intervals.sort(key=lambda i: i[0])
    merged_intervals = list()
    start = intervals[0][0]
    end = intervals[0][1]
    for i in intervals:
        if i[0] <= end:
            if i[1] > end:
                end = i[1]
        else:
            merged_intervals.append([start, end])
            start = i[0]
            end = i[1]
    merged_intervals.append([start, end])
    return merged_intervals

arr = [[18, 30], [1, 35], [18, 30], [36, 40]]
print(merge_intervals(arr))
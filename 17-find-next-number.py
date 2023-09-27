import time
'''
Given an array of integers between 0 and 9 which represent the 
digits of a multi-digit base 10 number with LSD in array[0], 
return the next largest number that can be formed using the same set 
of digits. 

Example: 

Input:   [1,9,5,2]  
          i.e. the number 1,952 
          (one-thousand, nine-hundred and fifty-two)
Return:  [2,1,5,9]
'''

'''
def binary_search(arr, x)
Return a positive integer representing the index of the found number x otherwise a negative 
number that represents the first index beyond the location where x would have been found if
if had existed. 

Examples: 
Given Array [1,2,5,9]
x = 1, return 0
x = 5, return 2
x = 3, return -3 (if 3 were present, it goes in index 2)
X = 0, return -1 (if 0 were present, it goes in index 0)

'''
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -(low+1)


def find_next_nlogn(num):
   
    # eliminate single digit numbers
    if len(num) < 2: 
        return []
    
    # eliminate numbers that are already representing the max possible number with
    # given digits. Examples 4321 and 998877
    rev = num.copy()
    rev.reverse()
    if sorted(num) == rev: 
        return []

    # define a sorted list and append the least significant digit (LSD) of num
    sorted_lsd = list()
    sorted_lsd.append(num[-1])
    i = 0

    # walk backwards through the array starting at the next to last LSD, len(num) - 2
    # reminder: range(start, stop, step)
    for i in range(len(num)-2, -1, -1):
        # look for the current digit in the sorted_lsd's
        r = binary_search(sorted_lsd,num[i])
        
        # the binary algorithm returns a positive number if the digit is found
        # and a negative number if not found. The negative value is the index
        # just after where the current digit would have been found.  

        if r < 0: 
            #this digit wasn't found
            belongs_in_index = abs(r)-1
            if(belongs_in_index < len(sorted_lsd)):
                # a digit greater than num[i] exists in sorted_lsd

                # add the current digit to the LSD list
                sorted_lsd.append(num[i])

                # reset the current digit to the first digit in sorted_lsd that is greater than itself
                num[i] = sorted_lsd[belongs_in_index]

                # remove the substituted digit out of sorted_lsd
                sorted_lsd.pop(belongs_in_index)

                # re-sort sorted_lsd to position the newly added num[i]
                sorted_lsd.sort()

                # we break out of this for loop whose goal was to find some 
                # LSD that was greater than the digit in the current position num[i]
                # since we found it and made the substitution, we can exit this loop
                # and proceed to the next step. 
                break
            else:
                # no lsd is greater than num[i] because num[i] belongs beyond 
                # the current size of the array meaning it's greater than all 
                # existing digits in sorted_lsd

                # add num[i] to sorted_lsd and re-sort the list
                sorted_lsd.append(num[i])
                sorted_lsd.sort()
        else:
            # the digit in num[i] was found in sorted_lsd. we will search for 
            # the first digit in sorted_lsd that is greater than num[i]
            j = 0
            for j in range(r,len(sorted_lsd),1):
                if sorted_lsd[j] > num[i]: 
                    break
            if j < len(sorted_lsd):
                # we have a lsd greater than num[i]
                sorted_lsd.append(num[i])
                num[i] = sorted_lsd[j]
                sorted_lsd.pop(j)
                sorted_lsd.sort()
                break
    
    # Once we have exited the for loop above we have replaced a digit 
    # at position i with the smallest digit below it that is also greater
    # than num[i]. Now we just fill in the digits left in sorted_lsd 
    # in increasing sorted order into the digits less significant than i.

    # starting from i+1 place the sorted lsd's into the array
    i += 1

    for k in range(len(sorted_lsd)):
        num[i]=sorted_lsd[k]
        i+=1

    return num

def find_next_brute(num):
    digits = sorted(num)
    possibilities = {}

    def branch(new_num, digits):
        nonlocal possibilities
        if len(digits) == 0:
            possibilities[int(''.join([str(elem) for elem in new_num]))] = ""
        for i in range(len(digits)):
            d = digits.copy()
            d.pop(i)
            n = new_num.copy()
            n.append(digits[i])
            branch(n, d)
    
    branch(list(), num)
    target = int(''.join([str(elem) for elem in num]))
    ordered_possibilities = sorted(possibilities)
    result = binary_search(ordered_possibilities,target)+1
    return ordered_possibilities[result] if result < len(ordered_possibilities) else []

# Run several tests to verify basic operation and two edge cases.
num = [1,9,5,6]
print(num,"->")
print(find_next_nlogn(num.copy()))
print(find_next_brute(num.copy()))

num = [2]
print(num,"->")
print(find_next_nlogn(num.copy()))
print(find_next_brute(num.copy()))

num = [6,5,4,3]
print(num,"->")
print(find_next_nlogn(num.copy()))
print(find_next_brute(num.copy()))

# The nlogn algorithm can find the solution for a 30 digit number quickly
# But the brute force runtime is untennable
num = [4,5,3,7,0,6,9,9,2,7,0,1,9,1,6,1,1,3,0,2,1,3,3,2,4,2,0,1,4,3]
print(num,"->")
print(find_next_nlogn(num.copy()))
#print(find_next_brute(num.copy()))

# Below we compare the run-time results on a 10 digit number
# In my test, 
#   nlogn algorithm ran in 7709 ns
#   n!    algorithm ran in 5456621917 ns
#   7.09e5 times longer
print()
print("---PERFORMANCE TEST----")
num = [4,5,3,7,0,6,9,9,2,7]

# Use nlogn algorithm to find next number
start = time.perf_counter_ns()
print(find_next_nlogn(num.copy()))
end = time.perf_counter_ns()
print("runtime nlogn (ns): ", end-start)

# Use brute force n! algorithm to find next number
start = time.perf_counter_ns()
print(find_next_brute(num.copy()))
end = time.perf_counter_ns()
print("runtime brute (ns): ", end-start)

#
# Find logest palindrome in a string
# 
# s = 'aaaabbaa'
# answer: 'aabbaa'
#

def is_palendrome(s, l, r):
    while(l<=r):
        if(s[l] != s[r]):
            return False
        else:
            l+=1
            r-=1
    return True

def max_palendrome(s):
    if s == None or len(s) == 0:
        return 0
    max_found = 1
    for size in range(1,len(s), 1):
        for l in range(len(s)):
            r = l+size
            if(r>= len(s)):
                break
            if is_palendrome(s, l, r):
                max_found = max(max_found, r-l+1)
    return max_found

def max_palendrome_dynamic(s):
    # set-up NxN matrix
    m = [[0]*len(s) for i in range(len(s))]

    # set matrix answers for all palindromes of size 1
    # all single character strings are palindromes
    for i in range(len(s)):
        m[i][i] = 1

    max_found = 1

    # set matrix answers for all palindromes of size 2
    size = 2
    for i in range(0, len(s)-size+1, 1):
        j = i+size-1 
        # i and j represent the start and end index of a substring
        # of length 'size'
        if s[i] == s[j]:
            m[i][j] = 1
            max_found = max(max_found, size)

    # set matrix answers for all palindromes of size 3 to max
    for size in range(3, len(s)+1, 1):
        for i in range(0, len(s)-size+1, 1):  # 0 1 2 3 4 (len:5)
            j = i+size-1 
            # i and j represent the start index and end index of a substring
            # of length 'size'
            if s[i] == s[j] and m[i+1][j-1] == 1:
                m[i][j] = 1
                max_found = max(max_found, size)

    return max_found


s = "aaaabbaa"
print(max_palendrome(s))
print(max_palendrome_dynamic(s))

s = "cbabacb"
print(max_palendrome(s))
print(max_palendrome_dynamic(s))

s = "qracbzbcarq"
print(max_palendrome(s))
print(max_palendrome_dynamic(s))

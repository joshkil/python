# Balance the parenthesis in a string
#
# You are given a string with alphanumeric characters and 
# parentheses. Your goal is to return a string with balanced 
# parentheses by removing the fewest characters possible. Note 
# that you cannot add anything to the string.
#
# Examples
#
# "()" -> "()"  
# "b(a)r)" -> "b(a)r"  
# ")(" -> ""  
# "(((((" -> ""  
# ")(())(" -> "(())"
# 
# Note that there can be multiple correct results per input. You 
# just have to return one of the correct results.
#
# "(()()(" -> "()()" OR "(())"  
# "(())())" -> "(()())" OR "(())()"

def balance(s):
    return ""

# main
ex1 = "(()(()"
print("Ballanced '{}' to '{}'".format(ex1, balance(ex1)))

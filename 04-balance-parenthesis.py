def balance(s):
    str_array = list(s)
    open_cnt = 0;
    for i, c in enumerate(str_array):
        if c == '(':
            open_cnt += 1
        if c == ')':
            if open_cnt > 0:
                open_cnt -= 1
            else:
                # remove this close paren
                str_array[i] = '#'
    
    if open_cnt > 0:
        for i in range(len(str_array)-1, -1, -1):
            if open_cnt == 0:
                break
            if str_array[i] == '(':
                str_array[i] = '#'
                open_cnt -= 1
    
    return "".join(str_array).replace("#", "")


# main
ex1 = "(()(()"
print("Ballanced '{}' to '{}'".format(ex1, balance(ex1)))

ex2 = "()"
print("Ballanced '{}' to '{}'".format(ex2, balance(ex2)))

ex3 = "b(a)r)"
print("Ballanced '{}' to '{}'".format(ex3, balance(ex3)))

ex4 = ")("
print("Ballanced '{}' to '{}'".format(ex4, balance(ex4)))

ex5 = "((((("
print("Ballanced '{}' to '{}'".format(ex5, balance(ex5)))

ex6 = ')(())('
print("Ballanced '{}' to '{}'".format(ex6, balance(ex6)))

ex7 = '(()()('
print("Ballanced '{}' to '{}'".format(ex7, balance(ex7)))

ex8 = '(())())'
print("Ballanced '{}' to '{}'".format(ex8, balance(ex8)))
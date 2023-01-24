# A Program to Implement a word search with wildcards
# This version uses a single Trie structure to search for words

# Node Class
# value    - each node has a value which is a single character
# children - each node has a dictionary of child nodes. the key is the 
#            character represented by the child node
# is_word  - a boolean value indicating if this node is the end of
#            a "word path". 
class Node:
    def __init__(self, value, is_word):
        self.value = value
        self.children = {}
        self.is_word = is_word

def add_to_trie(word, root):
    # recursion base case
    if len(word) == 0:
        root.is_word = True
        return

    # split off the first character of the current word
    first_char = word[0:1]
    sufx = word[1:]

    # recursive step
    if first_char in root.children:
        add_to_trie(sufx, root.children[first_char])
    else:
        new_node = Node(first_char, False)
        root.children[first_char] = new_node
        add_to_trie(sufx, new_node)

def setup(words, root):
    for w in words:
        add_to_trie(w.strip(), root)

# convenience function to initiate recursion
def find_words(word, node, num_visits):
    fwords = list()
    return find_words_r(word, node, fwords, num_visits)

# recursive search
def find_words_r(word, node, fwords, num_visits, path=""):
    num_visits[0] +=1

    # recursion base case
    if len(word) == 0:
        if node.is_word:
            fwords.append(path)
        return fwords

    # split the first character off the curent word
    first_char = word[0:1]
    sufx = word[1:] 

    # recursive step
    if first_char in node.children:
        return find_words_r(sufx, node.children[first_char], fwords, num_visits, path + first_char)
    elif first_char == '.':
        for k in node.children.keys():
            find_words_r(sufx, node.children[k], fwords, num_visits, path + k)
        return fwords
    else:
        return fwords


# Main Program 
words = list()
root = Node("", False)

with open("16-words_alpha.txt") as f:

    # Read the dictionary file into a list
    words = list(f)
    setup(words, root)
    print("Loaded {} words.".format(len(words)))

    # Do the search
    num_visits = [0]
    fwords = find_words(".one", root, num_visits)

    # Print the results
    print("Found words: {}. Visited: {}".format(len(fwords), num_visits[0]))
    print(fwords)


    # WORDLE SOLVER
    # The next lines are extra work to further filter the list of found words
    # by excluding words with certain characters or requiring that the words 
    # contain certain characters. There is also an option to prohibit characters 
    # in specific positions which is used to override the list of included characters
    # by specifying that they cannot exist in certain positions. 
    exclude = ['i', 'l', 'c', 'r']
    include = ['d', 'e', 'a']
    anti_positions = {'1':'d', '2':'e'}

    candidates = []
    for w in fwords:
        candidate = True
        for c in exclude:
            if c in w:
                candidate = False
        for c in include: 
            if c not in w:
                candidate = False
        for k, v in anti_positions.items(): 
            if w[int(k)] == v:
                candidate = False
        if candidate: 
            candidates.append(w)

    # print("Found words: {}. Visited: {}".format(len(candidates), num_visits[0]))
    # print(candidates)



# A Program to Implement a word search with wildcards
# This version breaks the search space into partitions by word length
# and creates a unique Trie for all unique word lengths in the dictionary

class Node:
    def __init__(self, value, is_word):
        self.value = value
        self.children = {}
        self.is_word = is_word

def add_to_trie(word, root):
    if len(word) == 0:
        root.is_word = True
        return

    first_char = word[0:1]
    sufx = word[1:]

    if first_char in root.children:
        add_to_trie(sufx, root.children[first_char])
    else:
        new_node = Node(first_char, False)
        root.children[first_char] = new_node
        add_to_trie(sufx, new_node)

def setup(words, roots):
    for w in words:
        if len(w.strip()) in roots: 
            add_to_trie(w.strip(), roots[len(w.strip())])
        else:
            roots[len(w.strip())] = Node("", False)
            add_to_trie(w.strip(), roots[len(w.strip())])

def find_words(word, node, num_visits):
    fwords = list()
    return find_words_r(word, node, fwords, num_visits)

def find_words_r(word, node, fwords, num_visits, path=""):
    num_visits[0] +=1
    if len(word) == 0:
        if node.is_word:
            fwords.append(path)
        return fwords

    first_char = word[0:1]
    sufx = word[1:] 

    if first_char in node.children:
        return find_words_r(sufx, node.children[first_char], fwords, num_visits, path + first_char)
    elif first_char == '.':
        for k in node.children.keys():
            find_words_r(sufx, node.children[k], fwords, num_visits, path + k)
        return fwords
    else:
        return fwords

words = list()
roots = dict()

with open("16-words_alpha.txt") as f:
    words = list(f)
    setup(words, roots)
    print("Loaded {} words.".format(len(words)))

    # Do the search
    num_visits = [0]
    word_to_find = "..."
    if(len(word_to_find) in roots):
        fwords = find_words(word_to_find, roots[len(word_to_find)], num_visits)
        print("Found words: {}. Visited: {}".format(len(fwords), num_visits[0]))
        print(fwords)
    else: 
        print("Found words: {}. Visited: {}".format(0, num_visits[0]))


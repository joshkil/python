def setup(words):
    for w in words:
        1

def find_words(search_str, words):
    fwords = list()
    return fwords

words = ['apple', 'ape', 'bar', 'barn', 'bark']
setup(words)
print("Search 'pear', expect [] : result {}".format(find_words("pear", words)))
print("Search 'ap*', expect ['ape'] : result {}".format(find_words("ap*", words)))
print("Search 'bar*', expect ['barn', 'bark'] : result {}".format(find_words("bar*", words)))
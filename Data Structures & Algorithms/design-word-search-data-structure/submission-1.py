class WordDictionary:

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        tree = self.tree
        for letter in word:
            if letter not in tree:
                tree[letter] = {}
            tree = tree[letter]
        tree["$"] = True

    def search(self, word: str, tree=None) -> bool:
        if tree is None:
            tree = self.tree
        if word == '':
            if type(tree) is dict:
                return "$" in tree
            return False
        for i, letter in enumerate(word):
            if letter == '.':
                for node in tree:
                    if self.search(word[i+1:], tree[node]):
                        return True
                return False
            if letter not in tree:
                return False
            tree = tree[letter]
        return "$" in tree

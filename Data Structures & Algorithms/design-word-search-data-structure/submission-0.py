class CharTree:
    def __init__(self):
        self.chars = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = CharTree()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.chars:
                cur.chars[c] = CharTree()
            cur = cur.chars[c]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        def _search(self, current_node: CharTree, index: int) -> bool:
            if index == len(word):
                return current_node.end
            char = word[index]
            if char == ".":
                for node in current_node.chars.values():
                    if _search(self, node, index+1): return True
                return False
            if char not in current_node.chars:
                return False
            else:
                return _search(self, current_node.chars[char], index+1)
        return _search(self, cur, 0)



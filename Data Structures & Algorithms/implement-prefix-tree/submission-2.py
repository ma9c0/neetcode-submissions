class PrefixTree:

    class Node:
        def __init__(self):
            self.nexts = [None for i in range(256)]

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for let in word:
            if curr.nexts[ord(let)] is None:
                curr.nexts[ord(let)] = self.Node()
            curr = curr.nexts[ord(let)]
        curr.nexts[0] = self.Node()

    def search(self, word: str) -> bool:
        curr = self.root
        for let in word:
            if curr.nexts[ord(let)] is None:
                return False
            curr = curr.nexts[ord(let)]
        if curr.nexts[0] is not None:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for let in prefix:
            if curr.nexts[ord(let)] is None:
                return False
            curr = curr.nexts[ord(let)]
        return True
        
        
import string 
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # graph: no connection graph, but at every word, we check its neighbors by replacing all letters of the current word
        wordset = set(wordList)
        if beginWord in wordset:
            wordset.remove(beginWord)

        # BFS from the beginWord and return as endWord is reached using a Deque
        dq = deque([(beginWord, 0)])
        lowercase_list = list(string.ascii_lowercase)

        def get_neighbors(word, depth):
            neighbors = []
            for index, char in enumerate(list(word)):
                for replace in lowercase_list:
                    if char != replace:
                        new_word = word[:index] + replace + word[index+1:]
                        if new_word in wordset:
                            neighbors.append((new_word, depth + 1))
                            wordset.remove(new_word)
            return neighbors

        while dq:
            current, current_depth = dq.popleft()

            if current == endWord:
                return current_depth + 1
                
            dq.extend(get_neighbors(current, current_depth))

        return 0
            
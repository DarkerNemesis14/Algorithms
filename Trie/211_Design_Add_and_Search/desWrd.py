class Node:
    def __init__(self):
        self.children = dict()
        self.isWord = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.isWord = True

    def _srch(self, node: Node, word: str):
        for i in range(len(word)):
            if word[i] == '.':
                for child in node.children.values():
                    if self._srch(child, word[i+1:]):
                        return True
                return False
            elif word[i] not in node.children:
                return False
            node = node.children[word[i]]
        
        return node.isWord

    def search(self, word: str) -> bool:
        return self._srch(self.root, word)
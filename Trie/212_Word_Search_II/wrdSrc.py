class Node:
    def __init__(self):
        self.children = dict()
        self.word = None

class Trie:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.word = word

    def search(self, board: List[List[str]]) -> List[str]:
        ret = set()

        dirtn = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()
        def _srch(node: Node, r: int, c: int):
            if board[r][c] not in node.children:
                return []
            node = node.children[board[r][c]]

            if node.word and node.word not in ret:
                ret.add(node.word)

            visited.add((r, c))
            for i, j in dirtn:
                row = r + i
                col = c + j
                if 0 <= row < len(board) and 0 <= col < len(board[row]) and (row, col) not in visited:
                    _srch(node, row, col)
            visited.remove((r, c))

        for i in range(len(board)):
            for j in range(len(board[i])):
                _srch(self.root, i, j)
        
        return list(ret)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.addWord(word)

        ret = trie.search(board)

        return ret
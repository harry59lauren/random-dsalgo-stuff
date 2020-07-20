__all__ = ['Trie']


class TrieNode:

    def __init__(self):
        self.map = dict()
        self.end_of_word = False

class Trie:

        
    def __init__(self):
       self.root = TrieNode()

    def insert(self, s):
        self.root = self._insert(s, self.root)

    def starts_with(self, c):
        l = []
        self.get_all_words(self.root.map[c],c ,l)
        return l
    
    def _insert(self, s, node):
        if s:
            node.map[s[0]] = self._insert(s[1:], node.map.get(s[0], TrieNode()))    
        else:
            node.end_of_word = True
        return node

    def get_all_words(self, node: TrieNode, s, l):
        if node.end_of_word:
            l.append(s)
        for c in sorted(node.map.keys()):
            self.get_all_words(node.map[c], s + c, l)

    def entries(self):
        words = []
        self.get_all_words(self.root,'',words)
        return words



t = Trie()

t.insert('happy')
t.insert('happen')
t.insert('quarantine')
t.insert('hap')
t.insert("apple")
t.insert("bufoon")
t.insert('happy')
t.insert('a')

print(t.starts_with('h'))

print(t.entries())

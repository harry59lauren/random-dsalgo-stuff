from dataclasses import dataclass


class UnionFind:

    def __init__(self,n):
        self._connections = [i for i in range(n)]
    
    @property
    def connections(self):
        return self._connections

    def union(self, p, q):
        if (0 > p > n - 1) or (0 > q > n - 1):
            raise ValueError((f'p and q must between values 0 and {len(connections)}'))
        self._connections[q] = self._connections[p]

    
    def is_connected(p, q):
        pass



    

if __name__ == '__main__':

    uf = UnionFind(10)
    print(uf.connections)
    uf.union(0, 9)
    uf.union(9, 7)
    print(uf.connections)


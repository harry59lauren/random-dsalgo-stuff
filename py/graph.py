import collections
import pprint

class IdGraph:

    def __init__(self):
        self.vertices = {}

    def link(self, p, q):

        if p not in self.vertices.keys():
            self.vertices[p] = set()
        if q not in self.vertices.keys():
            self.vertices[q] = set()

        self.vertices[p].add(q)
        self.vertices[q].add(p)


    def is_connected(self, p, q):
        return self.ispath_bfs(p, q)


    def ispath_bfs(self, s, e):

        queue, visited = collections.deque([s]), set()

        while queue:
            node = queue.popleft()
            if node == e:
                return True
            visited.add(node)
            queue.extend(self.vertices[node] - visited)

        return False

    def __str__(self):
        return str(self.vertices)



if __name__ == '__main__':

    idgraph = IdGraph()

    with open('connections.txt') as conn_file:
        for line in conn_file:
            p, q = [int(v) for v in line.split()]
            idgraph.link(p,q)

    pprint.pprint(idgraph.vertices)

    print(idgraph.is_connected(1,6))
    print(idgraph.is_connected(3,1))
    print(idgraph.is_connected(5,3))


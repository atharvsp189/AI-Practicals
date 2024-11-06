from queue import PriorityQueue
v = 14


class Graph:
    G = {}
    
    def __init__(self, name):
        self.name = name
        self.G = {}
    
    def addnode(self, V):
        if V not in self.G.keys():
            self.G[V] = []
        
    def addedge(self, V, T, C, one_way= False):
        if(one_way == True):
            self.G[V].append([T, C])
        else:
            self.G[V].append([T, C])
            self.G[T].append([V, C])
            
    def display(self):
        for i in self.G.keys():
            print(i, " -> ", end =" ")
            for j in self.G[i]:
                print(j, end =" ")
            print()

    def BestFirstSearch(self, source, target):
        visited = {key:False for key in self.G}
        pq = PriorityQueue()
        pq.put((0, source))
        path =  []
        visited[source] = True
        
        while pq.empty() == False:
            u = pq.get()[1]
            path.append(u)
            if u == target:
                break
            for v, c in self.G[u]:
                if visited[v] == False:
                    visited[v] = True
                    pq.put((c, v))
        return path

g = Graph("grph")

g.addnode('A')
g.addnode('B')
g.addnode('C')
g.addnode('D')
g.addnode('E')
g.addnode('F')
g.addnode('G')
g.addnode('H')
g.addnode('I')
g.addnode('J')

g.addedge('A', 'B', 6)
g.addedge('A', 'F', 3)
g.addedge('B', 'C', 3)
g.addedge('B', 'D', 2)
g.addedge('C', 'D', 1)
g.addedge('C', 'E', 8)
g.addedge('D', 'C', 1)
g.addedge('D', 'E', 8)
g.addedge('E', 'I', 5)
g.addedge('E', 'J', 5)
g.addedge('F', 'G', 1)
g.addedge('F', 'H', 7)
g.addedge('G', 'I', 3)
g.addedge('H', 'I', 2)
g.addedge('I', 'E', 5)
g.addedge('I', 'J', 3)

# print(graph)
g.display()

BestSearchPath = g.BestFirstSearch("A", "J")


print("BestSearchPath : ", BestSearchPath)
from queue import PriorityQueue
v = 14


class Graph:
    G = {}
    
    def __init__(self, name):
        self.name = name
        self.G = {}
    
    def addnode(self, v):
        if v not in self.G.keys():
            self.G[v] = []
        
    def addedge(self, v, t, c, one_way= True):
        if(one_way == True):
            self.G[v].append([t, c])
        else:
            self.G[v].append([t, c])
            self.G[t].append([v, c])
            
    def display(self):
        for i in self.G.keys():
            print(i, " -> ", end =" ")
            for j in self.G[i]:
                print(j, end =" ")
            print()


    def get_neighbors(self, v):
        if v in self.G.keys():
            return self.G[v]
        else:
            return None

    def aStarSearch(self, source, target):

        def h(n):
            H_dist = {
                'A': 10,
                'B': 8,
                'C': 5,
                'D': 7,
                'E': 3,
                'F': 6,
                'G': 5,
                'H': 3,
                'I': 1,
                'J': 0             
            }
            return H_dist[n]

        open_set = set(source)
        closed_set = set()
        g = {} # distance
        parents = {} # for tracing path
        g[source] = 0
        parents[source] = source
        
        while len(open_set) > 0:
            n = None
            
            for v in open_set:
                if n == None or ( g[v] + h(v) < g[n] + h(n) ):
                    n = v

            if n == target or g[n] == None:
                pass
            else:
                for (m, weight) in self.get_neighbors(n):
                    if m not in open_set and n not in closed_set:
                        open_set.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight
                    else:
                        if g[m] > g[n] + weight:
                            g[m] = g[n] + weight
                            if n in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
            if n == None:
                print("Path does not Exist")
                return None
            
            if n == target:
                path = []
                
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
                    
                path.append(source)
                path.reverse()
                return path
            open_set.remove(n)
            closed_set.add(n)
            
        print("Path does not Exist")
        return None


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

AStarPath = g.aStarSearch("A", "J")

print("AStarPath : ", AStarPath)


import heapq

# Prim's Algorithm using Min-Heap (Priority Queue)
def prim(graph, start_node):
    # Number of nodes
    n = len(graph)
    
    # Track visited nodes
    visited = [False] * n
    
    # Priority Queue to store edges (weight, node)
    min_heap = []
    
    # Add starting node to the min-heap
    heapq.heappush(min_heap, (0, start_node)) 
    
    # Initialize MST result list
    mst_edges = []
    total_weight = 0
    
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        
        # If u is already visited, skip it
        if visited[u]:
            continue
        
        # Mark u as visited
        visited[u] = True
        total_weight += weight
        
        # Add the edge to MST
        if weight != 0:
            mst_edges.append((prev_u, u, weight))
        
        # Add all adjacent edges to the min-heap
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                prev_u = u
    
    return mst_edges, total_weight

# Kruskal's Algorithm using Union-Find (Disjoint Set)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        
        # Union by rank
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False

def kruskal(graph, n):
    # Sort all edges in ascending order
    edges = []
    for u in range(n):
        for v, w in graph[u]:
            if u < v:  # To avoid duplicate edges (since undirected)
                edges.append((w, u, v))
    
    edges.sort()  # Sort edges by weight
    
    # Create a union-find structure
    uf = UnionFind(n)
    
    mst_edges = []
    total_weight = 0
    
    for weight, u, v in edges:
        if uf.union(u, v):  # If u and v are in different components
            mst_edges.append((u, v, weight))
            total_weight += weight
    
    return mst_edges, total_weight

# Graph representation (Adjacency List)
# graph[u] = [(v1, w1), (v2, w2), ...] where (v1, w1) means an edge from u to v1 with weight w1
graph = [
    [(1, 10), (3, 30), (4, 50)],  # edges from node 0
    [(0, 10), (2, 20)],           # edges from node 1
    [(1, 20), (3, 10)],           # edges from node 2
    [(0, 30), (2, 10), (4, 60)],  # edges from node 3
    [(0, 50), (3, 60)]            # edges from node 4
]

# Number of nodes
n = len(graph)

# Prim's Algorithm
mst_prim, total_weight_prim = prim(graph, 0)
print("Prim's Algorithm MST:")
for edge in mst_prim:
    print(f"Edge: {edge[0]} - {edge[1]} with weight {edge[2]}")
print(f"Total Weight: {total_weight_prim}")

# Kruskal's Algorithm
mst_kruskal, total_weight_kruskal = kruskal(graph, n)
print("\nKruskal's Algorithm MST:")
for edge in mst_kruskal:
    print(f"Edge: {edge[0]} - {edge[1]} with weight {edge[2]}")
print(f"Total Weight: {total_weight_kruskal}")

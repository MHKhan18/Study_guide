from typing import List, Dict, Tuple

class UnionFind:
    
    def __init__(self, size: int) -> None:
        self.parent = [i for i in range(size)]
        
    
    def find(self, p: int) -> int:
        
        root = p
        while self.parent[root] != root:
            root = self.parent[root]
        
        # path compression
        while p != root :
            next_node = self.parent[p]
            self.parent[p] = root 
            p = next_node
            
        return root
    
    def unify(self, p:int, q: int) -> None:
        
        root_p, root_q = self.find(p), self.find(q)
    
        if root_p == root_q:
            return
        
        self.parent[root_p] = root_q
        

class MST_Kruskal:
    
    def __init__(self, graph, num_nodes) -> None:
        '''input graph should be in edge list form'''
        
        self.graph = graph
        self.n = num_nodes
        
        self.union_find = UnionFind(self.n)
        
    
    def solve(self) -> Tuple[int, List[Tuple[int, int]]]:
        
        
        self.graph.sort(key = lambda edge_item: edge_item[2])
        
        mst_edges = []
        mst_cost = 0
        
        num_mst_edges = self.n - 1
        num_graph_edges = len(self.graph)
        
        i , j = 0, 0
        
        while i < num_mst_edges and j < num_graph_edges:
            
            from_node, to_node, cost = self.graph[j]
            
            root_from = self.union_find.find(from_node)
            root_to = self.union_find.find(to_node)
            
            if root_from != root_to:
                self.union_find.unify(from_node, to_node)
                mst_edges.append((from_node, to_node))
                mst_cost += cost
                i += 1
            
            j += 1
        
        if i != num_mst_edges:
            return (None, None)
        
        return (mst_cost, mst_edges)
                
    
    
    
    
def adj_lst_to_edge_lst(graph: Dict[int, List[Tuple[int, int]]]) -> List[Tuple[int, int, int]]:
    
    edge_lst = []
    for from_node in graph:
        for (to_node, cost) in graph[from_node]:
            edge_lst.append((from_node, to_node, cost))
    
    return edge_lst
    

if __name__ == "__main__":

    graph = {
        0: [(1, 10), (2, 1), (3, 4)],
        1: [(0, 10), (2, 3), (4, 0)],
        2: [(0, 1), (1, 3), (5, 8), (3, 2)],
        3: [(0, 4), (2, 2), (5, 2), (6, 7)],
        4: [(1, 0), (5, 1), (7, 8)],
        5: [(2, 8), (4, 1), (7, 9), (6, 6), (3, 2)],
        6: [(3, 7), (5, 6), (7, 12)],
        7: [(6, 12), (5, 9), (4, 8)],
    }
    
    graph_2 = [
        [0, 1, 1], 
        [0, 2, 2],
        [1, 2, 3],
        [1, 4, 3],
        [4, 3, 2],
        [3, 2, 2],
        [1, 3, 1],
        [2, 4, 1], 
        [4, 5, 3],
        [3, 5, 4]
    ]
    
    graph_edge_lst = adj_lst_to_edge_lst(graph)
    mst_kruskal_1 = MST_Kruskal(graph = graph_edge_lst, num_nodes = 8)
    mst_cost, mst_path = mst_kruskal_1.solve()
    print(f'Kruskal Algo Run \n MST cost: {mst_cost}, MST path: {mst_path}')
    
    mst_kruskal_2 = MST_Kruskal(graph = graph_2, num_nodes = 6)
    mst_cost_2, mst_path_2 = mst_kruskal_2.solve()
    print(f'Kruskal Algo Run \n MST cost: {mst_cost_2}, MST path: {mst_path_2}')
    
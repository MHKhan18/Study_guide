from typing import List

class EulerianPathFinder:
    """Checks existence and finds path on Directed Graphs. Runtime: O(E)"""

    def __init__(self, graph) -> None:
        self.graph = graph
        self.n = len(self.graph)

        self.edge_count = 0
        self.in_count = [0] * self.n
        self.out_count = [0] * self.n
        self.path: List[int] = []

    def solve(self) -> List[int]:
        
        self.count_in_out_edges()
        
        if not self.has_eulerian_path():
            return None 
        
        start_node = self.get_start_node()
        self.dfs(start_node)
        
        if len(self.path) == self.edge_count + 1:
            return self.path
        
        return None # input graph is disconnected

    def count_in_out_edges(self):

        for from_node in self.graph:
            for to_node in self.graph[from_node]:
                self.in_count[to_node] += 1
                self.out_count[from_node] += 1
                self.edge_count += 1 

    def has_eulerian_path(self):

        num_start_nodes, num_end_nodes = 0, 0
        for i in range(self.n):
            if (
                self.out_count[i] - self.in_count[i] > 1
                or self.in_count[i] - self.out_count[i] > 1
            ):
                return False
            elif self.out_count[i] - self.in_count[i] == 1:
                num_start_nodes += 1
            elif self.in_count[i] - self.out_count[i] == 1:
                num_end_nodes += 1

        return (num_end_nodes == 0 and num_start_nodes == 0) or (
            num_end_nodes == 1 and num_start_nodes == 1
        )

    def get_start_node(self) -> int:
        
        start = 0
        for i in range(self.n):
            
            # unique start node
            if self.out_count[i] - self.in_count[i] == 1:
                return i 
            
            # start at any node with an outgoing edge
            if self.out_count[i] > 0:
                start = i 
        
        return start 

    def dfs(self, at: int):
        
        while self.out_count[at] > 0:
            self.out_count[at] -= 1
            adj_lst_index = self.out_count[at]
            next_node = self.graph[at][adj_lst_index]
            self.dfs(next_node)
            
        self.path.insert(0, at)
        

if __name__ == "__main__":
    
    graph = {
        0 : [],
        1 : [2, 3],
        2 : [2, 4, 4],
        3 : [1, 2, 5],
        4 : [3, 6],
        5 : [6],
        6 : [3],
    }
    
    epf = EulerianPathFinder(graph)
    eulerian_path = epf.solve()
    print(eulerian_path)
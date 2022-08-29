

class FindBridges:
    
    def __init__(self, graph) -> None:
        self.graph = graph
        self.n = len(graph)
        self.ids = [float('inf')] * self.n
        self.lows = [float('inf')] * self.n
        self.visited = [False] * self.n 
        self.bridges = [] 
        self.cur_id = 0
    
    def dfs(self, at, parent):
       
        self.visited[at] = True
        self.ids[at] = self.cur_id
        self.lows[at] = self.cur_id
        self.cur_id += 1
        
        for to in self.graph[at]:
            
            # handle undirected graphs
            if to == parent: 
                continue
            
            if not self.visited[to]:
                self.dfs(to, at)
                
                self.lows[at] = min(self.lows[at], self.lows[to])
               
                
                if self.ids[at] < self.lows[to]:
                    self.bridges.append((at, to))
                    
            else:
                self.lows[at] = min(self.lows[at], self.ids[to])
               
    
    
    def solve(self):
        
        for vertex in range(self.n):
            if not self.visited[vertex]:
                self.dfs(vertex, -1)
                
        return self.bridges


class FindArticulationPoint:
    
    def __init__(self, graph) -> None:
        self.graph = graph
        self.n = len(graph)
        self.ids = [float('inf')] * self.n
        self.lows = [float('inf')] * self.n
        self.visited = [False] * self.n 
        self.is_art = [False] * self.n 
        self.cur_id = 0
        self.out_edge_count = 0
    
    def dfs(self, root , at, parent):
        
        if parent == root:
            self.out_edge_count += 1
        
        self.visited[at] = True
        self.lows[at] = self.ids[at] = self.cur_id
        self.cur_id += 1
        
        for to in self.graph[at]:
            
            if to == parent:
                continue
            
            if not self.visited[to]:
                self.dfs(root, to, at)
                
                self.lows[at] = min(self.lows[at], self.lows[to])
                
                if self.ids[at] < self.lows[to]: # articulation point
                    self.is_art[at] = True
                if self.ids[at] == self.lows[to]: # cycle
                    self.is_art[at] = True
               
                    
            else:
                self.lows[at] = min(self.lows[at], self.ids[to])
    
    def solve(self):
        
        for i in range(self.n):
            if not self.visited[i]:
                self.out_edge_count = 0 # reset -- a new tree
                self.dfs(i, i, -1)
                self.is_art[i] = self.out_edge_count > 1 
        
        res = []
        for i in range(self.n):
            if self.is_art[i]:
                res.append(i)
                
        return res 
    
                
    


if __name__ == "__main__":
    
    # undirected graph 
    graph1 = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3, 5],
        3: [2, 4],
        4: [3],
        5: [2, 6, 8],
        6: [5, 7],
        7: [6, 8],
        8: [5, 7]
    }
        
    find_bridges = FindBridges(graph1)
    bridges_graph1 = find_bridges.solve()
    print(bridges_graph1)
    print(find_bridges.ids)
    print(find_bridges.lows)
    
    find_ap = FindArticulationPoint(graph1)
    aps = find_ap.solve()
    print(aps)
    print(find_ap.ids)
    print(find_ap.lows)
    
    
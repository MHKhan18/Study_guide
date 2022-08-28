

from collections import deque

class SCC_TARJAN:
        
    def __init__(self, graph) -> None:
        self.graph = graph 
        self.n = len(graph)
        
         # index i -> node i
        self.ids = [-1] * self.n # visited + id
        self.lows = [float('inf')] * self.n # vertex with lowest id reachable from node i
        self.sccs = [float('inf')] * self.n
        self.on_stack = [False] * self.n 
        self.stack = deque()
        self.cur_id = 0
        self.scc_count = 0
        
        
    def dfs_tarjan(self, at):
        
        self.stack.append(at)
        self.on_stack[at] = True
        self.ids[at] = self.cur_id
        self.lows[at] = self.cur_id
        self.cur_id += 1

        for to in self.graph[at]:
            if self.ids[to] == -1: 
                self.dfs_tarjan(to)
            if self.on_stack[to]: # back edge, cross edges are not in stack 
                self.lows[at] = min(self.lows[at], self.lows[to]) # propagate low value
         
        if self.ids[at] == self.lows[at]:
            while True:
                node = self.stack.pop()
                self.on_stack[node] = False
                self.lows[node] = self.ids[at]
                self.sccs[node] = self.scc_count
                if node == at:
                    break 
            self.scc_count += 1
    
    def solve(self):
        for i in range(self.n):
            if self.ids[i] == -1:
                self.dfs_tarjan(i)
        return self.sccs
    

class SCC_KOSARAJU:
    
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        self.stack = deque()
        self.visited = [False] * self.n 
        self.graph_transpose = {}
        self.sccs = [float('inf')] * self.n 
    
    def transpose(self):
        
        graph = {}
        for i in range(self.n):
            graph[i] = []
        
        for start in self.graph:
            for end in self.graph[start]:
                graph[end].append(start)
                
        
        self.graph_transpose = graph
    
    def get_postorder(self, at: int):
        
        self.visited[at] = True
        for to in self.graph[at]:
            if not self.visited[to]:
                self.get_postorder(to)
        
        self.stack.append(at)
    
    def set_scc_group(self, group_id: int, node: int):
        
        self.visited[node] = True
        self.sccs[node] = group_id
        
        for to in self.graph_transpose[node]:
            if not self.visited[to]:
                self.set_scc_group(group_id, to)
        
    def solve(self):
        
        # get post order of nodes in stack 
        for i in range(self.n):
            if not self.visited[i]:
                self.get_postorder(i)
        
        self.transpose()
        self.visited = [False] * self.n # clean up from previous dfs
        
        group_id = 0
        while self.stack:
            cur_node = self.stack.pop()
            if not self.visited[cur_node]:
                self.set_scc_group(group_id, cur_node)
                group_id += 1
        
        return self.sccs
    
    

            
if __name__ == "__main__":

    graph1  = {
        0: [1],
        1: [2, 4, 6],
        2: [3],
        3: [2],
        4: [5],
        5: [2, 3, 4],
        6: [0 , 4]
    }
    
    graph2 = {
        0: [1, 4],
        1: [5],
        2: [1, 3, 6],
        3: [6],
        4: [0, 5],
        5: [2, 6],
        6: [7],
        7: [3]
    }

    
    tarjan_scc1 = SCC_TARJAN(graph1)
    tarjan_res1 = tarjan_scc1.solve()
    print(tarjan_res1)
    
    tarjan_scc2 = SCC_TARJAN(graph2)
    tarjan_res2 = tarjan_scc2.solve()
    print(tarjan_res2)
    
    kosaraju_scc1 = SCC_KOSARAJU(graph1)
    kosaraju_res1 = kosaraju_scc1.solve()
    print(kosaraju_res1)
    
    kosaraju_scc2 = SCC_KOSARAJU(graph2)
    kosaraju_res2 = kosaraju_scc2.solve()
    print(kosaraju_res2)
    
  
from typing import List

INF = float("inf")

class AllPairShortestPath:

    def __init__(self, matrix: List[List[int]]):

        self.n = len(matrix)
        self.dp = [[INF]*self.n for _ in range(self.n)]
        self.next = [[INF]*self.n for _ in range(self.n)]

        self.solved = False

        for i in range(self.n):
            for j in range(self.n):
                if matrix[i][j] != INF:
                    self.dp[i][j] = matrix[i][j]
                    self.next[i][j] = j 
    
    def solve(self) -> None:

        if self.solved: 
            return 
        
        # core algorithm 
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.dp[i][k] + self.dp[k][j] < self.dp[i][j]:
                        self.dp[i][j] = self.dp[i][k] + self.dp[k][j] #e.g. A->B === A->K + k->B
                        self.next[i][j] = self.next[i][k] #first node in i -> k 

        # identify negative cycles
        # propagate -1 to every edge that is either part of or reaches a negative cycle
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if self.dp[i][k] != INF and self.dp[k][j] != INF and self.dp[k][k] < 0:
                        self.dp[i][j] = float('-inf')
                        self.next[i][j] = -1

        self.solved = True

    def reconstruct_shortest_path(self, start: int, end: int) -> List[int]:

        if not self.solved:
            self.solve()
        
        if self.dp[start][end] == INF:
            return []
        
        path = [start]
        at = start
        while at != end:
            at = self.next[at][end]
            if at == -1: # negative cycle -> infinite number of shortest path
                return None
            path.append(at)
    
        return path 



if __name__ == "__main__":

    graph = [
        # a,  b,   c,  d
        [0, INF, 3, INF],
        [2, 0, INF, INF],
        [INF, 7, 0, 1],
        [6, INF, INF, 0],
    ]

    apsp = AllPairShortestPath(graph)
    apsp.solve()

    dp = apsp.dp
    print(dp)

    path = apsp.reconstruct_shortest_path(1 , 3) # b -> d
    res = "->".join(list(map(lambda  x: chr(x + ord('A')) , path)))
    print(res)

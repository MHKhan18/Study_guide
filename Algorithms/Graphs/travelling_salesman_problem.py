from typing import List


class TravellingSalesmanSolver:
    
    def __init__(self, graph: List[List[int]], start: int) -> None:
        # Assume: grah is N*N square matrix
        self.graph = graph
        self.n = len(self.graph)
        self.start = start 
        self.end_state = (1 << self.n) - 1
        

        self.memo = []
        for _ in range(self.n):
            self.memo.append([float("inf")] * (2 ** self.n))

        self.optimal_path = [None] * self.n
        self.min_cost = float('inf')
    
    
    def solve(self):
        self.__setup()
        self.__compute()
        self.min_cost = self.__get_min_cost()
        self.optimal_path = self.__get_min_path()
        
        path =  list(map(lambda s: "->".join(s), map(lambda n: str(n), self.optimal_path)))  
        return (self.min_cost, path)       
    
    def __setup(self):
        
        # initialize memo with info from graph 
        start = self.start
        for end in range(self.n):
            if end == start:
                continue
            self.memo[end][(1 << start) | (1 << end)] = self.graph[start][end]
    
    def __compute(self):
        
        start = self.start
        
        for r in range(3 , self.n+1):
            for subset in get_r_comb_n(r , self.n):
                if not_in(start, subset):
                    continue
                for next in range(self.n):
                    if next == start or not_in(next, subset):
                        continue
                    subset_without_next = subset ^ (1 << next)
                    min_dist = float('inf')
                    # case when there are multiple nodes in the subpath
                    # e.g [A,B,C] and we are picking D as next
                    # let start be S
                    # so we need to pick min of [ S->A + A->D, S->B + B->D, S->C+C->D ]
                    for end in range(self.n):
                        if end == start or end == next or not_in(end, subset):
                            continue
                        new_dist = self.memo[end][subset_without_next] + self.graph[end][next]
                        if new_dist < min_dist:
                            min_dist = new_dist
                    self.memo[next][subset] = min_dist
                    
    def __get_min_cost(self) -> int:
        
        start = self.start
        min_cost = float('inf')
        
        for i in range(self.n):
            if i == start:
                continue
            tour_cost = self.memo[i][self.end_state] + self.graph[i][start]
            if tour_cost < min_cost:
                min_cost = tour_cost
        
        return min_cost
    
    
    def __get_min_path(self) -> List[int]:
        
        min_path = []
        
        last_index = self.start 
        cur_state = self.end_state
        min_path.append(self.start)
        
        for _ in range(1 , self.n):
            
            best_index = -1
            best_dist = float('inf')
            
            for j in range(self.n):
                
                if j == self.start or not_in(j, cur_state):
                    continue
                new_dist = self.memo[j][cur_state] + self.graph[j][last_index]
                if new_dist < best_dist:
                    best_index = j 
                    best_dist = new_dist
            
            
            last_index = best_index
            cur_state = cur_state ^ (1 << best_index)
            min_path.append(best_index)
        
        min_path.append(self.start)
        min_path.reverse()
        
        return min_path
             
        
         
            
                        
                        
            
            
            
        

        


def not_in(i: int, subset: int):
    # returns ture if ith is not set in subset
    return ((1 << i) & subset) == 0


def get_r_comb_n(r: int, n: int) -> List[int]:
    subsets_lst = []
    get_r_comb_n_util(0, 0, r, n, subsets_lst)
    return subsets_lst


def get_r_comb_n_util(cur_set: int, at: int, r: int, n: int, subsets_lst: List[int]):

    # bit representation of cur_set is the combination of elements of the set

    elements_left_to_pick = n - at
    if elements_left_to_pick < r:
        return

    if r == 0:
        subsets_lst.append(cur_set)
    else:
        for i in range(at, n + 1):

            cur_set ^= 1 << i  # include ith element
            get_r_comb_n_util(cur_set, i + 1, r - 1, n, subsets_lst)
            cur_set ^= 1 << i  # backtrack


if __name__ == "__main__":

    graph = [
        [0, 1, 15, 6],
        [2, 0, 7,  3],
        [9, 6, 0, 12],
        [10, 4, 8, 0]
    ]
    tsp = TravellingSalesmanSolver(graph, 0)
    min_cost, min_path = tsp.solve()
    print(f'min_cost = {min_cost}, min_path = {min_path}')
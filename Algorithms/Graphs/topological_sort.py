
from collections import deque
from collections import OrderedDict

def topological_dfs(graph):
    # Graph is in adjacent list form
    # Vertices are capital English alphabets in sequence from A

    # Precondition: No Cycles in the directed graph
    # nodes in decreasing post order are topologically sorted

    num_vertices = len(graph)
    sorted_lst = []
    
    visited = [False] * num_vertices # check for cycle
    
    def dfs_util(vertex):

        visited[ord(vertex)-ord('A')] = True 
        
        for neighbor in graph[vertex]:
            if not visited[ord(neighbor)-ord('A')]:
                dfs_util(neighbor)


        # add items in increasing post order
        # i.e. vertices that are post visited first, are added first
        sorted_lst.append(vertex)

   
    for vertex in graph:  # disconnected graphs
        if not visited[ord(vertex)-ord('A')]:
            dfs_util(vertex)

    sorted_lst.reverse()
    return sorted_lst
           

def index(vertex):
    return ord(vertex) - ord('A')

def topological_Kahn(graph):

    num_vertices = len(graph)
    
    sorted_lst = []
    in_degree = [0] * num_vertices

    for node in graph:
        for neighbor in graph[node]:
            in_degree[index(neighbor)] += 1

    queue = deque()  # contains vertices with zero in-degree currently
    
    for node in graph:
        if in_degree[index(node)] == 0:
            queue.append(node)
    
    while queue:

        cur_node = queue.popleft()
        sorted_lst.append(cur_node)

        # reduce in-degree of cur_node's children
        for neighbor in graph[cur_node]:
            in_degree[index(neighbor)] -= 1

            if in_degree[index(neighbor)] == 0:
                queue.append(neighbor)

    if len(sorted_lst) != num_vertices:
        raise AssertionError('Input is not a DAG')

    return sorted_lst


def get_all_topological_orders(graph: dict):

    num_vertices = len(graph)

    in_degree = [0] * num_vertices
    for node in graph:
        for neighbor in graph[node]:
            in_degree[index(neighbor)] += 1

    
    discovered = [False] * num_vertices # keeps track if a vertex is used in current enumeration

    all_paths = []
    
    def get_all_util(cur_path: list , discovered: list , in_degree: list):

        for node in graph: # try every node in all indices

            if in_degree[index(node)] == 0 and (not discovered[index(node)]):

                for neighbor in graph[node]:
                    in_degree[index(neighbor)] -= 1
                discovered[index(node)] = True
                cur_path.append(node)

                get_all_util(cur_path , discovered , in_degree)

                # backtrack
                for neighbor in graph[node]:
                    in_degree[index(neighbor)] += 1
                discovered[index(node)] = False
                cur_path.pop()

        if len(cur_path) == num_vertices:
            all_paths.append(list(cur_path))

    get_all_util([] , discovered , in_degree)
    return all_paths












if __name__ == "__main__":
    graph = OrderedDict({
        'A' : [],
        'B' : [],
        'C' : ['D'],
        'D' : ['B'],
        'E' : ['A' , 'B'],
        'F' : ['A' , 'C']
    })


    res_dfs = topological_dfs(graph)
    print(res_dfs)

    res_kahn = topological_Kahn(graph)
    print(res_kahn)
    
    print("All orders:")
    all_orders = get_all_topological_orders(graph)

    
    for path in all_orders:
        print(path)
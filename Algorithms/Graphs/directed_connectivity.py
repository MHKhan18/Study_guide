
from collections import OrderedDict

def scc_Kosaraju(graph):
    # Graph is in adjacent list form
    # Vertices are capital English alphabets in sequence from A

    num_vertices = len(graph)
    
    visited = [False] * num_vertices # check for cycle
    topsort_stack = []

    def dfs_util(vertex):
    
        visited[ord(vertex)-ord('A')] = True 
        
        for neighbor in graph[vertex]:
            if not visited[ord(neighbor)-ord('A')]:
                dfs_util(neighbor)


        # add items in increasing post order
        # i.e. vertices that are post visited first, are added first
        topsort_stack.append(vertex)

   
    for vertex in graph:  # disconnected graphs
        if not visited[ord(vertex)-ord('A')]:
            dfs_util(vertex)


    visited = [False] * num_vertices # for second dfs


    def reverse_graph(graph):

        reversed_graph = OrderedDict()

        for node in graph:
            reversed_graph[node] = []

        for node in graph:
            for neighnor in graph[node]:
                reversed_graph[neighnor].append(node)
                
        return reversed_graph

    
    graph = reverse_graph(graph)
    
    strongly_connected_components = []
    

    def dfs_util2(vertex):
        
        visited[ord(vertex)-ord('A')] = True 
        
        for neighbor in graph[vertex]:
            if not visited[ord(neighbor)-ord('A')]:
                dfs_util2(neighbor)

        connected_component.append(vertex)

    while topsort_stack:

        cur_vertex = topsort_stack.pop()
        connected_component = []

        if not visited[ord(cur_vertex)-ord('A')]:
            dfs_util2(cur_vertex)
            strongly_connected_components.append(connected_component)

    return strongly_connected_components


    


if __name__ == "__main__":

    graph = OrderedDict({
        'A' : [],
        'B' : ['A' , 'E'],
        'C' : ['B' , 'F'],
        'D' : ['B'],
        'E' : ['B'],
        'F' : ['C' , 'E'],
        'G' : ['E' , 'I'],
        'H' : ['F' , 'G'],
        'I' : ['J'],
        'J' : ['G' , 'L'],
        'K' : ['H'],
        'L' : ['K']
    })

    strongly_connected_components = scc_Kosaraju(graph)

    for component in strongly_connected_components:
        print(component)

    
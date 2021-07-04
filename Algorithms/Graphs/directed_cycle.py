

def is_cycle_dfs(graph):
    # Graph is in adjacent list form
    # Vertices are capital English alphabets in sequence from A
    # Returns True if there is cycle, False otherwise

    num_vertices = len(graph)
    
    visited = [False] * num_vertices # ignore already visited nodes
    exploring = [False] * num_vertices # check for cycle
    
    
    def dfs_util(vertex):

        visited[ord(vertex)-ord('A')] = True 
        exploring[ord(vertex)-ord('A')] = True

        for neighbor in graph[vertex]:
            if not visited[ord(neighbor)-ord('A')]:
                if dfs_util(neighbor):
                    return True 
            else:
                # either post visited or currently exploring (i.e. in recursion stack -- back edge)
                # bc it's a directed graph, even the neighbor is a parent, it's a cycle
                if exploring[ord(neighbor)-ord('A')]:
                    return True
                # not a cycel if the neighbor is already post visited
        
        exploring[ord(vertex)-ord('A')] = False  # done exploring -- post visited         
        return False 
        
    for vertex in graph:  # disconnected graphs
        if not visited[ord(vertex)-ord('A')]:
            if dfs_util(vertex):
                return True 
    
    return False


def is_cycle_coloring(graph):
    # Graph is in adjacent list form
    # Vertices are capital English alphabets in sequence from A
    # Returns True if there is cycle, False otherwise

    num_vertices = len(graph)
    
    visited = [False] * num_vertices # ignore already visited nodes
    '''
    WHITE : Vertex is not processed yet. Initially, all vertices are WHITE.
    GRAY: Vertex is being processed 
        (DFS for this vertex has started, but not finished which means that 
        all descendants (in DFS tree) of this vertex are not processed yet 
        (or this vertex is in the function call stack)
    BLACK : Vertex and all its descendants are processed. 
    '''
    colors = ['WHITE'] * num_vertices # check for cycle
    
    
    def dfs_util(vertex):

        visited[ord(vertex)-ord('A')] = True 
        colors[ord(vertex)-ord('A')] = "GREY"

        for neighbor in graph[vertex]:
            if not visited[ord(neighbor)-ord('A')]:
                if dfs_util(neighbor):
                    return True 
            else:
                # either post visited or currently exploring (i.e. in recursion stack -- back edge)
                # bc it's a directed graph, even the neighbor is a parent, it's a cycle
                if colors[ord(neighbor)-ord('A')] == "GREY":
                    return True
                # not a cycel if the neighbor is already post visited
        
        colors[ord(vertex)-ord('A')] = "BLACK"  # done exploring -- post visited         
        return False 

    
    for vertex in graph:  # disconnected graphs
        if not visited[ord(vertex)-ord('A')]:
            if dfs_util(vertex):
                return True 
    
    return False



            
if __name__ == '__main__':
    graph1 = {
        'A' : ['B' , 'C'],
        'B' : ['C'],
        'C' : ['A' , 'D'],
        'D' : ['D']
    } 

    print(is_cycle_dfs(graph1))

    graph2 = {
        'A' : ['B' , 'C'],
        'B' : [ 'C'],
        'C' : ['D'],
        'D' : []
    } 

    print(is_cycle_dfs(graph2))


    print(is_cycle_coloring(graph1))
    print(is_cycle_coloring(graph2))
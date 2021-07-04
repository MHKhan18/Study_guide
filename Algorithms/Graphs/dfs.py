

def dfs(graph):
    # Graph is in adjacent list form
    
    visited = set() # check for cycle
    
    def dfs_util(vertex):

        visited.add(vertex)

        # previsit 

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs_util(neighbor) # tree edge
            
            # else: backedge

        # post visit

    for vertex in graph:  # disconnected graphs
        if vertex not in visited:
            dfs_util(vertex)





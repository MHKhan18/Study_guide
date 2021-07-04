

def is_cycle_dfs(graph):
    # Graph is in adjacent list form
    # Vertices are capital English alphabets in sequence from A
    # Returns True if there is cycle, False otherwise

    num_vertices = len(graph)
    
    visited = [False] * num_vertices # check for cycle
    
    
    def dfs_util(vertex , parent):

        visited[ord(vertex)-ord('A')] = True 
        
        for neighbor in graph[vertex]:
            if not visited[ord(neighbor)-ord('A')]:
                if dfs_util(neighbor , vertex):
                    return True 
            elif neighbor != parent:
                return True
        
        return False 

    
    for vertex in graph:  # disconnected graphs
        if not visited[ord(vertex)-ord('A')]:
            if dfs_util(vertex , None):
                return True 
    
    return False
            
if __name__ == '__main__':
    graph1 = {
        'A' : ['B' , 'C'],
        'B' : ['A' , 'C'],
        'C' : ['A' , 'B' , 'D'],
        'D' : ['C']
    } 

    print(is_cycle_dfs(graph1))

    graph2 = {
        'A' : ['B'],
        'B' : ['A' , 'C'],
        'C' : ['B' , 'D'],
        'D' : ['C']
    } 

    print(is_cycle_dfs(graph2))
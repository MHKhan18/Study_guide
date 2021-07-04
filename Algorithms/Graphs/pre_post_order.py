from collections import OrderedDict
  

def get_pre_post_order(graph):
    # Graph is in adjacent list form
    # Vertices are contiguous sequence of capital English alphabets starting from A 

    num_vertices = len(graph)
    
    visited = [False] * num_vertices # check for cycle
    
    previsit_orders = [-1] * num_vertices
    postvisit_orders = [-1] * num_vertices

    counter = 1
    
    
    def dfs_util(vertex):

        visited[ord(vertex)-ord('A')] = True 
        
        nonlocal counter
        previsit_orders[ord(vertex) - ord('A')] = counter
        counter += 1

        for neighbor in graph[vertex]:  # sorting is non-essential
            if not visited[ord(neighbor)-ord('A')]:
                dfs_util(neighbor)

        postvisit_orders[ord(vertex) - ord('A')] = counter
        counter += 1

    
    for vertex in graph:  # disconnected graphs
        if not visited[ord(vertex)-ord('A')]:
            dfs_util(vertex)

    ordered_vertices = [chr(ord('A') + i) for i in range(num_vertices)]
    print(ordered_vertices)
    print(previsit_orders)
    print(postvisit_orders)

    return (previsit_orders , postvisit_orders)
        

    


if __name__ == '__main__':
    graph = OrderedDict({
        'A' : ['B' , 'E'],
        'B' : ['A'],
        'E' : ['A' , 'J' , 'I'],
        'F' : [],
        'I' : ['E' , 'J'],
        'J' : ['E' , 'I'],
        'C' : ['D' , 'G' , 'H'],
        'D' : ['C' , 'H'],
        'G' : ['C' , 'H' , 'K'],
        'H' : ['D' , 'C' , 'G' , 'K' , 'L'],
        'K' : ['G' , 'H'],
        'L' : ['H']
    })

    # sorting and ordered dict to break ties in alphabetic order

    graph = OrderedDict(sorted(graph.items()))

    for node in graph:
        graph[node] = sorted(graph[node])

    get_pre_post_order(graph)

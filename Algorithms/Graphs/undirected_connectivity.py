
def get_connected_components(graph):
    # Graph is in adjacent list form
    # Vertices are capital English alphabets in sequence from A

    num_vertices = len(graph)
    
    visited = [False] * num_vertices # check for cycle
    connected_component_num = [-1] * num_vertices
    
    def dfs_util(vertex , component_num):

        visited[ord(vertex)-ord('A')] = True 
        connected_component_num[ord(vertex)-ord('A')] = component_num

        for neighbor in graph[vertex]:
            if not visited[ord(neighbor)-ord('A')]:
                dfs_util(neighbor , component_num)

    component_num = 0
    for vertex in graph:  # disconnected graphs
        if not visited[ord(vertex)-ord('A')]:
            dfs_util(vertex , component_num)
            component_num += 1

    compnum_vertices = {}
    for index , component_no in enumerate(connected_component_num):
        if component_no in compnum_vertices:
            compnum_vertices[component_no].append(chr(ord('A') + index))
        else:
            compnum_vertices[component_no] = [chr(ord('A') + index)]

    for connected_component in compnum_vertices.values():
        print(connected_component)

    return compnum_vertices


if __name__ == '__main__':
    graph = {
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
    } 
    get_connected_components(graph)

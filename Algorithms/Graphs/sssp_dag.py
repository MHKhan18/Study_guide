from collections import OrderedDict
from collections import deque


def dag_shortest_path(graph , start):

    '''
        Running Time: O(V + E)
    '''

    num_vertices = len(graph)

    dist = [float('inf')] * num_vertices  
    dist[index(start)] = 0

    topological_order = topological_Kahn(graph)

    for node in topological_order:
        for neighbor in graph[node]:
            to , edge = neighbor
            dist[index(to)] = min(dist[index(to)] , dist[index(node)] + edge)

    return dist


def index(vertex):
    return ord(vertex) - ord('A')


def topological_Kahn(graph):
    
    num_vertices = len(graph)
    
    sorted_lst = []
    in_degree = [0] * num_vertices

    for node in graph:
        for neighbor in graph[node]:
            to , edge = neighbor
            in_degree[index(to)] += 1

    queue = deque()  # contains vertices with zero in-degree currently
    
    for node in graph:
        if in_degree[index(node)] == 0:
            queue.append(node)
    
    while queue:

        cur_node = queue.popleft()
        sorted_lst.append(cur_node)

        # reduce in-degree of cur_node's children
        for neighbor in graph[cur_node]:

            to , edge = neighbor
            in_degree[index(to)] -= 1

            if in_degree[index(to)] == 0:
                queue.append(to)

    if len(sorted_lst) != num_vertices:
        raise AssertionError('Input is not a DAG')

    return sorted_lst


if __name__ == "__main__":
    graph  = OrderedDict({
        'A' : [('B' , 5) , ('C' , 3) ],
        'B' : [('C' , 2) , ('D' , 6)],
        'C' : [('D' , 7) , ('E' , 4) , ('F' , 2)],
        'D' : [('F' , 1) , ('E' , -1)],
        'E' : [('F' , -2)],
        'F' : []
    })

    dist = dag_shortest_path(graph , 'B')
    print(dist)
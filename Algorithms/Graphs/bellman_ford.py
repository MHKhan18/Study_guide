
from collections import OrderedDict

def index(vertex):
    return ord(vertex) - ord('A')

def bellman_ford(graph , start):
    '''
    Finds shortest path from start to every other node,
    in the presence of negative edges.
    Dynamic Programming.
    Runnimg Time : O(V * E)
    Marks edges in a negative cycle and reachable from a negtive cycle with -inf
    '''
    
    num_vertices = len(graph)

    dist = [float('inf')] * num_vertices
    dist[index(start)] = 0

    for _ in range(num_vertices - 1):
        for node in graph:
            for neighbor in graph[node]:
                to , edge = neighbor
                dist[index(to)] = min(dist[index(to)] , dist[index(node)] + edge)

    # Run algorithm a second time to detect which nodes are part
    # of a negative cycle. A negative cycle has occurred if we
    # can find a better path beyond the optimal solution.
    for _ in range(num_vertices - 1):
        for node in graph:
            for neighbor in graph[node]:
                to , edge = neighbor

                if dist[index(node)] + edge < dist[index(to)]:
                    # Assert: vertex 'to' is either part of a negative cycle or 
                    # reachable from a negative cycle 
                    dist[index(to)] =  float('-inf')
    return dist


if __name__ == "__main__":

    graph = OrderedDict({
        'A' : [('E' , 2)],
        'B' : [('A' , 1) , ('C' , 1)],
        'C' : [('D' , 3)],
        'D' : [('E' , -1)],
        'E' : [('B' , -2)],
        'F' : [('A' , -4) , ('E' , -1)],
        'G' : [('F' , 1)],
        'H' : [('A' , 10) , ('G' , 8)]
    })

    dist = bellman_ford(graph , 'H')
    print(dist)



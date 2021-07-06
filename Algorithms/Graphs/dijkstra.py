from collections import OrderedDict

from priority_queue_min import PriorityQueue

def index(vertex):
    return ord(vertex) - ord('A')

def dijkstra(graph , start):
    # Graph is in adjacent list form
    # Vertices are contiguous capital English alphabets starting from A

    # works for both directed and unidrected and cyclic and acyclic graphs
    # just not for negative edge wights

    # Running time:

    # V is num_vertices and E is num_edges
    # (V * deletemin) + (V + E) * insert
    # with binary heap: O((V + E) * log(V))

    num_vertices = len(graph)

    dist = [float('inf')] * num_vertices  # stores distance from start to every other node in graph
    prev = [None] * num_vertices # stores the previous vetex in the shortest path to vertex i

    dist[index(start)] = 0

    priority_queue = PriorityQueue()

    for node in graph:
        priority_queue.insert((node , dist[index(node)]))
    
    while priority_queue.get_size() > 0:

        closest_vertex , closest_distance = priority_queue.delete_min()  # shortest distance to closest_vertex can't be improved further

        for neighbor in graph[closest_vertex]:

            neighbor_vertex , neighbor_edge = neighbor

            new_distance = dist[index(closest_vertex)] + neighbor_edge

            if dist[index(neighbor_vertex)] > new_distance:

                prev_neighbor_dist = dist[index(neighbor_vertex)]
                
                dist[index(neighbor_vertex)] = new_distance
                prev[index(neighbor_vertex)] = closest_vertex
                
                priority_queue.decrease_key( (neighbor_vertex , prev_neighbor_dist) , (neighbor_vertex , new_distance))

    return (dist , prev)



def find_shortest_path(graph , start, end):

    dist , prev = dijkstra(graph , start)

    path = [end]
    cur = end
    while not prev[index(cur)] is None:
        path.append(prev[index(cur)])
        cur = prev[index(cur)]
    
    path.reverse()

    print(f'Shortest path from {start} to {end} is:')
    print(path)

    print(f'Total Cost: {dist[index(end)]}')

    return path





    

if __name__ == "__main__":
    
    graph = OrderedDict({
        'A' : [('B',4) , ('C',2)],
        'B' : [('C',3) , ('D',2) , ('E',3)],
        'C' : [('B',1) , ('D',4) , ('E',5)],
        'D' : [],
        'E' : [('D',1)]
    })

    (dist , prev) = dijkstra(graph , 'A')
    print(dist)
    print(prev)

    find_shortest_path(graph , 'A', 'E')
from collections import deque
from collections import OrderedDict

def index(vertex):
    return ord(vertex) - ord('A')


def bfs(graph , start_node):
    # Graph is in adjacent list form
    # Vertices are contiguous capital English alphabets starting from A

    num_nodes = len(graph)
    distances = [float('inf')] * num_nodes
    queue = deque()

    distances[index(start_node)] = 0
    queue.append(start_node)

    while queue:

        cur_node = queue.popleft()

        for neighbor in graph[cur_node]:

            if distances[index(neighbor)] == float('inf'):
                queue.append(neighbor)
                distances[index(neighbor)] = distances[index(cur_node)] + 1
            
            # else cycle found in an undirected graph 
                # if neighbor is not the parent of cur_node 
                # keep track of parents in an array to check this


    return distances


if __name__ == "__main__":

    graph = OrderedDict({
        'A' : ['F' , 'B'],
        'B' : ['A' , 'C'],
        'C' : ['B' , 'F'],
        'D' : ['E' , 'F'],
        'E' : ['D' , 'F'],
        'F' : ['A' , 'C' , 'D' , 'E']
    })

    distances = bfs(graph , 'F')
    print(distances)



from queue import PriorityQueue


class MST_LAZY_PRIM:
    def __init__(self, graph, start_node=0) -> None:

        self.graph = graph
        self.n = len(graph)
        self.start_node = start_node
        self.visited = [False] * self.n
        self.pq = PriorityQueue()  # min pq

    def add_edges(self, cur_node):

        self.visited[cur_node] = True

        for to in self.graph[cur_node]:
            to_node, cost = to
            if not self.visited[to_node]:  # causes a cycle
                self.pq.put((cost, (cur_node, to_node)))

    def solve(self):

        m = self.n - 1  # num edges in mst
        mst_cost = 0
        mst_edges = []

        self.add_edges(self.start_node)

        while self.pq.qsize() > 0 and len(mst_edges) < m:

            next_item = self.pq.get()
            cost, (from_node, to_node) = next_item

            # stale edge -- would cause cycle
            # the to_node got visited from parent other than from_node by an earlier parent, thus less cost
            if self.visited[to_node]:
                continue

            mst_edges.append((from_node, to_node))
            mst_cost += cost

            self.add_edges(to_node)

        if len(mst_edges) != m:
            return (None, None)

        return (mst_cost, mst_edges)


"""
The eager version simply uses indexed priority queue instead of simple priority queue
Instead of inserting deplicate entries in pq of same edge, we use decreaseKey (update) operation on the ipq
decreaseKey runs in log(E) time in ipq
but for simple pq, removal times is linear
"""


if __name__ == "__main__":

    graph = {
        0: [(1, 10), (2, 1), (3, 4)],
        1: [(0, 10), (2, 3), (4, 0)],
        2: [(0, 1), (1, 3), (5, 8), (3, 2)],
        3: [(0, 4), (2, 2), (5, 2), (6, 7)],
        4: [(1, 0), (5, 1), (7, 8)],
        5: [(2, 8), (4, 1), (7, 9), (6, 6), (3, 2)],
        6: [(3, 7), (5, 6), (7, 12)],
        7: [(6, 12), (5, 9), (4, 8)],
    }

    lazy_prim = MST_LAZY_PRIM(graph)
    mst_cost, mst_edges = lazy_prim.solve()
    print(f"LAZY PRIM RUN \n MST COST: {mst_cost}, edges in MST: {mst_edges}")

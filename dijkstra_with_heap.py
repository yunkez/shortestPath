
from min_heap import MinHeap

#uses array implementation
def dijkstra(G, s):
    d = {}
    nodes = []           # node with distances from source
    predecessor = {}     # node predecessor on the shortest path

    #initing distances to INF for all but source.
    for v in G:
        if v == s:
            nodes.append((0, s))
            d[s] = 0
        else:
            nodes.append((float("inf"), v))
            d[v] = float("inf")

    predecessor[s] = None

    Q = MinHeap(nodes)   # contains all nodes to find shortest paths to, intially everything.
    while(Q.arr):                        # until there is nothing left in Q
        u = Q.delete_min()[1]            # get min distance node
        for v in G[u]:                   # relax all outgoing edges from it
            relax(u, v, d, predecessor, Q)

    print(d)
    print_paths(predecessor)


def relax(u, v, d, predecessor, Q):
    weight = v[1]
    v = v[0]
    if d[v] > d[u] + weight:
        old_d = d[v]
        d[v] = d[u] + weight
        Q.decrease_key((old_d,v),(d[v],v))
        predecessor[v] = u

def print_paths(predecessor):
    paths = {}
    for v in predecessor:
        paths[v] = ""
        p = predecessor[v]
        while p is not None:
            paths[v] += "<-"+p
            p = predecessor[p]
    for v, path in paths.items():
        print(v+":"+path)

G = {
"a": [("b", 10), ("c", 3)],
"b": [("c",  1), ("d", 2)],
"c": [("b",  4), ("d", 8), ("e", 2)],
"d": [("e",  7)],
"e": [("d",  9)]
}

dijkstra(G, "a")
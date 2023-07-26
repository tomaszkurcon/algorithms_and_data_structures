from queue import PriorityQueue
from math import inf

def relax(u,v, l, d, parent, queue):
    if d[v] > d[u]+l:
        d[v]=d[u]+l
        parent[v]=u
        queue.put((d[v], v))
def Dijkstra(G, s):
    n=len(G)
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0
    queue = PriorityQueue()
    queue.put((d[s],  s))
    while not queue.empty():
        du, u = queue.get()
        if d[u] == du:
            for v, l in G[u]:
                relax(u, v, l, d, parent, queue)
    return d, parent


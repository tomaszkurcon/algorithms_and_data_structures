
from math import inf
def relax(u,v, l, d, parent):
    if d[v] > d[u]+l:
        d[v]=d[u]+l
        parent[v]=u

def Bellman_ford(G, s):
    n=len(G)
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0
    for i in range(n-1):
        for u in range(n):
            for v, w in G[u]:
                relax(i, v, w, d, parent)
    for i in range(n):
        print("vertex: ", i, " cost: ", d[i])
        for v, w in G[i]:
            if d[v] > d[i] + w:
                print("negative cycle !", "vertex i: ", i, "vertex v: ", v, d[i], d[v], w)



Bellman_ford([[(1, 3)], [(2, -4)], [(4, -3)], [(2, 2), (0, -3)], [(3, 5), (5, 1)], []], 0)
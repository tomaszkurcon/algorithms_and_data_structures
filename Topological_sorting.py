from collections import deque

def DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    time_tab = [-1 for _ in range(n)]
    time = 0
    Q=deque()
    def DFSVisit(G, s):
        nonlocal time
        visited[s]=True
        for v in G[s]:
            if not visited[v]:
                parent[v]=s
                DFSVisit(G, v)
        time+=1
        time_tab[s]=time
        Q.appendleft(s)

    for u in G:
        if not u.visited:
            DFSVisit(G, u)
    return Q


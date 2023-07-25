from collections import deque

def BFS(G, s):
    n = len(G)
    q = deque()
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    d = [-1 for _ in range(n)]
    q.appendleft(s)
    visited[s] = True
    d[s] = 0
    while len(q)!=0:
        u = q.pop()
        for v in G[u]:
            if not v[visited]:
                visited[v]=True
                parent[v] = u
                q.appendleft(v)
                d[v]=d[u]+1


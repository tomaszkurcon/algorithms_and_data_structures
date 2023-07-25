def DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    time_tab = [-1 for _ in range(n)]
    time = 0
    def DFSVisit(G, s):
        nonlocal time
        time+=1 #entry time
        visited[s]=True
        for v in G[s]:
            if not visited[v]:
                parent[v]=s
                DFSVisit(G, v)
        time+=1  #processing time
        time_tab[s]=time

    for u in G:
        if not visited[u]:
            DFSVisit(G, u)



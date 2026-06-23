def create_adjacency_list(edges):
    adj_list = {}
    for edge in edges:
        u, v = edge
        if not adj_list.get(u):
            adj_list[u]=[v]
        else:
            adj_list[u].append(v)
        if not adj_list.get(v):
            adj_list[v]=[u]
        else:
            adj_list[v].append(u)
    return adj_list
edges = [(1,2),(0,3),(4,5),(3,6)]

print(create_adjacency_list(edges))
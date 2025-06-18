graph = {}
def create_edge(source , destination):
    if source not in graph:
        graph[source] = []
    graph[source].append(destination)
    if destination not in graph:
        graph[destination] = []
    graph[destination].append(source)
def dfs(node , visited):
    visited.append(node)
    print(node)
    for nbr in graph[node]:
        if nbr not in visited: 
            dfs(nbr , visited)
create_edge("A" , "B")
create_edge("A" , "C")
create_edge("A" , "Y") 
create_edge("B" , "D") 
create_edge("C" , "E") 
create_edge("D" , "E") 
create_edge("D" , "F")
create_edge("E" , "F") 
create_edge("F" , "G")
dfs("A" , [])
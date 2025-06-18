graph = {}
def create_edge(source , destination):
    if source not in graph:
        graph[source] = []
    graph[source].append(destination)
    if destination not in graph:
        graph[destination] = []
    graph[destination].append(source)
create_edge(1 , 2)
create_edge(1 , 3)
create_edge(2  , 4) 
create_edge(3 , 5) 
create_edge(4 , 5) 
create_edge(4 , 6) 
create_edge(5 , 6)
create_edge(6 , 7) 
print(graph)
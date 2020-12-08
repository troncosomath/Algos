def count_Components(n, edges):
    # Keep track of parent of each node
    # Initialize as each node it is each own parent
    ids = [i for i in range(n)]
    
    for edge in edges:
        union(edge[0], edge[1], ids)
    
    set_representatives = set()
    for i in range(n):
        # Add parent of node i
        set_representatives.add(find(i, ids))

    return len(set_representatives)

def union(edge1, edge2, ids):
    '''
    Merge edge1 and edge2
    '''
    parent1 = find(edge1, ids)
    parent2 = find(edge2, ids)
    ids[parent1] = parent2

def find(edge, ids):
    # This check is crucial to avoid cycles
    # We need to check and redefine 
    # chains to the corresponding parent
    if ids[edge] != edge:
        ids[edge] = find(ids[edge], ids)
    return ids[edge]

def test(n=5, edges=[[0,1], [1,2], [2,0], [3,4]]):
    print(count_Components(n, edges))

test()

    






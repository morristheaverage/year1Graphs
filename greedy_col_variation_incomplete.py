import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_next_vertex(G):

    if G.node[1]['visited'] == 'no':
        return 1

    visited = set()
    adjacent = set()
    
    for i in G.nodes():
        if G.node[i]['visited'] == 'yes':
            visited.add(i)
            adjacent.update(G.neighbors(i)) #add code to find lowest value of adjacent (convert to list first?)

    return min(adjacent - visited)








def find_smallest_color(G,i):
    global kmax
    n = len(G.nodes())
    
    neighbourCols = [0 for i in range(n)]   #0 if the colour of that index is not in the node's neighbours. Else 1

    for n in G.neighbors(i):
        col = G.node[n]['color']
        if col > 0:
            neighbourCols[col - 1] = 1

    for j in range(len(neighbourCols)):
        if neighbourCols[j] == 0:
            if j + 1 > kmax:
                kmax = j + 1
                
            return j + 1

    return n + 1 #this line should never run and if it does that is a bug










def greedy(G):
    n = len(G.nodes())
    global kmax
    global visited_counter
    
    kmax = 1
    visited_counter = 0

    G.add_nodes_from(G.nodes(), color = -1)
    
    while visited_counter < n:
        i = find_next_vertex(G)
        G.node[i]['visited'] = 'yes'
        G.node[i]['color'] = find_smallest_color(G, i)
        visited_counter += 1



    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)
    print()



print('Graph G1:')
G=graph1.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G2:')
G=graph2.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G3:')
G=graph3.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G4:')
G=graph4.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)


print('Graph G5:')
G=graph5.Graph()
G.add_nodes_from(G.nodes(), visited = 'no')
greedy(G)

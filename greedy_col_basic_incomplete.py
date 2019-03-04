import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


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
    global kmax

    kmax = 1

    for i in G.nodes():
        G.node[i]['color'] = -1 #uncoloured

    for i in G.nodes():
        col = find_smallest_color(G, i)
        G.node[i]['color'] = col

    print()
    for i in G.nodes():
        print('vertex', i, ': color', G.node[i]['color'])
    print()
    print('The number of colors that Greedy computed is:', kmax)


print('Graph G1:')
G=graph1.Graph()
greedy(G)


print('Graph G2:')
G=graph2.Graph()
greedy(G)


print('Graph G3:')
G=graph3.Graph()
greedy(G)


print('Graph G4:')
G=graph4.Graph()
greedy(G)


print('Graph G5:')
G=graph5.Graph()
greedy(G)

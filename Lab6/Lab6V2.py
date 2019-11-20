'''
Ismael Villalobos
11-17-19
Lab Assignment 6
Professor Fuentes
TA-Dita Nath
Purpose:
'''
import graph_AL as graphAL
import graph_AM as graphAM
import graph_EL as graphEL

# build three graph representation:
# - adjacency list
# - adjacency matrix
# - edge list
def buildGraphRepresentations():
    # vars
    v = 16
    weighted = False
    directed = False
    
    # build adjacency list
    AL = graphAL.Graph(v, weighted, directed)
    AL.insert_edge(0, 5)
    AL.insert_edge(2, 11)
    AL.insert_edge(2, 7)
    AL.insert_edge(4, 5)
    AL.insert_edge(4, 7)
    AL.insert_edge(4, 13)
    AL.insert_edge(8, 11)
    AL.insert_edge(8, 13)
    AL.insert_edge(10, 11)
    AL.insert_edge(10, 15)
    
    # build adjacency matrix, build edge list
    AM = AL.as_AM()
    EL = AL.as_EL()
    
    # return all three representations
    return AL, AM, EL

# for lab report
def graphs(AL, AM, EL):
    AL.draw()
    AM.draw()
    EL.draw()
    
if __name__ == "__main__":
    
    AL, AM, EL = buildGraphRepresentations()
    
    # adjacency list
    # depth first
    print("Adjancency List Depth First:")
    print(AL.DFS(0, 15))
    AL.printDFS(0, 15)
    # breadth first
    print("Adjacency List Breadth First:")
    print(AL.BFS(0, 15))
    AL.printBFS(0, 15)
    
    print()
    print()
    
    # adjancency matrix
    # depth first
    print("Adjancency Matrix Depth First:")
    print(AM.DFS(0, 15))
    AM.printDFS(0, 15)
    # breadth first
    print("Adjacency Matrix Breadth First:")
    print(AM.BFS(0, 15))
    AM.printBFS(0, 15)
    
    print()
    print()
    
    # edge list
    # depth first
    print("Edge List Depth First:")
    print(EL.DFS(0, 15))
    EL.printDFS(0, 15)
    # breadth first
    print("Edge List Breadth First:")
    print(EL.BFS(0, 15))
    EL.printBFS(0, 15)
    
    print()
    print()
    
    # for lab report
    graphs(AL, AM, EL)
import networkx as nx
import matplotlib.pyplot as mp


def Graph1():
    G = nx.Graph()  #creates empty graph
    nodes=[1,2,3,4,5,6,7]  #list of nodes
    G.add_nodes_from(nodes)  #add nodes to graph
    G.add_weighted_edges_from([(1,2,4),(1,3,9),(1,4,1),(2,5,12),(2,6,14),(3,7,13),(4,7,7),(5,1,9),(6,7,10),(3,6,20),(7,2,16)])  #add weighted edges to nodes
    V=7  #vertices stored

    pos= nx.circular_layout(G)  #arrange the nodes in a circular layout
    nx.draw_networkx_nodes(G,pos)  #nodes added to graph
    nx.draw_networkx_edges(G, pos)  #edges added to the graph
    labels=nx.get_edge_attributes(G, "weight")  #edge weights as labels
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)  #display weights on the graph
    nx.draw_networkx_labels(G, pos)  #label the nodes with their IDs
    mp.show()

    edges = [(u,v,data["weight"]) for u,v,data in G.edges(data=True)]  #create a list of edges with their weights

    def weight_edge(edge):  #function to get the weight of an edge
        return edge[2]  #return the third value from the edge tuple

    def kruskal(V, edges):
        parent = list(range(V+1))  #make a list to keep track of parent nodes

        def find(i):  # function to find the highest parent (root) of a node
            while i != parent[i]:  #keep going until we find the node that is its own parent
                parent[i] = parent[parent[i]]  # make the node point higher up
                i = parent[i]  # move one level up the tree
            return i  # return the root parent node


        def union(a, b):  #function to connect two sets together
            parent[find(a)] = find(b)  #connect group of a to b

        edges_sorted = sorted(edges, key=weight_edge)  # sort all edges by their weight (smallest first)
        mst = []  #empty list
        cost = 0  #set the total MST cost to 0

        for u, v, w in edges_sorted:  #go through all edges in order
            if find(u) != find(v):  #checks if adding the edge makes a loop
                union(u, v)  #if not, connect the two sets
                mst.append((u, v, w))  #add this edge to the MST
                cost += w  #add the weight of the edge to the total cost

        return mst, cost  # return the final MST and its total cost

    mst, cost = kruskal(7, edges)  # run Kruskal’s algorithm and get results

    print("MST edges:")
    for u, v, w in mst:  #go through each edge in the MST
        print(u, v, w)  #print the two nodes and their weight
    print("Total MST Cost =", cost)  #show the total cost of the MST

def Graph2():
    G = nx.Graph()  #creates empty graph
    nodes=[1,2,3,4,5]  #list of nodes
    G.add_nodes_from(nodes)  #add nodes to graph
    G.add_weighted_edges_from([(1,2,2),(1,3,1),(1,4,8),(2,5,10),(3,2,14),(5,1,9),(4,2,6),(5,3,10)])  #add weighted edges to nodes
    V=5  #vertices stored

    pos= nx.circular_layout(G)  #arrange the nodes in a circular layout
    nx.draw_networkx_nodes(G,pos)  #nodes added to graph
    nx.draw_networkx_edges(G, pos)  #edges added to the graph
    labels=nx.get_edge_attributes(G, "weight")  #edge weights as labels
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)  #display weights on the graph
    nx.draw_networkx_labels(G, pos)  #label the nodes with their IDs
    mp.show()

    edges = [(u,v,data["weight"]) for u,v,data in G.edges(data=True)]  #create a list of edges with their weights

    def weight_edge(edge):  #function to get the weight of an edge
        return edge[2]  #return the third value from the edge tuple

    def kruskal(V, edges):
        parent = list(range(V+1))  #make a list to keep track of parent nodes

        def find(i):  # function to find the highest parent (root) of a node
            while i != parent[i]:  #keep going until we find the node that is its own parent
                parent[i] = parent[parent[i]]  # make the node point higher up
                i = parent[i]  # move one level up the tree
            return i  # return the root parent node


        def union(a, b):  #function to connect two sets together
            parent[find(a)] = find(b)  #connect group of a to b

        edges_sorted = sorted(edges, key=weight_edge)  # sort all edges by their weight (smallest first)
        mst = []  #empty list
        cost = 0  #set the total MST cost to 0

        for u, v, w in edges_sorted:  #go through all edges in order
            if find(u) != find(v):  #checks if adding the edge makes a loop
                union(u, v)  #if not, connect the two sets
                mst.append((u, v, w))  #add this edge to the MST
                cost += w  #add the weight of the edge to the total cost

        return mst, cost  # return the final MST and its total cost

    mst, cost = kruskal(5, edges)  # run Kruskal’s algorithm and get results

    print("MST edges:")
    for u, v, w in mst:  #go through each edge in the MST
        print(u, v, w)  #print the two nodes and their weight
    print("Total MST Cost =", cost)  #show the total cost of the MST

def Graph3():
    G = nx.Graph()  #creates empty graph
    nodes=[1,2,3,4,5]  #list of nodes
    G.add_nodes_from(nodes)  #add nodes to graph
    G.add_weighted_edges_from([(1,2,10),(1,3,5),(1,4,3),(2,5,20),(3,2,4),(5,1,19),(4,2,16),(5,3,1)])  #add weighted edges to nodes
    V=5  #vertices stored

    pos= nx.circular_layout(G)  #arrange the nodes in a circular layout
    nx.draw_networkx_nodes(G,pos)  #nodes added to graph
    nx.draw_networkx_edges(G, pos)  #edges added to the graph
    labels=nx.get_edge_attributes(G, "weight")  #edge weights as labels
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)  #display weights on the graph
    nx.draw_networkx_labels(G, pos)  #label the nodes with their IDs
    mp.show()

    edges = [(u,v,data["weight"]) for u,v,data in G.edges(data=True)]  #create a list of edges with their weights

    def weight_edge(edge):  #function to get the weight of an edge
        return edge[2]  #return the third value from the edge tuple

    def kruskal(V, edges):
        parent = list(range(V+1))  #make a list to keep track of parent nodes

        def find(i):  # function to find the highest parent (root) of a node
            while i != parent[i]:  #keep going until we find the node that is its own parent
                parent[i] = parent[parent[i]]  # make the node point higher up
                i = parent[i]  # move one level up the tree
            return i  # return the root parent node


        def union(a, b):  #function to connect two sets together
            parent[find(a)] = find(b)  #connect group of a to b

        edges_sorted = sorted(edges, key=weight_edge)  # sort all edges by their weight (smallest first)
        mst = []  #empty list
        cost = 0  #set the total MST cost to 0

        for u, v, w in edges_sorted:  #go through all edges in order
            if find(u) != find(v):  #checks if adding the edge makes a loop
                union(u, v)  #if not, connect the two sets
                mst.append((u, v, w))  #add this edge to the MST
                cost += w  #add the weight of the edge to the total cost

        return mst, cost  # return the final MST and its total cost

    mst, cost = kruskal(5, edges)  # run Kruskal’s algorithm and get results

    print("MST edges:")
    for u, v, w in mst:  #go through each edge in the MST
        print(u, v, w)  #print the two nodes and their weight
    print("Total MST Cost =", cost)  #show the total cost of the MST


Graph1()
Graph2()
Graph3()


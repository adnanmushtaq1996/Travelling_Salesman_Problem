# Import Dependencies
from sys import maxsize 
from itertools import permutations
import sys
import networkx as nx
import matplotlib.pyplot as plt
 
# Function for of traveling Salesman Problem 
def calroute(graph, s): 
  
    V = len(graph)
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 
 
    min_path = maxsize 
    next_permutation=permutations(vertex)

    for i in next_permutation:
 
        # store current Path weight(cost) 
        current_pathweight = 0
 
        # compute current path weight 
        k = s 
        for j in i: 
            current_pathweight += graph[k][j] 
            k = j 
        current_pathweight += graph[k][s] 
 
        # update minimum 
        min_path = min(min_path, current_pathweight) 
        route = i
     
    return min_path ,route


def add_node(graph):
    length_of_graph = len(graph[0])
    print("Enter Distance from Next node ", length_of_graph + 1,  " required distances")
    lst = [] 
    n = length_of_graph
    
    for i in range(0, n): 
        ele = int(input()) 
        lst.append(ele) # adding the element 

    for i in range(len(lst)):
        graph[i].append(lst[i])
    
    lst.insert(0,0)
    graph.append(lst)

    return(graph)


def delete_node(graph):
    node= int(input("Enter which node you want to delete 1, 2, 3 ... etc: "))
    length_of_graph = len(graph[0])
    if node > length_of_graph :
        print("Node does not exist")
        return -1
    
    new_graph = []
    for i in range(len(graph)):
        if i != node:
            new_graph.append(graph[i])

    return(new_graph)


def plot_nodes(graph):

    G=nx.Graph()
    nodes = []

    for i in range(1,len(graph)+1):
        nodes.append(i)
    G.add_nodes_from(nodes)

    edges = [(nodes[i],nodes[j]) for i in range(len(nodes)) for j in range(i+1, len(nodes))]
    # adding a list of edges:
    G.add_edges_from(edges)

    nx.draw(G,with_labels=True, font_weight='bold')
    plt.show() # display
    return
    

def main():
    graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]] 
    plot_nodes(graph)

    s = 0
    print("\n", "*"*50)
    print("Current Graph is  : ", graph)
    length_of_graph = len(graph[0])
    print("Current Graph has ", length_of_graph, " number of nodes")
    min_path, route = calroute(graph, s)
    print("Min Path Distance is : " , min_path)
    print("Route for Min Path Distance is : " , route)
    print("\n", "*"*50)

    print("*"*25, "Menu","*"*25 )
    print("1. Add More Nodes  : 'a'")
    print("2. Delete Some Nodes : 'd'")
    print("3. Exit or Do nothing : 'e'")
    print("*"*25)

    user_input = input("Enter your choice : ")

    while user_input :

        if user_input == "a":
            print("\n", "*"*50)
            print("You selected to add 1 more node")
            new_graph = add_node(graph)
            length_of_graph = len(new_graph[0])
            print("Current Graph has ", length_of_graph, " number of nodes")
            print("New Graphs is : ", new_graph)
            min_path, route = calroute(new_graph, s)
            print("Min Path Distance is : " , min_path)
            print("Route for Min Path Distance is : " , route)
            plot_nodes(graph)
            print("\n", "*"*50)
            user_input = input("Enter your choice : ")

        elif user_input == "d":
            print("\n", "*"*50)
            print("You selected to delete 1  node")
            new_graph = delete_node(graph)
            if new_graph == -1 :
                print("ERROR in deleting Node!!")

            length_of_graph = len(new_graph[0])
            print("Current Graph has ", length_of_graph, " number of nodes")
            print("New Graphs is : ", new_graph)
            min_path, route = calroute(new_graph, s)
            print("Min Path Distance is : " , min_path)
            print("Route for Min Path Distance is : " , route)
            plot_nodes(graph)
            print("\n", "*"*50)
            user_input = input("Enter your choice : ")
        
        elif user_input == "e":
            print("\n", "*"*50)
            print("You selected to leave. Bye !")
            sys.exit(1)
        
        else :
            print("Wrong Input!! Kindly Re-enter.")
            user_input = input("Enter your choice : ")
    

if __name__ == "__main__": 
    main()



             

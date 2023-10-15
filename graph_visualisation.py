
G= nx.Graph()
for i in range(n):
    for j in range(n):
        if distance[i][j]>0:
            G.add_edge(i,j,weight=distance[i][j],capacity=fuel[i][j])

node_labels={}
for i in range(n):
    node_labels[i] = (i,station[i])

edge_labels={}
for i in range(n):
    for j in range(n):
        edge_labels[(i,j)]=(distance[i][j],fuel[i][j])

pos = nx.spring_layout(G,seed=7)
nx.draw_networkx_nodes(G,pos, node_size=1800)
nx.draw_networkx_edges(G,pos)
nx.draw_networkx_labels(G,pos,node_labels)
nx.draw_networkx_edge_labels(G,pos,edge_labels,font_color="red")
plt.show()